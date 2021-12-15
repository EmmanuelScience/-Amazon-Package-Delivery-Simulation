#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:06:33 2020

@author: isegura
"""
from phase1 import AmazonManagement

amz=AmazonManagement()
dataPac=[
      
      ['132-1352234-332348','C/Coronavirus',3,28911],
      ['132-1352234-332349','C/Paz',4,28911],
      ['132-1352234-332350','C/Metro',3,28912],
      ['132-1352234-332351','C/Mar',4,28912],
      ['132-1352234-332352','C/Salvador',1,28913],
      ['132-1352234-332353','C/Brasil',5,28913],
      ['132-1352234-332354','C/Salvador',1,28913],
      ['132-1352234-332355','C/Brasil',5,28913],
      ['132-1352234-332344','C/Canovas del Castillo',53,28914],
      ['132-1352234-332347','C/Madrid',5,28914],
      ['132-1352234-332345','C/Mayor',10,28915],
      ['132-1352234-332346','C/Real',15,28915],
      ['132-1352234-000001','C/Pez',10,28916],
      ['132-1352234-000002','C/Paris',15,28917],
      ['132-1352234-000003','C/Sevilla',33,28918],
      ['132-1352234-000004','C/Jaen',15,28918]  
]
amz.loadOrders(dataPac)
print('Orders:\t',str(amz.orders))
print('\n')


dataDSM=[
  ['R1000001','Segura Bedmar, Isabel','Activo',[28911,28912]],
  ['R1000002','Iglesias, Julio','Activo',[28911]],
  ['R1000003','Vargas, Chavela','Activo',[28912]],
  ['R1000004','Bose, Miguel','Activo',[28913,28914]],
  ['R1000005','Barrio, Paquita','Activo',[28914]],
  ['R1000006','Escudero, Juan','Activo',[28915]],
  ['R1000007','Ruíz, Juan','Activo',[28915,28916]],
  ['R1000008','Segura, David','Activo',[28917]],
  ['R1000009','Sampedro, Monica','Activo',[28918]],
  ['R1000010','Molina, Clara','Activo',[28914,28916]],
  ['R1000011','Molina, Miguel','Activo',[28917,28918]]
]
amz.loadDSMembers(dataDSM)
print('Delivery staff members before package assignation:')
amz.showDSMembers()
print('\n')

amz.assignDistribution()
print('Delivery staff members after package assignation:')
amz.showDSMembers()
print('\n')
# #
amz.removeDSMember('R1000011')
print('\n')

print('Show delivery staff members after removing R1000011')

amz.showDSMembers()
print('\n')

amz.deliver()
print('\n')
amz.showDSMembers()


print("\n Successfully delivered:",str(amz.delivered))
print("Incidences",str(amz.incidents))

"""The output of the program should be:
    
    Orders:         132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0,
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0,
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0,
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0,
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0,
                132-1352234-000001 C/Pez 10 28916 0,
                132-1352234-000002 C/Paris 15 28917 0,
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0


Delivery staff members before package assignation:
DSMember: R1000005, Barrio, Paquita, Activo, Zonas: 28914,

DSMember: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914,

DSMember: R1000006, Escudero, Juan, Activo, Zonas: 28915,

DSMember: R1000002, Iglesias, Julio, Activo, Zonas: 28911,

DSMember: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916,

DSMember: R1000011, Molina, Miguel, Activo, Zonas: 28917, 28918,

DSMember: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

DSMember: R1000009, Sampedro, Monica, Activo, Zonas: 28918,

DSMember: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912,

DSMember: R1000008, Segura, David, Activo, Zonas: 28917,

DSMember: R1000003, Vargas, Chavela, Activo, Zonas: 28912



RDelivery staff members after package assignation:
DSMember: R1000005, Barrio, Paquita, Activo, Zonas: 28914
        Packages:
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0,

DSMember: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914
        Packages:
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0,

DSMember: R1000006, Escudero, Juan, Activo, Zonas: 28915
        Packages:
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0,

DSMember: R1000002, Iglesias, Julio, Activo, Zonas: 28911
        Packages:
                132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0,

DSMember: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916
        Packages:
                132-1352234-000001 C/Pez 10 28916 0,

DSMember: R1000011, Molina, Miguel, Activo, Zonas: 28917, 28918
        Packages:
                132-1352234-000002 C/Paris 15 28917 0,
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0,

DSMember: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

DSMember: R1000009, Sampedro, Monica, Activo, Zonas: 28918,

DSMember: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912
        Packages:
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0,

