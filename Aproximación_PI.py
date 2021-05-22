# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:45:29 2021

@author: ASUS
"""
import numpy as np
import random
#APROXIMACIónN PI

#Método simulación Montecarlo:

dardos = 100000

puntos_circulo = 0
puntos_cuadrado = 0

for i in range(dardos):
    coordenada_x = random.uniform(-1,1)
    coordenada_y = random.uniform(-1,1)
    
    dist_origen = coordenada_x**2 + coordenada_y**2
    
    if dist_origen <= 1:
        puntos_circulo +=1
    
    puntos_cuadrado += 1
    pi = 4*puntos_circulo/puntos_cuadrado

print("Pi estimado: " , pi)

#Serie de Leibniz
pil = 0
for i in range(0,1000):
    n=((-1)**i)*(1/((2*i)+1))
    pil += n
    print(4*pil)

#Aproximación de Wallis 
piw = 1
for i in range(1,10000):
    n=(4*i**2)
    d=(1/((4)*((i)**2)-1))
    p= n*d
    piw *= p
    print(2*piw)

#Aproximación Euler
pie = 0
for i in range(1,10000):
    n1=(2**i)
    n2=((np.math.factorial(i))**2)
    d= np.math.factorial((2*i+1))
    p= (n1*n2)/d
    pie += p
    print(2*(pie+1))