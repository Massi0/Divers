#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:18:33 2020

@author: massimacbookpro
"""

from Modules import Robot

import numpy as np 
import matplotlib.pyplot as plt
    
if __name__ == "__main__":
    dt = .1
    robot = Robot(x0=0,
                  y0=0,
                  th0=0,
                  v=1)
    
    
    t = 0
    ths = np.linspace(-np.pi,np.pi,100)
    
    while t<10:
        x,y,th = robot.get_next(dt=.1)
        
        
        t += dt
        robot.move(x,y,th,t)
        if int(t/dt)%40 ==0:
            u = np.random.choice(ths)
            robot.update_control(u)
            
    
    
    pos = np.array(robot.pos)
    
    
    plt.plot(pos[:,0],pos[:,1])
    plt.axis("equal")
    plt.show()
        