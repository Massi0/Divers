#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:46:45 2020

@author: massimacbookpro
"""
from Tests import unittest
from Algos import Graph



class GraphSearchTest (unittest.TestCase):
    def __init__(self, methodName="runTest", nodes=None, expected=None,value=None):
             
        super(GraphSearchTest, self).__init__(methodName)
        self.nodes = nodes
        self.expected = expected
        self.value = value
        
        
    @staticmethod
    def parametrizeTest(testcase_klass, nodes=None, expected=None,value=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, nodes=nodes, expected=expected,value=value))
        return suite