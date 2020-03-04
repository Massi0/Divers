#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 02:22:43 2020

@author: massimacbookpro
"""
# from Tests import Unit_test


from Tests import unittest,DjikastraTest,GraphSearchTest
from Algos import *
# from Tests import Djikastra_TEST


if __name__== "__main__":
    test_inputs = range(9)
    test_values_output = [0,4,12,19,21,11,9,8,14]
    
    
    suite = unittest.TestSuite()
    for dest,eValue in zip(test_inputs,test_values_output):
        suite.addTest(GraphSearchTest.parametrizeTest(DjikastraTest, 
                                                      nodes=(0,dest),
                                                      expected=True,
                                                      value=eValue))
  
    unittest.TextTestRunner(verbosity=2).run(suite)

