#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:06:33 2020

@author: emma
"""


from dsmembers import DSMembers
from dsmembers import DSMember

from orders import Orders
from orders import Package
from orders import Incidents
from orders import Incident
from orders import Delivered
from orders import Deliveredpackage



import random 


class AmazonManagement:
    """Main class including functionality for phase 1"""
    
    def __init__(self):
        self.orders=Orders()
        self.dsmembers=DSMembers()
        self.delivered=Delivered()
        self.incidents = Incidents()


    def loadOrders(self,data):
        """ This method receives the data needed to initialize the object 
        storing the orders that Amazon must deliver  
        """
        for t in data:
            idpac=t[0]
            street=t[1]
            num=t[2]
            pc=t[3]
            package=Package(idpac,street,num,pc)
            self.orders.enqueue(package)
            #include the instructions needed to add the package to the orders 
            #object

    def loadDSMembers(self,data):
        """ This method receives data to initialice the object storing the 
        delivery staff members at Amazon, it inserts the dsmembers in the 
        dsmembers object in an orderly fashion"""
        for t in data:
            iddsm=t[0]
            name=t[1]
            status=t[2]
            zones=t[3]
           #  Adding the dsmembers to the dsmemberslist by arranging them
           # alphabetically
            dsmember=DSMember(iddsm,name,status,zones)
            # if the lis is empty we just add the elemnt to the top of the list
            if self.dsmembers.isEmpty():
                self.dsmembers.addLast(dsmember)
            
            # if the name is greater than the tail of the list, we addLast
            elif (dsmember.name.lower() >= self.dsmembers.tail.elem.name.lower()):
                self.dsmembers.addLast(dsmember)
            # if it's smaller than the head we addfirst
            elif dsmember.name.lower() <= self.dsmembers.head.elem.name.lower():
                self.dsmembers.addFirst(dsmember)
            
            else:
                # if it's not smaller than the head nor bigger than the tail
                # we go through the list, find its adequate position and 
                # insert it
                current = self.dsmembers.head
                counter = 0
                while current and dsmember.name.lower() > current.elem.name.lower():
                    counter += 1
                    current =current.next
                self.dsmembers.insertAt(counter, dsmember)
                
              
             
           
    
    def showDSMembers(self):
        '''shows all the dsmembers alphabetically'''
        # it just iterates through the list as it's already sorted
        current = self.dsmembers.head
        while current:
            print (current.elem, '\n')
            current  = current.next
            
    
    def  min_zone(self):
        '''returns the minimum zone'''
        '''it runs through the dsmebers object and returns the one with least 
        amount of assigned zones'''
        
        # First we set the first dsmemmebr as the one with minimum zone
        min_zone = self.dsmembers.head
        current = min_zone
        
        # then we loop through the dsmember to find the dsmmeber with
        # minimum amount of zones and that is active
        while current:
            if current.elem.zones.size < min_zone.elem.zones.size:
                if current.elem.status == 'Activo':
                    min_zone = current
            current = current.next
        
        # When we find the zone we return it
        return min_zone.elem
                  
    
    def  assign(self, data):
        '''This elements goes through the queue of orders and dsmembers, 
        and assign the orders to the adequate dsmember'''
        # setting  a counter to 0 at first to loop the dsmember list
        counter = 0
        
        # An intitial condition used to know if there exist an active dsmember
        # in the same zone as the package
        con = False
        
        # Firstly, we go through the entire dsmember list
        while not con and counter < self.dsmembers.size:
            
            # giving the current dsmember a name in order to be coherent
            dsm = self.dsmembers.getAt(counter)
            top = self.orders.top()
            
            # We check if the current dsmember is active  and is assigned to 
            # the same zone as the package.
            if dsm.zones.contains(top.pc) and dsm.status == 'Activo':
                
                # if the assignation comes from a removed dsmember, we print
                # a different message in the console
                if data == 'return':
                    print('reassigning packege ', top.idpac, 'to: ', dsm.iddsm)
                
                # in the case in which the conditions are met, we assign the
                # package to the dsmember and set the condition to true
                dsm.orders.enqueue(top)
                con = True
            counter += 1
                
                
        if con == True:    
            return True
        else:
            return False
        
    def assignDistribution(self):
        """
        assigns each order (package) to a distributor. Remember that the 
        distributor must be active and must cover the area of the package.
        If there is no active distributor for that zone, the package (and its 
        zone) will be assigned to the active distributor with fewer zones.
         """
        
        for elem in range(self.orders.size):   
            # assign to top of the queue to variable for readability
            
            
            # if there's no active distributor it assigns the order to the
            # dsmember with minimum zone
            if  not self.assign('norm'):
                top = self.orders.top()
                self.min_zone().orders.enqueue(top)
            
            # In any case after the order is assigned we have to dequeue it
            self.orders.dequeue()
          
                
    
    def deliverPackages(self,dsm):
        ''', this method simulates the delivery of the
        packages for a specific distributor. The function receives a distributor
        (identifier) and must process all its packages, always starting with the
        first package and processing them in strict order. For each package to be
        delivered, a random value (True or False) is generated to indicate 
        whether the package has been correctly delivered or not. If the value
        generated is True,the package must be removed from the set of packages 
        assigned to that distributor, and registered as delivered. If, on the 
        contrary, the value generated is False, which means that the package
        could not be delivered,the package will be placed at the end of the 
        orders to be delivered by the distributor. If the distributor has
        tried to deliver a package 3 times without success, the package will 
        be removed from the distribution order and recorded as an incident. 
        The function must always show for each processed package the package 
        id and a message informing of it status: correctly delivered, 
        pending (with the number of attempts made) or removed. The process
        continues while the distributor still has packages to deliver'''
        
        # A condition is set to true initially to find the dsmember
        con = True
                
        current = self.dsmembers.head
        
        # we loop the dsmember list until we find the dsm we want
        while current.next and con:
            if current.elem.iddsm == dsm:
                # when we find the dsm we set the con to false to end the loop
                con = False
            current = current.next
            
        # if the dsm is not found we return
        if current == None:
            print(dsm, ' not found')
            return
        
         # so now we make current an element instead of a node
        current = current.prev.elem
        print('\n processing delivery for: ')        
        print(current, '\n')
        
       
        
        
        
        # if the dsm has no orders, we give a message of no orders and return
        if current.orders.isEmpty():
            print(dsm, ' does not have package to deliver.')
            return
         
        #we have to loop through the entire queue of orders, unil it's empty
        while not current.orders.isEmpty():
            
           # when the attempts is less than 3 we have to enter ths condition
           if current.orders.top().numAttempts < 3:
               print('Package to deliver ...', current.orders.top())
               
               # We then generate a random number in order to process the 
               # delivery
               if random.randrange(2) == 0:
                   print('Delivered: ', current.orders.top().idpac,
                         'delivered by: ', dsm, 'at attempt: ',
                         current.orders.top().numAttempts )
                   
                   
                   idpac = current.orders.top().idpac
                   self.deliveredpackage = Deliveredpackage(idpac, dsm)
                   
                   # if the two above conditions are met we add the package
                   # to de queue of delivered packages
                   self.delivered.enqueue(self.deliveredpackage)
                   
                   # then we remove the package from the queue of orders
                   current.orders.dequeue()
                   
               else:
                   #if the attempt is less than 3, and it couldn't be delivered
                   # We remove it from the top and add enqueu it
                   current.orders.top().numAttempts += 1
                   print('Could not be delivered: ',current.orders.top().idpac,
                         'dsmember : ', dsm, 'at attempt: ',
                         current.orders.top().numAttempts )
                   temp = current.orders.dequeue()
                   current.orders.enqueue(temp)
                   
                   
                   
           else:
               # if the number of attempts is greater than 3, we add the 
               # package to the queue of incidents
              print('Incidence: ', current.orders.top().idpac,
                         'dsmember: ', dsm, 'at attempt',
                         current.orders.top().numAttempts)
              idpac =  current.orders.top().idpac
              reason = 'Number of attempt exceeded'
              incident = Incident(idpac, dsm, reason)
              self.incidents.enqueue(incident)
              current.orders.dequeue()
                  
                   
                
    def deliver(self):
        """that simulates the delivery of packages from all distributors."""
        current = self.dsmembers.head
        while current:
            self.deliverPackages(current.elem.iddsm)
            current = current.next
                   
                
    def removeDSMember(self,idrep):
        """receives a distributor (identifier) and sets it as inactive. If the 
        distributor has a pending package to be delivered, it must be 
        reassigned to an active distributor that covers the area of the 
        package. If no available distributor is found, the package will be 
        registered as an incident."""
        
        # first we go through the dsmember list, find the dsmember by it's id,.
        # set it to inactive, then set its orders to the general orders, after 
        # which it will be reasigned
        current = self.dsmembers.head
        con = False
        while not con and current:
            if current.elem.iddsm == idrep:
                print('Removing Dsmember: ', idrep )
                current.elem.status = 'Inactive'
                self.orders = current.elem.orders
                con = True
            current = current.next
        
        for elem in range(self.orders.size):               
            if  not self.assign('return'):
                idpac = self.orders.top().idpac
                iddsm =  idrep
                reason = 'No available dsmember'
                incident = Incident(idpac, iddsm, reason)
                self.incidents.enqueue(incident)
            self.orders.dequeue()
        
        
        
 
