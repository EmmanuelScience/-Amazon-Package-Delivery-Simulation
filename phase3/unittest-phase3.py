#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:12:32 2020

@author: isegura
"""

import unittest
from phase3 import Map
from phase3 import DeliveryPoint


class Test(unittest.TestCase):
    def setUp(self):
        print('\ninitializing data...\n')
        
        #https://github.com/isegura/EDA/blob/master/grafoEjemplo.png
        #Create delivery points
        self.pA=DeliveryPoint('C/A',1,28921)             #A
        self.pB=DeliveryPoint('C/B',2,28921)             #B
        self.pC=DeliveryPoint('C/C',3,28922)             #C
        self.pD=DeliveryPoint('C/D',4,28922)             #D
        self.pE=DeliveryPoint('C/E',5,28923)             #E
        self.pF=DeliveryPoint('C/F',6,28923)             #F
        self.pG=DeliveryPoint('C/G',6,28923)             #G


        self.points=[self.pA,self.pB,self.pC,self.pD,self.pE,self.pF,self.pG]
        self.m=Map()
        for p in self.points:
            #m.addDeliveryPoint(DeliveryPoint(v,5,28911))
            self.m.addDeliveryPoint(p)
        
        #print(self.m)
        
        self.m.addConnection(self.pA,self.pB,8)                    #A,B,8
        self.m.addConnection(self.pA,self.pC,9)                    #A,C,9
        self.m.addConnection(self.pA,self.pD,14)                   #A,D,14
        
        self.m.addConnection(self.pB,self.pE,15)                   #B,E,15
        self.m.addConnection(self.pB,self.pF,11)                   #B,F,11
        
        self.m.addConnection(self.pC,self.pF,2)                    #C,F,2
        
        self.m.addConnection(self.pF,self.pG,8)                    #F,G,8
        self.m.addConnection(self.pD,self.pG,2)                    #D,G,2


        #print(self.m)
        
        
        # route applying dfs: A B E F C G D
        self.rutaDFS=[self.pA,self.pB,self.pE,self.pF,self.pC,self.pG,self.pD]
            
    
        #self.m.dijkstra()
        
        self.min_A_G=[self.pA,self.pD,self.pG]
        self.dis_A_G=16
        
        self.min_B_D=[self.pB,self.pF,self.pG,self.pD]
        self.dis_B_D=21
        
        self.min_E_D=[self.pE,self.pB,self.pF,self.pG,self.pD]
        self.dis_E_D=36
        
        

        
    def test1_areConnected(self):
        #check pA connections
        print('\n****** test1_areConnected ******************')
        self.assertEqual(self.m.areConnected(self.pA,self.pB),8)
        self.assertEqual(self.m.areConnected(self.pA,self.pC),9)
        self.assertEqual(self.m.areConnected(self.pA,self.pD),14)
        #and the reverse connections
        self.assertEqual(self.m.areConnected(self.pB,self.pA),8)
        #check some non connected
        self.assertEqual(self.m.areConnected(self.pA,self.pE),0)
        self.assertEqual(self.m.areConnected(self.pA,self.pF),0)
        self.assertEqual(self.m.areConnected(self.pA,self.pG),0)

        print('****** OK test1_areConnected ******************')

        
    
    def test2_deleteConnection(self):
        print('\n******  test2_deleteConnection ******************')
        self.assertEqual(self.m.areConnected(self.pB,self.pC),0)
        self.m.addConnection(self.pB,self.pC,10) #B,C,10
        self.assertEqual(self.m.areConnected(self.pB,self.pC),10)
        self.m.deleteConnection(self.pB,self.pC)
        self.assertEqual(self.m.areConnected(self.pB,self.pC),0)
        
        print('****** OK test2_deleteConnection ******************')

    def test3_generateRoute(self):
        print('\n****** test3_generateRoute ******************')
        result=self.m.generateRoute()
        self.assertEqual(len(result),len(self.rutaDFS))
        for i in range(len(result)):
            #print(result[i],self.rutaDFS[i])
            self.assertEqual(result[i],self.rutaDFS[i])
        print('****** OK test3_generateRoute ******************')
        

    def test4_minRoute(self):
        print('\n******  test4_minRoute ******************')
        result,d=self.m.minRoute(self.pA,self.pG)
        self.assertEqual(d,self.dis_A_G)
        self.assertEqual(len(result),len(self.min_A_G))
        for i in range(len(result)):
            self.assertEqual(result[i],self.min_A_G[i])
        print('****** OK test4_minRoute******************')

    
#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()