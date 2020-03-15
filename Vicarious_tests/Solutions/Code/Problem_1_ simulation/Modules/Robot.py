#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:14:51 2020

@author: massimacbookpro
"""

import numpy as np 

class Robot:
    def __init__(self,x0,y0,th0,radius=.25,v=.1,th_nsamples = 10):
        #x0,y0: euclidean coor of the init position
        #th0: initial orientation
        #dt: the time discretization (the robot will move at each dt)
        #v: velocity of the robot
 
        self.pos = [(x0,y0,th0)]#store the position of the robot over time
        self.times = [0] #store the different discret times
        self.v = v
        self.radius = radius
        self.control = th0 #direction control (defined online )
        self.controls_list = np.linspace(0,2*np.pi,th_nsamples)
        
    
    def reinitialize(self,pos):
        x0,y0,th0 = pos
        self.pos = [(x0,y0,th0)]#store the position of the robot over time
        self.times = [0]
        self.control = th0
    def get_next(self, dt,u=None):
        #return the potiential next position
        #The dynamics are :
        #x_{n+1} = dt*v*cos(self.control)+x_n
        #y_{n+1} = dt*v*sin(self.control)+y_n
        x,y,th = self.pos[-1]
        if u is None:
            u = self.control
            
        x += dt*self.v*np.cos(u)
        y += dt*self.v*np.sin(u)
        
        return (x,y,self.control)
        
    
    def move(self,x,y,th,t):
        #update the position
        self.pos.append((x,y,th))
        self.times.append(t)
        
        
    def update_control(self,u):
        self.control = u
        
        
    def get_control(self,*args,**kwargs):
        return self.get_random_heading()
    
    
    def get_random_heading(self):
        return np.random.choice(self.controls_list)
    
    
    def get_distance_to(self,xp, yp):
        #return the distance from the point p
        
        x,y,_ = self.pos[-1]
        
        
        return np.sqrt(( x- xp)**2 + (y - yp)**2)


    def get_BoundingBox(self,x=None,y=None):
        if x is None or y is None:
            x,y,_ = self.pos[-1]
            
        r = self.radius
        bottom_left = (x-r, y-r)
        top_right = (x+r, y+r)
        
        return bottom_left,top_right
    
    def get_path(self):
        #return the path i.e. the history of positions of the robot
        pos = np.array(self.pos)
        x,y = pos[:,0],pos[:,1]
        
        return x,y,self.radius
    
    