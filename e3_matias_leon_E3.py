# -*- coding: utf-8 -*-
"""Ejercicio_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VHaNotW0mgVyhyrH54x07lVtZNl8pkki
"""

import numpy as np
import random

A = np.array([0]*10)

for i in range(10):
  A[i] = random.randint(0,300)

B = np.array([0]*10)

for i in range(10):
  B[i] = random.randint(0,300)

print("2.- La suma de los elementos de A es:", sum(A), "y de B es:", sum(B), "\n")

print("3.- La suma de los elementos de A y B es:", (sum(A) + sum(B)), "\n")

impares_B = [elemento for elemento in B if elemento % 2 == 1]
for elemento in impares_B:
    print("\n4.- La tabla de multiplicar de", elemento, "es:\n")
    for i in range(1, 11):
        print(elemento, "x", i, "=", elemento * i)