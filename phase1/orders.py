#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:56:41 2020

@author: isegura
"""

from myqueue import SQueue

class Package:
    """Class for one package"""
    def __init__(self,idpac,street,num,pc):
        self.idpac=idpac
        self.street=street
        self.num=num
        self.pc=pc
        #By default the number of attempts for a package is 0
        self.numAttempts = 0
    
    def __str__(self):
    
        return( str(self.idpac)+' ' + str(self.street)+' ' + 
               str(self.num)+' ' + str(self.pc)+ ', ' + str(self.numAttempts))
     #Add any method you may need

    
class Orders(SQueue):
    pass
    #Add any method you may need

class Deliveredpackage:
    def __init__(self, idpac, iddsm):
        self.idpac = idpac
        self.iddsm = iddsm
        
    def __str__(self):
        return str(self.idpac) + ' '  +  str(self.iddsm) 
    
    
class Delivered(SQueue):
    pass
    """To represent packages successfully delivered"""
    #Add any method you may need

class Incident:
    def __init__(self, idpac, iddsm, reason):
        self.idpac = idpac
        self.iddsm = iddsm
        self.reason = reason
        
    def __str__(self):
        return str(self.idpac) +' '+ str(self.iddsm) +' '  + str(self.reason)
            
class Incidents(SQueue):
    pass
    """To represent packages that have suffered some incident"""
    #Add any method you may need

 