#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 01:07:49 2020

@author: massimacbookpro
"""
from Tests import Unit_test

from Algos import Djikastra,Renderer

@Unit_test
class Djikastra_Test():
    def __init__(self,graph,*args,**kwargs):
        self._instance = Djikastra(graph)
        
    def __getattr__(self,attr):
        
        if attr=="solve":
            return lambda source,dest,*args,**kwargs: getattr(self._instance,attr)(source,dest)
    
        attr = getattr(self._instance,attr)
        if not attr:
            raise Exception("Attribute does not exist")
            
        return attr
    
@Unit_test
class Renderer_Test():
    def __init__(self,graph,*args,**kwargs):
        self._instance = Renderer(graph)
        
    def __getattr__(self,attr):
        
        if attr=="get_path":
            return lambda source,dest,*args,**kwargs: getattr(self._instance,attr)(source,dest)
    
        attr = getattr(self._instance,attr)
        if not attr:
            raise Exception("Attribute does not exist")
            
        return attr
        
    
