#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:49:06 2020

@author: isegura
"""
import sys


class AdjacentVertex:
    """Note: Instead of using this class, you could use a tuple"""

    def __init__(self,vertex,weight):
        self.vertex=vertex
        self.weight=weight
  
    def __str__(self):
        return str(self.vertex)+','+str(self.weight)
    
class DeliveryPoint():
    def __init__(self,street,num=None,pc=None):
        self.street=street
        self.num=num
        self.pc=pc
        self.name = str(self.street)+', '+str(self.num)+', '+str(self.pc)
        
    def __eq__(self,other):
        if other==None:
            return False
        
        return (self.street==other.street and self.num==other.num
                and self.pc==other.pc)
    
    def __str__(self):
        result=str(self.street)
        if self.num!=None:
            result+=', '+str(self.num)
        if self.pc!=None:
            result+=', '+str(self.pc)
        return result


class Map():
    
    def __init__(self):
        '''self.point saves the list of vertices, and self.vertices svaes each
        point object using a name assigned to it'''
        self.points = {}
        self._vertices = {}
        # self._routeList = []
        
    def addDeliveryPoint(self,point):
        '''this methos adds a given point to the map'''
        # it assigns to the name a list
        self.points[point.name] = []
        
        # and also to the name the vertice related to it
        self._vertices[point.name] = point
        
        
    def addConnection(self,point1,point2,distance):
        '''a method that given two points and a distance,
        it creates an edge between both'''
        if point1.name not in self.points:
            print(point1,' does not exist!')
    
        if point2.name not in self.points:
            print(point2,' does not exist!')
            
        
        #adds to the end of the list of neigbours for start
        self.points[point1.name].append(AdjacentVertex(point2,distance))
        
        #adds to the end of the list of neigbours for end
        self.points[point2.name].append(AdjacentVertex(point1,distance))
       

        
    def areConnected(self,point1,point2):
        '''a method that , given two points, it checks if they are connected'''
        if point1.name not in self.points:
            print(point1,' does not exist!')
            return 
        if point2.name not in self.points:
            print(point2,' does not exist!')
            return 

        #we search the AdjacentVertex whose v is end
        for adj in self.points[point1.name]:
            if adj.vertex==point2:
                return adj.weight
        return 0  #does not exist
       
            
    def deleteConnection(self,point1,point2):
        ''' this method takes two points and delete the connection'''
        if point1.name not in self.points:
            print(point1,' does not exist!')
            return
        
        if point2.name not in self.points:
            print(point2.name,' does not exist!')
            return

        #we must look for the adjacent AdjacentVertex (neighbour)  whose 
        # vertex is end, and then remove it
        for adj in self.points[point1.name]:
            if adj.vertex==point2:
                self.points[point1.name].remove(adj)
        #we must also look for the AdjacentVertex (neighbour)  whose 
        # vertex is end, and then remove it
        for adj in self.points[point2.name]:
            if adj.vertex==point1:
                self.points[point2.name].remove(adj)
        

    def __str__(self):
       result=''
       for v in self.points:
            result+='\n'+str(v)+':'
            for adj in self.points[v]:
                result+=str(adj)

       return result
        

    def generateRoute(self): 
        '''This function prints all vertices of the graph using dfs'''
        self._routeList = []
        print('dfs traversal:')
        # Mark all the vertices as not visited 
        visited={}
        for v in self.points.keys():
            visited[v]=False

        for v in self.points.keys():
            if visited[v]==False:
                self._dfs(v,visited)
                
        return self._routeList

    # Function to print a BFS of graph 
    def _dfs(self, v, visited): 
    # This funcion prints the DFS traversal from the vertex whose index is indexV
    # Mark the current node as visited and print it 
        visited[v] = True
        #print(v, end = ' ') 
        #Instead of printing the index, we have to print its label
        
        self._routeList.append(self._vertices[v])
        # Recur for all the vertices  adjacent to this vertex 
        for adj in self.points[v]: 
            if visited[adj.vertex.name] == False: 
                self._dfs(adj.vertex.name, visited)
       
            
        
    
    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for vertex in self.points.keys(): 
            if distances[vertex] <= min and visited[vertex] == False: 
                min = distances[vertex] #update the new smallest
                min_vertex = vertex      #update the index of the smallest
    
        return min_vertex 



    def minRoute(self, origin,dest): 
        """"This function takes a vertex v and calculates its mininum path 
        to the rest of vertices by using the Dijkstra algoritm"""  
        
        #visisted is a dictionary whose keys are the verticies of our graph. 
        #When we visite a vertex, we must mark it as True. 
        #Initially, all vertices are defined as False (not visited)
        visited={}
        for v in self.points.keys():
            visited[v]=False

        #this dictionary will save the previous vertex for the key in the minimum path
        previous={}
        for v in self.points.keys():
            #initially, we defines the previous vertex for any vertex as None
            previous[v]=None


        #This distance will save the accumulate distance from the  
        #origin to the vertex (key)
        distances={}
        for v in self.points.keys():
            distances[v]=sys.maxsize


        #The distance from origin to itself is 0
        distances[origin.name] = 0
        
        for n in range(len(self.points)): 
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to origin in first iteration 
            u = self.minDistance(distances, visited) 

            visited[u] = True
            
            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            
            #we must visit all adjacent vertices (neighbours) for u
            for adj in self.points[u]: 
                i=adj.vertex
                w=adj.weight
                if visited[i.name]==False and distances[i.name]>distances[u]+w:
                    #we must update because its distance is greater than the new distance
                    distances[i.name]=distances[u]+w   
                    previous[i.name]=u       
                
        #finally, we print the minimum path from origin to the other vertices
        return self.Solution(distances,previous,origin,dest)
        

  

    def Solution(self,distances,previous,origin, dest): 
        '''returns the solution of the list and distance'''
        print("Mininum path from ",origin)
        for i in self.points.keys():
            if distances[i]==sys.maxsize:
                print("There is not path from ",origin,' to ',i)
            else: 
                #minimum_path is the list wich contains the minimum path from v to i
                
                minimum_path=[]
                prev=previous[i]
                #this loop helps us to build the path
                while prev!=None:
                    minimum_path.insert(0,self._vertices[prev])
                    prev=previous[prev]
                
                #we append the last vertex, which is i
                minimum_path.append(self._vertices[i])  
                if i == dest.name:
                    return minimum_path, distances[i]
                    
        
        

    
    
    
