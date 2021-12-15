#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:57:54 2020

@author: isegura
"""

from dlist import DList
from dlist import DNode
from orders import Orders

class Zones(DList):
    pass
       #Add any method you may need


class DSMember:
    """Class for a DSMember"""
    def __init__(self,iddsm,name,status,zones):
        self.iddsm=iddsm
        self.name=name
        self.status=status
        self.zones=Zones()
        self.str = ''
        for z in zones:
            self.zones.addLast(z)
            if zones[0] == z:
                self.str +=str(z)
            else:
                self.str += ', ' + str(z) 
            
        self.orders=Orders()
        
    def __str__(self):
        if self.orders.isEmpty():
            return (' DSmember: ' + str(self.iddsm) +', ' + str(self.name) + ', ' 
                + str(self.status) + ', ' + 'Zones: ' + str(self.str))
        
        return (' DSmember: ' + str(self.iddsm) +', ' + str(self.name) + ', ' 
                + str(self.status) + ', ' + 'Zones: ' + str(self.str) +'\n' +
                '\t Packages: \n' + '\t\t' +str(self.orders))
    #Add any method you may need
    
class DSMembers(DList):
    def __init__(self):
        super().__init__()
        self.value = 0
       #Add any method you may need

        
    