# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest
from phase2 import Zones


def areEqual(tree1,tree2):
    """Function to check if to zone trees are the same"""
    return areEqualNode(tree1.root,tree2.root)
    
def areEqualNode(node1,node2):
    """Function to check if 2 nodes for the zone tree are the same.
    Note!!! The distributor list for the distributors is not checked"""

    if node1==None and node2==None:
        return True
    if node1 and node2==None:
        return False
    if node1==None and node2:
        return False
    
    return node1.elem.pc==node2.elem.pc and areEqualNode(node1.left,node2.left) and areEqualNode(node1.right,node2.right)

class Test(unittest.TestCase):
    
    def setUp(self):
        print('\Initializing data (initialized for each method)...\n')
        self.lZones=[28332, 28378, 28142, 28331, 28193, 28766,28760]
        self.objZone=Zones()
        for z in self.lZones:
            self.objZone.createZone(z)
         
        
        self.pc1=28332
        self.dist28332=['Iglesias, P.','Sánchez, P.','Abascal, J.','Arrimadas, I.']
        for r in self.dist28332:
            self.objZone.assignsDistributor(self.pc1,r)
        
        
        self.pc2=28142
        self.dist28142=['Calvo, C.','Montero, MJ.','Montero, I.']
        for r in self.dist28142:
            self.objZone.assignsDistributor(self.pc2,r)
        
        
        self.pc3=28766
        self.objZone.assignsDistributor(self.pc3,'Casado, P.')


        self.pc4=28193
        self.dist28193=['Castells, M.','Grande-Marlaska, F.','Celaa, I.']
        for r in self.dist28193:
            self.objZone.assignsDistributor(self.pc4,r)
        
        
        #self.objZona.draw()

         
    def test1_zones(self):
        print('******* test1_zones ***************************************************')
        result=self.objZone.showZones()
        output=sorted(self.lZones)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).pc,output[i],'FAIL: zones are not equal')
        print('****** OK test1_zones ************************************************\n')
        
        
    def test2_distributors(self):
        print('******* test_distributors ********************************************')
        result=self.objZone.showDistributors(self.pc1)
        output=sorted(self.dist28332)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:', output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i),output[i],'FAIL: Distributors are not equal')
        print('****** OK test2_distributors *****************************************\n')

    def test3_deleteDistributor(self):
        print('******* test3_deleteDistributor *************************************************')
        nameDist='Abascal, J.'
        #print('\tborrarRepartidor() zona='+ str(self.cp1) + ", repartidor="+ nombreRep)
        self.objZone.deleteDistributor(self.pc1,nameDist)

        result=self.objZone.showDistributors(self.pc1)
        output=sorted(self.dist28332)
        output.remove(nameDist)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i),output[i],'FAIL: distributors are not equal')
#
        print('****** OK test3_deleteDistributor ************************************************\n')

        

    
    def test4_isBalanced(self):
        print()
        print('******* test4_isBalanced ***************************************')
        
        print('\tCase 1: isBalanced() for not balanced.')
        self.assertFalse(self.objZone.isBalanced(),'FAIL: the input is not balanced!!!')
        #self.objZona.draw()        
        print('\tCase 2: isBalanced() for a balanced tree.')
        #añado zonas para hacerlo balanceado
        self.objZone.createZone(28140)
        self.objZone.createZone(28375)
        #self.objZona.draw()
        self.assertTrue(self.objZone.isBalanced(),'FAIL: the input is not balanced!!!')
#        print('\n\n')

        print('******* OK test4_isBalanced ******************************')


    
    def test5_balance(self):
         print('******* test5_balance ******************************************')
         #self.objZona.draw()
         self.objZone.balance()
         #self.objZona.draw()
         aux=Zones()
         for z in [28332, 28760,28378, 28766, 28193, 28331, 28142]:
             aux.createZone(z)
         #aux.draw()
         self.assertTrue(areEqual(self.objZone,aux),'Fail: are not equal')
         
         print('******* OK test5_balance ***************************************')
 
    def test6_deleteZone(self):
        """When deleting a zone with distributors, the test does not check if the distributors 
        have been reassigned correctly. This check is done manualy by printing the tree."""
        
        print('******* test6_deleteZone (TREES MUST BE PRINTED TO CHECK THEM!!!) *****')

        pc=28378
        print('\tCase 1: deleteZone() for a pc without distributors: '+ str(pc) )
        self.objZone.deleteZone(pc)
        result=self.objZone.showZones()
        output=sorted(self.lZones)
        output.remove(pc)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).pc,output[i],'FAIL: zones are not equal')
        print()

        
        print('\tCase 2: deleteZone() for a pc with distributors: '+ str(self.pc1) )
        print('\tbefore deleting: ' + str(self.pc1)+'\n')
        self.objZone.draw()
        
        self.objZone.deleteZone(self.pc1)
        result=self.objZone.showZones()
        output.remove(self.pc1)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).pc,output[i],'FAIL: zonas are not equal')
        print()
        print('\n\tafter deleting: ' + str(self.pc1)+'\n')
        self.objZone.draw()
        print('****** OK test6_deleteZone ************************************************\n')

      
        
#Uncomment to use with Spyder
if __name__ == '__main__':
    unittest.main()