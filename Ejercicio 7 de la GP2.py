# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:16:45 2022

@author: alumno
"""

# Ejercicio 7

def Suma_digitos():
    '''
    Al ingresar un nùmero entero positivo, 


    Returns
    -------
    int
        nùmero entero positivo

    '''
    n = int(input())
    k = 10
    
    if n == 0:
        return 0
    
    return Suma_digitos(n//k) + (n % k)