DSMember: R1000008, Segura, David, Activo, Zonas: 28917,

DSMember: R1000003, Vargas, Chavela, Activo, Zonas: 28912



Removing DSMember: R1000011
reassigning package  132-1352234-000002  to: R1000008
reassigning package 132-1352234-000003  to: R1000009
reassigning package  132-1352234-000004  to: R1000009


Show delivery staff members after removing R1000011 
DSMember: R1000005, Barrio, Paquita, Activo, Zonas: 28914
        Packages:
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0,

DSMember: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914
        Packages:
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0,

DSMember: R1000006, Escudero, Juan, Activo, Zonas: 28915
        Packages:
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0,

DSMember: R1000002, Iglesias, Julio, Activo, Zonas: 28911
        Packages:
                132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0,

DSMember: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916
        Packages:
                132-1352234-000001 C/Pez 10 28916 0,

DSMember: R1000011, Molina, Miguel, No activo, Zonas: 28917, 28918,

DSMember: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

DSMember: R1000009, Sampedro, Monica, Activo, Zonas: 28918
        Packages:
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0,

DSMember: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912
        Packages:
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0,

DSMember: R1000008, Segura, David, Activo, Zonas: 28917
        Packages:
                132-1352234-000002 C/Paris 15 28917 0,

DSMember: R1000003, Vargas, Chavela, Activo, Zonas: 28912


#This section can change because delivering a given package is a random process

processing delivery for: 
DSMember: R1000005, Barrio, Paquita, Activo, Zonas: 28914
        Packages:
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0


Package to deliver ... 132-1352234-332344 C/Canovas del Castillo 53 28914 0
Could not be delivered: 132-1352234-332344  DSMmber por: R1000005  attempts: 1
Package to deliver ... 132-1352234-332347 C/Madrid 5 28914 0
Could not be delivered: 132-1352234-332347  DSMmber por: R1000005  attempts: 1
Package to deliver ... 132-1352234-332344 C/Canovas del Castillo 53 28914 1
Delivered: 132-1352234-332344  delivered by; R1000005  at attempt: 1
Package to deliver ... 132-1352234-332347 C/Madrid 5 28914 1
Could not be delivered: 132-1352234-332347  DSMmber por: R1000005  attempts: 2
Package to deliver ... 132-1352234-332347 C/Madrid 5 28914 2
Incidencia del paquete: 132-1352234-332347  DSMmber por: R1000005  attempts: 3

Processing delivery for: 
DSMmber: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914
        Packages:
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0


Package to deliver ... 132-1352234-332352 C/Salvador 1 28913 0
Could not be delivered: 132-1352234-332352  DSMmber por: R1000004  attempts: 1
Package to deliver ... 132-1352234-332353 C/Brasil 5 28913 0
Delivered: 132-1352234-332353  delivered by; R1000004  at attempt: 0
Package to deliver ... 132-1352234-332354 C/Salvador 1 28913 0
Delivered: 132-1352234-332354  delivered by; R1000004  at attempt: 0
Package to deliver ... 132-1352234-332355 C/Brasil 5 28913 0
Could not be delivered: 132-1352234-332355  DSMmber por: R1000004  attempts: 1
Package to deliver ... 132-1352234-332352 C/Salvador 1 28913 1
Delivered: 132-1352234-332352  delivered by; R1000004  at attempt: 1
Package to deliver ... 132-1352234-332355 C/Brasil 5 28913 1
Delivered: 132-1352234-332355  delivered by; R1000004  at attempt: 1

Processing delivery for: 
DSMmber: R1000006, Escudero, Juan, Activo, Zonas: 28915
        Packages:
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0


Package to deliver ... 132-1352234-332345 C/Mayor 10 28915 0
Delivered: 132-1352234-332345  delivered by; R1000006  at attempt: 0
Package to deliver ... 132-1352234-332346 C/Real 15 28915 0
Could not be delivered: 132-1352234-332346  DSMmber por: R1000006  attempts: 1
Package to deliver ... 132-1352234-332346 C/Real 15 28915 1
Could not be delivered: 132-1352234-332346  DSMmber por: R1000006  attempts: 2
Package to deliver ... 132-1352234-332346 C/Real 15 28915 2
Incidencia del paquete: 132-1352234-332346  DSMmber por: R1000006  attempts: 3

Processing delivery for: 
DSMmber: R1000002, Iglesias, Julio, Activo, Zonas: 28911
        Packages:
                132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0


