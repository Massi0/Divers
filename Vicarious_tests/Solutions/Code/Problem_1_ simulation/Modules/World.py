#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:37:35 2020

@author: massimacbookpro
"""

import numpy as np 

from Modules import *


class RedZone:
    #This class defines the No Go zones where the robot is not permitted to go.
    
    def __init__(self,bottom_left,top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right
        
    
    def is_robot_in(self,bottom_left,top_right):
        xl = self.bottom_left[0]
        xr = self.top_right[0]
        yb = self.bottom_left[1]
        yt = self.top_right[1]
        
        
        for x,y in [top_right,bottom_left]:
            if x>=xl and x<=xr and y>=yb and y<=yt:
                return True

        return False
    
class Grid:
    #This class defines the mesh or grid, i.e. a descretizaiton of the world
    #it will be used to store the robot cleaned area
    def __init__(self, bottom_left, top_right, ncells):
        
        self.cells = np.zeros((ncells,ncells)) #creat a grid of size ncells x ncells
        
        self.cells_init = np.zeros((ncells,ncells)) #keep a persistant copy of the init world 
        
        x = np.linspace(bottom_left[0],top_right[0],ncells) 
        y = np.linspace(bottom_left[1],top_right[1],ncells)  
        X,Y = np.meshgrid(x, y, indexing='ij')
        self.X = X
        self.Y = Y
        
    def reinitialize(self):
        #reinit the cells value to zeros
        
        self.cells = self.cells_init.copy() 
        
    def fill_robot(self, pos, rad):
        #fill the cells that represent the area that is cleaned now by the robot
        Z = (((self.X-pos[0])**2 + (self.Y-pos[1])**2)<= rad**2).astype(self.cells.dtype)
        self.cells += Z
        
    def fill_path(self,robot):
        #robot is an instance of the class Robot
        xs,ys,rad = robot.get_path()
        
        for pos in zip(xs,ys):
            self.fill_robot(pos,rad)
            
    def fill_rect(self,bottom_left,length,width):
        #fill the cells that represent an obstacle with value -1
        xc = self.X-bottom_left[0]
        yc = self.Y-bottom_left[1]
        Z = (xc <= width).astype(self.cells.dtype)*(xc >=0).astype(self.cells.dtype)
        Z *= (yc <= length).astype(self.cells.dtype) * (yc >=0).astype(self.cells.dtype)
        Z *= -1
        self.cells +=  Z
        self.cells_init = self.cells.copy()
        
    def get_cells(self):
        return self.cells
    
    
            
        
        
        
    
        
        
        
class World:
    
    #In this, the scene or the environnement where the robot will move is defined. 
    #It handles the clock ticks, the collisions ..etc
    #The world is defined by a list of list of go and rectanglar NoGo zones. 
    
    
    def __init__(self, robot, bottom_left, top_right,dt=.1,ncells=100):
        self.robot = robot
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.nogo_zones = []
        self.time = 0
        self.dt = dt
        self.grid = Grid(bottom_left, top_right, ncells)
        
    def add_RedZone(self,bottom_left,top_right, update_grid=True):
        #Add a no go zone that the robot should avoid to collide with
        self.nogo_zones.append(RedZone(bottom_left,top_right))
        length = top_right[0]-bottom_left[0]
        width = top_right[1]-bottom_left[1]
        self.grid.fill_rect(bottom_left, length, width)
        
     
    
   
    def is_robot_in(self,bottom_left,top_right):
        #Check if the robot is in the world
        #True if the robot is in the world otherwise false
        xl = self.bottom_left[0]
        xr = self.top_right[0]
        yb = self.bottom_left[1]
        yt = self.top_right[1]
        
        res = True
        for x,y in [top_right,bottom_left]:
            if not(x>=xl and x<=xr and y>=yb and y<=yt):
                res &= False
           

        return res


    def isCollision(self,x=None,y=None):
        #check if a collision occured
        #True if occured otherwise False
        for red_zone in self.nogo_zones:
            if red_zone.is_robot_in(*self.robot.get_BoundingBox(x,y)):
                return True
        
           
        return not self.is_robot_in(*self.robot.get_BoundingBox(x,y))
            
    
    
    def step(self,t):
        #move the robot for one time step.
        #Check the collision and the other canditions
        x,y,th = self.robot.get_next(dt=self.dt)
        heading = th
        while self.isCollision(x,y):
            heading = self.robot.get_control(self) #get a control strategy (heading angle) either randomely or more smartly
            x,y,th = self.robot.get_next(u=heading,dt=self.dt)
            
        self.robot.move(x,y,th,t)
        self.robot.update_control(heading)
        return x,y,t
        
        
    def run(self,final_time,fill_grid=True):
        #run the world until the clock hit the final_timme value
        #if fill_grid is True, update the cells that are covered in the Grid
        t=0
        
        while t<final_time:
            t += self.dt
            x,y,t = self.step(t)
            self.grid.fill_robot((x,y), self.robot.radius)
            self.time = t
            
            
    def conditional_run(self, candition, *args, **kwargs):
        #run the world until "candition" is true
        
        t=0
        
        while candition(*args, **kwargs):
            t += self.dt
            x,y,t = self.step(t)
            self.grid.fill_robot((x,y), self.robot.radius)
            self.time = t
        
        
    def get_random_pos(self,dh=100):
        #return a random position within the world. 
        #dh is the descretization param
        xl = self.bottom_left[0]
        xr = self.top_right[0]
        yb = self.bottom_left[1]
        yt = self.top_right[1]
        X = np.linspace(xl,xr,dh)
        Y = np.linspace(xl,xr,dh)
        x,y = (-1,-1)
        while(self.isCollision(x,y)):
            x = np.random.choice(X)
            y = np.random.choice(Y)
            
        return x,y
        
        
        
            
    def get_coverage(self):
        Z = self.grid.get_cells() #get the cells
    
        n, m = Z.shape
        # obs_cells = np.nonzero(Z<0) #remove the cells that represent the no go zone
    
        # return (np.nonzero(Z>0)[0].shape[0]-obs_cells[0].shape[0])/(n*m-obs_cells[0].shape[0])
        return (np.nonzero(Z>0)[0].shape[0])/(np.nonzero(Z>=0)[0].shape[0])
            
        
    def reinitialize(self,random_init_pos=True):
        #reinitialize the world with random postion if random_init_pos is true
        if random_init_pos:
            r_pos =  self.get_random_pos() #random valid position
            th0 = np.random.choice(self.robot.controls_list)
        else:
            *r_pos,th0 = self.robot.pos[0]
        # print(r_pos, th0)
        self.robot.reinitialize((r_pos[0],r_pos[1],th0))
        self.grid.reinitialize()
        self.time = 0
        
                
            
        
        
        
        
        
        
        
    
        
        
        