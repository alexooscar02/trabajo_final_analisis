import numpy as np
from sympy import sympify

def pedir_tabla_her():
    valores_x = input("Ingrese los valores de 'x' separados por comas: ")
    valores_y = input("Ingrese los valores de 'y' separados por comas: ")
    
    valores_x = np.array([float(x.strip()) for x in valores_x.split(",")])
    valores_y = np.array([sympify(y.strip()) for y in valores_y.split(",")])
    
    return valores_x, valores_y