Package to deliver ... 132-1352234-332348 C/Coronavirus 3 28911 0
Delivered: 132-1352234-332348  delivered by; R1000002  at attempt: 0
Package to deliver ... 132-1352234-332349 C/Paz 4 28911 0
Delivered: 132-1352234-332349  delivered by; R1000002  at attempt: 0

Processing delivery for: 
DSMmber: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916
        Packages:
                132-1352234-000001 C/Pez 10 28916 0


Package to deliver ... 132-1352234-000001 C/Pez 10 28916 0
Could not be delivered: 132-1352234-000001  DSMmber por: R1000010  attempts: 1
Package to deliver ... 132-1352234-000001 C/Pez 10 28916 1
Could not be delivered: 132-1352234-000001  DSMmber por: R1000010  attempts: 2
Package to deliver ... 132-1352234-000001 C/Pez 10 28916 2
Incidencia del paquete: 132-1352234-000001  DSMmber por: R1000010  attempts: 3
R1000011 is not active

.
R1000007 does not have packages to deliver.



Processing delivery for: 
DSMmber: R1000009, Sampedro, Monica, Activo, Zonas: 28918
        Packages:
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0


Package to deliver ... 132-1352234-000003 C/Sevilla 33 28918 0
Could not be delivered: 132-1352234-000003  DSMmber por: R1000009  attempts: 1
Package to deliver ... 132-1352234-000004 C/Jaen 15 28918 0
Delivered: 132-1352234-000004  delivered by; R1000009  at attempt: 0
Package to deliver ... 132-1352234-000003 C/Sevilla 33 28918 1
Could not be delivered: 132-1352234-000003  DSMmber por: R1000009  attempts: 2
Package to deliver ... 132-1352234-000003 C/Sevilla 33 28918 2
Delivered: 132-1352234-000003  delivered by; R1000009  at attempt: 2

Processing delivery for: 
DSMmber: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912
        Packages:
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0


Package to deliver ... 132-1352234-332350 C/Metro 3 28912 0
Could not be delivered: 132-1352234-332350  DSMmber por: R1000001  attempts: 1
Package to deliver ... 132-1352234-332351 C/Mar 4 28912 0
Could not be delivered: 132-1352234-332351  DSMmber por: R1000001  attempts: 1
Package to deliver ... 132-1352234-332350 C/Metro 3 28912 1
Delivered: 132-1352234-332350  delivered by; R1000001  at attempt: 1
Package to deliver ... 132-1352234-332351 C/Mar 4 28912 1
Could not be delivered: 132-1352234-332351  DSMmber por: R1000001  attempts: 2
Package to deliver ... 132-1352234-332351 C/Mar 4 28912 2
Delivered: 132-1352234-332351  delivered by; R1000001  at attempt: 2

Processing delivery for: 
DSMmber: R1000008, Segura, David, Activo, Zonas: 28917
        Packages:
                132-1352234-000002 C/Paris 15 28917 0


Package to deliver ... 132-1352234-000002 C/Paris 15 28917 0
Delivered: 132-1352234-000002  delivered by; R1000008  at attempt: 0
R1000003 does not have packages to deliver.


DSMmber: R1000005, Barrio, Paquita, Activo, Zonas: 28914,

DSMmber: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914,

DSMmber: R1000006, Escudero, Juan, Activo, Zonas: 28915,

DSMmber: R1000002, Iglesias, Julio, Activo, Zonas: 28911,

DSMmber: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916,

DSMmber: R1000011, Molina, Miguel, No activo, Zonas: 28917, 28918,

DSMmber: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

DSMmber: R1000009, Sampedro, Monica, Activo, Zonas: 28918,

DSMmber: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912,

DSMmber: R1000008, Segura, David, Activo, Zonas: 28917,

DSMmber: R1000003, Vargas, Chavela, Activo, Zonas: 28912



Successfully delivered: R1000005 132-1352234-332344,
                R1000004 132-1352234-332353,
                R1000004 132-1352234-332354,
                R1000004 132-1352234-332352,
                R1000004 132-1352234-332355,
                R1000006 132-1352234-332345,
                R1000002 132-1352234-332348,
                R1000002 132-1352234-332349,
                R1000009 132-1352234-000004,
                R1000009 132-1352234-000003,
                R1000001 132-1352234-332350,
                R1000001 132-1352234-332351,
                R1000008 132-1352234-000002
Incidences 132-1352234-332347 R1000005 number of attempts exceeded,
                132-1352234-332346 R1000006 number of attempts exceeded,
                132-1352234-000001 R1000010 number of attempts exceeded
    
    """

