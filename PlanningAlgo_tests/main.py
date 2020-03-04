#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 02:22:43 2020

@author: massimacbookpro
"""
# from Tests import Unit_test

from Algos import *
from Tests import *
# from Tests import Djikastra_TEST



if __name__=="__main__":
    
    print("Hello" )
    
    
    graph = Graph()
    
    test_inputs = range(9)
    test_values_output = [0,4,12,19,21,11,9,8,14]

    V = [ 
            [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
            [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
            [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
            [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
            [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
            [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
            [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
            [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
            [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] 
        ]
    graph.initialize(V=V)
    djikastra_test = Djikastra_Test(graph)
    renderer_test = Renderer_Test(graph)
    
    for dest,eV in zip(test_inputs,test_values_output):
        
        
        kwargs = {'expected_values': True,
                  'source': 0,
                  'dest': dest}
        
        res = djikastra_test.check(attr="solve", **kwargs)
        
        
        kwargs = {'expected_values': [None, eV],
                  'source': 0,
                  'dest': dest}
        res = res & renderer_test.check(attr="get_path", **kwargs)
        
        if not res:
            print("Failed --> Djikastra failed at eV={}, input:(0,{})".format(eV,dest))
            continue
        
        print("Successed --> input(input:(0,{})".format(dest))
    
