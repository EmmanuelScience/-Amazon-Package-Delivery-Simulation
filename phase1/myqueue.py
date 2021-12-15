# -*- coding: utf-8 -*-
"""Implementation of a queue using a linked list
"""

class SNode:
  def __init__(self, e, next=None):
    self.elem = e
    self.next = next


class SQueue:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0
    
    
  def isEmpty(self):
    """Checks if the queue is empty"""
    return self.head == None   
    
  def __len__(self):
    return self.size


    
    
  def enqueue(self,e):
    """Adds a new elem, e, at the end of the queue"""
    newNode=SNode(e)
    
    if self.isEmpty():
      self.head=newNode
    else:
      self.tail.next= newNode
      
    self.tail=newNode
    self.size += 1
    
    
  def __str__(self):
    """Returns a string with the elems of the queue"""
    temp=self.head
    result=''
    while temp !=None:
      result+='\t\t'+str(temp.elem)+',\n'
      temp=temp.next
    result=result.strip()
    if len(result)>0:
      result=result[:-1]
    return result
    
  
    
  def dequeue(self):
    """Removes the first elem of the queue"""
    if self.isEmpty():
      print('Error: queue is empty!')
      return None
    
    #gets the first elem, which we will return later
    first=self.head.elem
    #updates head to point to the new head (the next node)
    self.head=self.head.next
    #if the list only has one node, tail must be None
    if self.isEmpty():
      self.tail=None
    self.size -= 1
    
    return first
    
  def top(self):
    """returns the first elem of the queue"""
    if self.isEmpty():
      print('Error: queue is empty!')
      return None

    return self.head.elem
  
