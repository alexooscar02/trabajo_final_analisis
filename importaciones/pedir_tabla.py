import numpy as np

def pedir_tabla():
    x_valores = input("Ingrese los valores de 'x' separados por comas: ")
    y_valores = input("Ingrese los valores de 'y' separados por comas: ")
    x_valores = np.array([float(x.strip()) for x in x_valores.split(",")])
    y_valores = np.array([float(y.strip()) for y in y_valores.split(",")])
    return x_valores, y_valores

