# -*- coding: utf-8 -*-
"""Ejercicio_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16qRRq5vWYW1XDaFDr8yPHpUHkLdK9-P1
"""

import numpy as np
import random
import math

arreglo_1 = np.array([0]*10)

for i in range(10):
  arreglo_1[i] = random.randint(0,1000)

print("1.- El arreglo es: ", arreglo_1, "\n")

num_pares = 0
for elemento in arreglo_1:
    if elemento % 2 == 0:
        num_pares += 1
print("2.- La cuenta de los elementos pares son: ", num_pares, "\n")

suma_impares = 0
for elemento in arreglo_1:
    if elemento % 2 == 1:
        suma_impares += elemento
print("3.- La suma de los elemento impares es: ", suma_impares, "\n")

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for elemento in arreglo_1:
    if es_primo(elemento):
        print("4.- El elemento", elemento, "es primo.")