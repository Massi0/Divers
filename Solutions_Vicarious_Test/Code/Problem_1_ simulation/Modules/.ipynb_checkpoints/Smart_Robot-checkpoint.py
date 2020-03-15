#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:01:17 2020

@author: massimacbookpro
"""

import numpy as np 

from Modules import *

class Smart_Robot(Robot):
    #This class is the same as the Robot class with the difference that the controller is generated smartly
    #by having feedback on the clean area
    def get_control(self,world,*args,**kwargs):
        
        X = world.grid.X
        Y = world.grid.Y
        cells = world.grid.get_cells()
        pos = self.pos[-1]
        eps = .05
        
        #find the cells along the circumference of the robot
        Z = (((X-pos[0])**2 + (Y-pos[1])**2) <= self.radius**2+eps).astype(cells.dtype)
        Z *= (((X-pos[0])**2 + (Y-pos[1])**2) >= self.radius**2-eps).astype(cells.dtype)
        
         
        n,_ = cells.shape
        
        #find circumference cells
        d_cells = np.nonzero(Z) 
       
        
        d_cells = [(x,y) for x,y in zip(d_cells[0],d_cells[1])]
        
        max_attempts = 100 #put a bound on  attempts to find dirty or clean (important when the area is very clean or dirty)
        i = 0
        
        #choose dirty with probability 2/3
        if np.random.randint(0,3)<2:
            idx = np.random.choice(range(len(d_cells)))
            
            #pick a dirty cell
            while (cells[d_cells[idx]] != 0 and i<max_attempts):
                idx = np.random.choice(range(len(d_cells)))
                i += 1
                
            x,y = d_cells[idx]
            x *= 10/n
            y *= 10/n
            
            th = np.arctan2(y-pos[1],x-pos[0])
        #choose from clean    
        else:
            idx = np.random.choice(range(len(d_cells)))
          
            while (cells[d_cells[idx]] == 0 and i<max_attempts):
                idx = np.random.choice(range(len(d_cells)))
                i += 1
                
            x,y = d_cells[idx]
            
            x *= 10/n
            y *= 10/n
            
            th = np.arctan2(y-pos[1],x-pos[0])
            
        return th
            
            
        