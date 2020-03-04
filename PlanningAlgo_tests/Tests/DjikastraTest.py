#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:45:46 2020

@author: massimacbookpro
"""

from Algos import Djikastra,Renderer,Graph

from Tests import GraphSearchTest,unittest




# import unittest

class DjikastraTest(GraphSearchTest):
    
    
    def __init__(self,*args,**kwargs):

        self.graph = Graph()
        V = [ 
            [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
            [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
            [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
            [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
            [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
            [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
            [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
            [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
            [ 0, 0, 2, 0, 0, 0, 6, 7, 0  ] 
            ]
        
        self.graph.initialize(V=V)
        super(DjikastraTest,self).__init__(*args,**kwargs)

    
    #     test_inputs = range(9)
    #     test_values_output = [0,4,12,19,21,11,9,8,14]
    
    #     V = [ 
    #         [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
    #         [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
    #         [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
    #         [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
    #         [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
    #         [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
    #         [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
    #         [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
    #         [ 0, 0, 2, 0, 0, 0, 6, 7, 0  ] 
    #         ]
    #     self.graph.initialize(V=V)

        
    def test_solver_success(self):
        # self.graph = Graph()
        
        
        source, dest = self.nodes
        expected = self.expected
        djikastra = Djikastra(self.graph)
        
        self.assertEqual(djikastra.solve(source,dest), expected, "Should be {}".format(expected))
        
        
    def test_solver_value(self):
        source, dest = self.nodes
        value = self.value
        
        renderer = Renderer(self.graph)
        djikastra = Djikastra(self.graph)
        
        djikastra.solve(source,dest)
        
        _,estVal = renderer.get_path(source,dest)
        
        self.assertEqual(estVal, value, "Should be {}".format(value))
        
   
    
    
    
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(GraphSearchTest.parametrizeTest(DjikastraTest, nodes=(0,2),expected=True,value=12))
    # suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
    unittest.TextTestRunner(verbosity=2).run(suite)