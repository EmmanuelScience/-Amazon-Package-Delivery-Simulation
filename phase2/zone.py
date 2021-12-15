# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:24:15 2020

@author: Godfire
"""
from binarysearchtrees import BinarySearchTree


class Zone(BinarySearchTree):
    '''A zone class its that inherits the Bst, it ahs an attribute pc to save 
    the postal code'''
    def __init__(self, value):
        super().__init__()
        self.pc = value
        
    
    def __eq__(self, other):
        if self.pc == other.pc:
            return True
       # return (self.cp == other.cp)
   
    def __gt__(self, other):
       return (self.pc > other.pc)
   
    def __lt__(self, other):
       return (self.pc < other.pc)
   
    def __ge__(self, other):
       return (self.pc >= other.pc)
   
    def __le__(self, other):
       return (self.pc <= other.pc)
   
    def __str__(self):
        return str(self.pc)
    

      
      
      
      
      

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      