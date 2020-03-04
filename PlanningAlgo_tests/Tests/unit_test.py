#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:30:05 2020

@author: massimacbookpro
"""

class Unit_test:
    def __init__(self,klass,*args,**kwargs):
        self._instance = None
        self.klass= klass
        
            
    def __call__(self,*args,**kwargs):
        if not self._instance:
            self._instance = self.klass(*args,**kwargs)
            
        return self
            
            
            
    def check(self,*args,**kwargs):
        attr = kwargs.get("attr")
        expected_values = kwargs.get("expected_values")
        if not attr:
            raise Exception("The method to be tested is not specified")
            
        self._func = getattr(self._instance,attr)
         
        if not callable(self._func):
            raise Exception("Method is not callable")
            
        
        values = self._func(*args,**kwargs)
        if isinstance(expected_values,list) or isinstance(values,tuple) :
            if len(values) != len(expected_values):
                return False 
        
        
            for val,eV in zip(values,expected_values):
                if not eV:
                    continue
                
                if eV!=val:
                    return False
        else:
            return values == expected_values
            
            
        return True
    
    
        