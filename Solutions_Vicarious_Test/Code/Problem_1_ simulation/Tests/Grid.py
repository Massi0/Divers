#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 02:22:08 2020

@author: massimacbookpro
"""
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fill_cell(cell, corner, rad):
    m, n = cell.shape
    ctr = corner[0], corner[1]
    x = np.linspace(0,10,n) 
    y = np.linspace(0,10,n) 
    X,Y = np.meshgrid(x, y, indexing='ij')  # could try order='xy'
    Z = (((X-ctr[0])**2 + (Y-ctr[1])**2)<= rad**2).astype(cell.dtype)
    return X,Y,Z





if __name__=="__main__":
    n = 100
    empty_lattice = np.ones((n,n))
    radius = .3
    X,Y,Z = fill_cell(empty_lattice, (5,5),radius)
    
    fig, ax = plt.subplots()
    ax.imshow(Z)
    ax.patch.set_facecolor("red")
    print(Z.shape)