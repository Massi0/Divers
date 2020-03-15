#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:52:23 2020

@author: massimacbookpro
"""

from Modules import Robot, World, Smart_Robot

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
    

def plot_path():
    dt = .5 #sampling time
    r_radius = .25/2# robot radis
    r_pos = (7.5,2,5) #robot init position as plot in the problem
    
    robot = Smart_Robot(x0=r_pos[0],
                  y0=r_pos[1],
                  th0=5*np.pi/4,
                  v=.1,
                  radius=r_radius,
                  th_nsamples = 100)
    
    #Define the world as a rectangle 
    world = World(robot,
                  bottom_left = (0,0),
                  top_right = (10,10),
                  dt=dt,
                  ncells = 150)
    
    #Add a rectangular No Go zone where the robot cannot go
    world.add_RedZone(bottom_left = (5,5),
                      top_right = (10,10))
    
    

    # world.run(50*60)

    world.reinitialize(random_init_pos=True)
    world.conditional_run(lambda world: world.time<40*60,  world )
        
    
    #Post processing 
    pos = np.array(robot.pos)

    fig,(ax1,ax2) = plt.subplots(2,1)
    
    # # Create a Rectangle patch (No go zone) and cicle
    rect = patches.Rectangle((5,5),5,5,linewidth=1,edgecolor='r',facecolor='r')
    circ = patches.Circle(r_pos, radius=r_radius,edgecolor='g',facecolor='g')
    ax1.add_patch(rect)
    ax1.add_patch(circ)
    
    ax1.plot(pos[::5,0],pos[::5,1])
    ax1.axis([0,10,0,10])
    ax1.grid()
    
    Z = world.grid.get_cells() #get the cells
    print(np.min(Z))
    obs_cells = np.nonzero(Z<0) #Cells that represent the no go zone 
    
    #remove the cells that represent the no go zone
    
    print(world.get_coverage())
    
    Z[obs_cells]= 0

    ax2.imshow(np.rot90(Z))
    # ax.patch.set_facecolor("red")
    
    
  
    
def find_average_time_of_cleaning(ratio=.75):
    dt = .9 #sampling time
    r_radius = .25/2 # robot radis
    r_pos = (7.5,2,5) #robot init position
    robot = Smart_Robot(x0=r_pos[0],
                  y0=r_pos[1],
                  th0=5*np.pi/4,
                  v=.1,
                  radius=r_radius,
                  th_nsamples = 1000)
    
    #Define the world as a rectangle 
    world = World(robot,
                  bottom_left = (0,0),
                  top_right = (10,10),
                  dt=dt,
                  ncells = 100)
    
    #Add a rectangular No Go zone where the robot cannot go
    world.add_RedZone(bottom_left = (5,5),
                      top_right = (10,10))
    
    
    n_samplings = 1400*2
    sum_time = 0
    
    for i in range(1,n_samplings):
        world.reinitialize(random_init_pos=True) # reinit the whole scenario (with new init position and cells)
        world.conditional_run(lambda world: world.get_coverage()<ratio,  world )
        sum_time += world.time
        if i%10 == 0:
            print("run {}: average time to cover {} is {:0.2f} min".format(i,ratio,sum_time/i/60))
        
    print("--> Average time to cover {} is {:0.2f} hours".format(ratio,sum_time/i/3600))
    




if __name__=="__main__":
    # plot_path()
    find_average_time_of_cleaning(ratio = .75)