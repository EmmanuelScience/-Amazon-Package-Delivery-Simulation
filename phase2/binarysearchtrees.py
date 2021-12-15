#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:49:28 2019

@author: isegura
"""
from binarytrees import Node
from binarytrees import BinaryTree
from dlist import DList
class BinarySearchTree(BinaryTree):
    def removeLittleMan(self):
        self._removeLittleMan(self.root)
        
    def _removeLittleMan(self,node):
        if node:
            if not node.leftChild and not node.rightChild:
                if node.parent:
                    node.parent.leftChild = None
                else:
                    self.root = None
                return  
                    
            if not node.leftChild and node.rightChild:
                 if node.parent:
                    node.parent.leftChild = node.rightChild
                    
                 else:
                    self.root = node.rightChild
                    self.root.parent = None
                 return
            self._removeLittleMan(node.leftChild)
        
    def insert(self,x):
        """inserts a new node, with element x, into the tree"""
        if self.root==None:
            self.root=Node(x)
        else:
            self.insertNode(self.root,x)
            
    def insertNode(self,node,x):
        """Inserts a new node (with the element x) inside of the subtree node"""
        if node.elem==x:
            # Duplicate elements are not allowed
            print(x,'already exists!!!')
            return
        
        if x<node.elem:
            if node.leftChild!=None:
                self.insertNode(node.leftChild,x)
            else:
                newNode=Node(x)
                node.leftChild=newNode
                newNode.parent=node
        else: #x>node.elem
            if node.rightChild!=None:
                self.insertNode(node.rightChild,x)
            else:
                newNode=Node(x)
                node.rightChild=newNode
                newNode.parent=node

    def search(self,x):
        return self.searchNode(self.root,x)
    
    def searchNode(self,node,x):
        """Auxiliary method to search a node with value x"""
        if node is None:
            return False
        
        if node.elem==x:
            return True
        
        if x<node.elem:
            return self.searchNode(node.leftChild,x)
        
        if x>node.elem:
            return self.searchNode(node.rightChild,x)
 
    def find(self,x):
        """Returns the ndoe whose element is x. If it is not found, it returns None"""
        return self.findNode(self.root,x)
    
    def findNode(self,node,x):
        if node is None:
            return None
        
        if node.elem ==x:
            return node
        
        if x<node.elem:
            return self.findNode(node.leftChild,x)
        
        if x>node.elem:
            return self.findNode(node.rightChild,x)      
          
    def remove(self,x):
        """Searches and removes the node whose element is x"""
        if self.size() == 1:
            if self.root.elem == x:
                print('removing ', x)
                self.root = None
                return
        node=self.find(x)
        if node is None:
            print(x,' does not exist!!!')
            return
        print('removing ', x)
        self.removeNode(node)
        return x
    
    def fsize(self,node):
        """Returns the size balance factor for the input node"""
        if node is None:
            return 0
        return abs(self._size(node.leftChild)-self._size(node.rightChild))
    
    def balance(self):
        self._balance(self.root)
        
    def _balance(self, node):
       if  node == None:
           return
       if (self.sizeOf(node.leftChild) - self.sizeOf(node.rightChild)) > 1:
           nodeToBalance = self.fsize(node)//2
           while nodeToBalance > 0:
               rootNode = node.elem
               pred = self.predecessor(node)
               self.remove(pred.elem)               
               node.elem = pred.elem
               self.insert(rootNode)
               nodeToBalance -= 1
               
       elif (self.sizeOf(node.rightChild) - self.sizeOf(node.leftChild)) > 1:
           nodeToBalance = self.fsize(node)//2
           while nodeToBalance > 0:
               rootNode = node.elem
               suc = self.successor(node)
               self.remove(suc.elem)
               node.elem = suc.elem
               self.insert(rootNode)
               nodeToBalance -= 1
       self._balance(node.leftChild)
       self._balance(node.rightChild)
           
           
        
        
        
    def successor(self,node):
        """returns the successor node from its left subtree"""
        if node is None:
            return None
        
        if node.rightChild is None:
            print(node.elem, 'does not have any successor in its right child')
            return None
        
        successor=node.rightChild
        while successor.leftChild:
            successor=successor.leftChild
            
        return successor     
    
    
    def isSizeBalanced(self):
        """Checks if the tree is size-balanced"""
        return self._isSizeBalanced(self.root)
    
    def _isSizeBalanced(self,node):
        if node is None:
            return True
        
        if self.fsize(node)>1:
            return False
        
        return (self._isSizeBalanced(node.leftChild) and
                self._isSizeBalanced(node.rightChild))
    
    def predecessor(self,node):
        """returns the predecessor node from its left subtree"""
        if node is None:
            return None
        
        if node.leftChild is None:
            print(node.elem, 'does not have any predeccessor in its left child')
            return None
        
        predecessor=node.leftChild
        while predecessor.rightChild:
            predecessor=predecessor.rightChild
            
        return predecessor
        
    def mirror(self):
        self._mirror(self.root)
        
    def _mirror(self,node):
        if node != None:
            if node.leftChild and node.rightChild:
                node.leftChild,node.rightChild = node.rightChild, node.leftChild
            elif node.leftChild or node.rightChild:
                if node.leftChild:
                    node.rightChild = node.leftChild
                    node.leftChild = None
                if node.rightChild:
                    node.leftChild = node.rightChild
                    node.rightChild = None
            self._mirror(node.leftChild)
            self._mirror(node.rightChild)  
    def inorder1(self):
        print('\n-----------SHOWING ZONES AND DSMEMBERS------------')  
        self._inorder1(self.root)
        print()
    
    def _inorder1(self,currentNode):
        if currentNode!=None:
            self._inorder1(currentNode.leftChild)
            print('The Dsmembers in ',currentNode.elem.pc, ' are: ')
            currentNode.elem.inorder()
            self._inorder1(currentNode.rightChild)
     
    def getNonLeaves(self):
        lis = DList()
        self._getNonLeaves(self.root, lis)
        return lis
    
    def _getNonLeaves(self, node, lis):
        if node:
            self._getNonLeaves(node.rightChild, lis)
            if node.leftChild or node.rightChild:
                lis.addLast(node.elem)
            self._getNonLeaves(node.leftChild, lis)
        
    
        
        
    def removeNode(self,node):    
        """Auxiliary method to remove the node which takes as parameter"""
        #First case: no children
        if node.leftChild is None and node.rightChild is None:
            parent_node=node.parent
            if parent_node is not None:
                if parent_node.leftChild==node:
                    parent_node.leftChild=None
                else:
                    parent_node.rightChild=None
                node.parent=None
            else:
                self.root=None
            return
        
        #Second case: only one child
        if node.leftChild is not None and node.rightChild is None:
            
            parent_node=node.parent
            if parent_node is not None:
                if parent_node.leftChild==node:
                    parent_node.leftChild=node.leftChild
                else:
                    parent_node.rightChild=node.leftChild
                node.leftChild.parent=parent_node
            else:
                self.root=node.leftChild
            return
        
         #Second case: only one child
        if node.leftChild is None and node.rightChild is not None:
            
            parent_node=node.parent
            if parent_node is not None:
                if parent_node.leftChild==node:
                    parent_node.leftChild=node.rightChild
                else:
                    parent_node.rightChild=node.rightChild
                node.rightChild.parent=parent_node
            else:
                self.root=node.rightChild
            return
            
        #Third case: two children
        successor=node.rightChild
        while successor.leftChild is not None:
            successor=successor.leftChild
            
        #we replace the node's elem by the successor's elem
        node.elem=successor.elem
        #we remove the succesor from the tree
        self.removeNode(successor)
        
    

##### 
        




