# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:15:11 2020

@author: Godfire
"""

from zone import Zone
from binarysearchtrees import BinarySearchTree



class Zones:
    def __init__(self):
        '''This method contains all the attributes of the AmaZone class'''
        self.zones = BinarySearchTree()
        self.root = self.zones.root
        
    
    def createZone(self, cp):
        '''This method recieves a postal code, makes it as a zone attribute and
        adds it to the zone object, which is Tree, using the insert method, 
        the complexity of the insert method is log(n)'''
        
        print('Creating zone: ', cp)
        zone = Zone(cp)
        # the zones object is a binary search tree, so inserting an element in 
        # it would have a complexity of log(n) as requested
        self.zones.insert(zone)
            
    
    def assignsDistributor(self, CP, DSMember):  
        '''this method takes in a postal code, searches through the zones tree
        taking into consideration that the each zone is a list, when the 
        the current zone is found, the DSMember is added to the zone'''
        
        print(' \nAssigning ', DSMember, ' to zone', CP)
        temp = Zone(CP)
        currentzone = self.zones.find(temp).elem
        currentzone.insert(DSMember)

                 

    def showDistributors(self, CP):
        '''This method takes a zone as parameter, finds it in the tree and
        if prints out all the Distrubutor assigned to it alphabetically'''
        
        print('Showing distributors for: ', CP)
        temp = Zone(CP)
        currentzone = self.zones.find(temp).elem
        # it uses an inorder method to traverse the tree, as the dsmembers are
        # stored as a tree
        if currentzone.size() != 0:
            currentzone.inorder()
            print('\n')
        else:
            print('No distributor available\n')
        return currentzone.makelist()
    
    def deleteDistributor(self, CP, DSMember):
        '''this method takes a postal code and a DSMember, finds the postal
        then deletes the dsmember from it is it exists'''
        temp = Zone(CP)
        currentzone = self.zones.find(temp).elem
        if currentzone:
            print('\nRemoving ', DSMember, ' from zone: ', CP)
            print(currentzone.remove(DSMember))
        else:
            print('DSMember does not exst')
        
    
    def showZones(self):
        '''This method prints out all the zones and their members, it simply
        uses the inorder traversal'''
        
        self.zones.inorder1()
        # the makelist method is a method in the BST class, and returns the 
        # tree as a list in  an orderly fashion
        return self.zones.makelist()
        
        
        
        
    def _redistribute_right(self, lis, count, dlis, k):
        ''' this is a private method created specifically for the deletezone, 
         it takes a list(lis) the list of zones to the right of the zone we 
         want to delete, count; the position close to the zone we want to 
         delete, dlis; the list of dsmembers in the zone wewant to delete,and k
         the amount of dsmembers we want to delete'''
        counter = count
        while k > 0:
            # it distrubutes all the dsmemebrs as evenly as possible until
            # there is none left
            lis.getAt(counter).insert(dlis.removeLast())
            if counter == lis.size-1:
                counter = count-1
            counter += 1
            k -= 1
            
    def _redistribute_left(self, lis, count, dlis, k):
        ''' this is a private method created specifically for the deletezone, 
         it takes a list(lis) the list of zones to the left of the zone we 
         want to delete, count; the position close to the zone we want to 
         delete, dlis; the list of dsmembers in the zone wewant to delete,and k
         the amount of dsmembers we want to delete'''
        counter = count
        while k > 0:
            # it distrubutes all the dsmemebrs as evenly as possible until
            # there is none left
            lis.getAt(counter).insert(dlis.removeLast())
            if counter == 0:
                counter = count+1
            counter -= 1
            k-= 1
     
     
    def deleteZone(self, CP):
        '''This method takes a Zone postal code, distributes the dsmembers and
        deletes the zone'''
        # first we make a list of the zones
        mylis = self.zones.makelist()
        temp = Zone(CP)
        # find the zone
        currentnode = self.zones.find(temp).elem
        # make a list of the zone dsmembers
        dlis = currentnode.makelist()
        # get the index of zone in the created list
        index = mylis.index(currentnode)
        # get the amount of dsmembers in the zone
        k = currentnode.size()
        # divide them in 2 parts
        k2 = k//2
        k22 = k - k2
        # And then redistrubute the dsmembers as described in each of the 
        # redistribute methods
        if mylis.head.elem == currentnode:
            self._redistribute_right(mylis, 1, dlis, k)
                
        elif mylis.tail.elem == currentnode:
            self._redistribute_left(mylis, mylis.size-2, dlis, k)
            
        else:
            self._redistribute_left(mylis, index-1, dlis, k2)
            self._redistribute_right(mylis, index+1, dlis, k22)   
        # And lastly, deletes the zone
        self.zones.remove(currentnode)    
        
    def draw(self):
        '''This method draws the zones '''
        self.zones.draw()
        

        
    def isBalanced(self):
        """Checks if the tree is size-balanced"""
        return self._isBalanced(self.zones.root)
      
    def _isBalanced(self,node):
        # if we get to a node that is none, that means the tree is balanced
        # so we return true
        if node is None:
            return True
        
        # if the size difference is greater thatn 1, this means we have to
        # return false and the tree is not balanced
        if self.zones.fsize(node)>1:
            return False
        
        # finally if none of the above conditions are met, we repeat the method
        # for the left and right child
        return (self._isBalanced(node.leftChild) and
                self._isBalanced(node.rightChild))       
    

        
    def balance(self):
        '''A method that is used to balance the tree using the sizebalance 
        technique'''
        self._balance(self.root)
        
    def _balance(self, node):
        # firstly if the node is none, we have to return and stop the 
        # recursion
        if  node == None:
            return
        
        # then we check the size differnce between the left and right child
        if (self.sizeOf(node.leftChild) - self.sizeOf(node.rightChild)) > 1:
            # if the size of the left child is greater than the size of the right
            # child with more than a factor of 1, we set a variable called 
            # nodetobalance, while this variable is greter than 0
            # we replace the root node with the predecessor, and later 
            # reinsert the root element into the tree
            nodeToBalance = self.zones.fsize(node)//2
            while nodeToBalance > 0:
                rootNode = node.elem
                pred = self.zones.predecessor(node)
                self.zones.remove(pred.elem)               
                node.elem = pred.elem
                self.zones.insert(rootNode)
                nodeToBalance -= 1
        
        # Same as the above method but using the sucessor element
        elif (self.sizeOf(node.rightChild) - self.sizeOf(node.leftChild)) > 1:
            nodeToBalance = self.zones.fsize(node)//2
            while nodeToBalance > 0:
                rootNode = node.elem
                suc = self.zones.successor(node)
                self.zones.remove(suc.elem)
                node.elem = suc.elem
                self.zones.insert(rootNode)
                nodeToBalance -= 1
        self._balance(node.leftChild)
        self._balance(node.rightChild)        
    
       
    
        
        
        
        
        
        
        
        
        
        
        






































































