# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:52:40 2022

@author: alumno
"""

import random
import time
import matplotlib



valores_de_n = 10 ** i
tiempos = []

def buscar_item(lista, item):
    encontrado = False
    i = 0
    while i < len(lista) and not encontrado:
        if item == lista(i):
            encontrado = True
        i += 1
    return encontrado

def busqueda_binaria(lista, item):
    encontrado = False
    primero = 0
    ultimo = len(lista) -1
    while primero <= ultimo and not encontrado:
        punto_medio =(primero + ultimo)//2
        
        if lista (punto_medio) == item:
            encontrado = True
        elif lista(punto_medio) > item:
            ultimo = punto_medio - 1
        else:
            primero = punto_medio+ 1
    
    return encontrado


    

        