#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:07:03 2020

@author: massimacbookpro
"""

import numpy as np
import sys


class Node:
    
    def __init__(self,id):
        self.id = id
        self.value = 1e10
        self.prev = None;
        self
        
    def update_value(self,val):
        if val<self.value :
            self.value = val 
            return True
        
        return False
    
    def set_prev(self,prev):
        self.prev = prev
        
    def get_value(self):
        return self.value
        
        

class Graph:
    def __init__(self,V=None):
        self.V = V
        self.nodes = []
        
    def initialize(self,**kwargs):
        V = kwargs.get("V") 
        if V is not None:
            self.V = V
            
        if self.V is None:
            raise Exception("None Edges found")
        
        for id in range(np.shape(V)[0]):
            self.nodes.append(Node(id))
            
    def get_value(self,i,j):
        ii = self.nodes.index(i) if not isinstance(i,int) else i
        jj = self.nodes.index(j) if not isinstance(j,int) else j
        return self.V[ii][jj]
            
        
            
            


        
        
        
    