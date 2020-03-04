#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:58:38 2020

@author: massimacbookpro
"""
import numpy as np

from Algos.tools import Node,Graph


class Djikastra:
    def __init__(self,graph):
        self.graph = graph
        self.visited_nodes = []
        self.unvisited_nodes = list(graph.nodes)
        self.nodes = list(graph.nodes)
        
    
        
    def solve_(self,source,dest):  
        
        while (len(self.unvisited_nodes) >0):
            node_i = min(self.unvisited_nodes, 
                    key=lambda node: node.value)
            
            self.unvisited_nodes.remove(node_i)
            
            for node_j in self.unvisited_nodes:
                dij = self.graph.get_value(node_i,node_j)
                if dij == 0 :
                    continue
                
                if node_j.update_value(dij+node_i.get_value()):
                    node_j.set_prev(node_i)
                
                if node_j == dest:
                    return True
                    
        return True
                
                
                
    def solve(self,source_idx,dest_idx):      
        self.unvisited_nodes = list(self.graph.nodes)
        self.nodes = list(self.graph.nodes)
        
        source = self.unvisited_nodes[source_idx]
        dest = self.unvisited_nodes[dest_idx]
        
        for node in self.nodes:
            node.value = np.Inf
            node.set_prev(0)
        source.update_value(0)
        return self.solve_(source,dest)
            


class Renderer:
    def __init__(self, graph):
        self.graph = graph
        
        
    def get_path(self,source, dest):
        path = []
        source = self.graph.nodes[source]
        dest = self.graph.nodes[dest]
        node = dest
        v = 0
        while(True):
            path.append(node)
            if not node or not node.prev :
                break
            v += self.graph.get_value(node.prev,node)
            node = node.prev
            
        path.reverse()
        return path,v
        
