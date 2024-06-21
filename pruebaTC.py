import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Trazador cúbico natural de grado 3
def grado3():
    xi = np.array([2, 3, 5])
    yi = np.array([-1, 2, 7])
    n = len(xi)
    
    # Valores h
    h = np.zeros(n - 1, dtype=float)
    for j in range(0, n - 1):
        h[j] = xi[j + 1] - xi[j]
    
    # Sistema de ecuaciones
    A = np.zeros((n - 2, n - 2), dtype=float)
    B = np.zeros(n - 2, dtype=float)
    S = np.zeros(n, dtype=float)
    
    A[0, 0] = 2 * (h[0] + h[1])
    if n > 3:  # Para asegurarse de que no accedemos a índices fuera de rango
        A[0, 1] = h[1]
    B[0] = 6 * ((yi[2] - yi[1]) / h[1] - (yi[1] - yi[0]) / h[0])
    
    for i in range(1, n - 3):
        A[i, i - 1] = h[i]
        A[i, i] = 2 * (h[i] + h[i + 1])
        A[i, i + 1] = h[i + 1]
        B[i] = 6 * ((yi[i + 2] - yi[i + 1]) / h[i + 1] - (yi[i + 1] - yi[i]) / h[i])
    
    A[n - 3, n - 4] = h[n - 3]
    A[n - 3, n - 3] = 2 * (h[n - 3] + h[n - 2])
    B[n - 3] = 6 * ((yi[n - 1] - yi[n - 2]) / h[n - 2] - (yi[n - 2] - yi[n - 3]) / h[n - 3])
    
    # Resolver sistema de ecuaciones S
    r = np.linalg.solve(A, B)
    for j in range(1, n - 1):
        S[j] = r[j - 1]
    S[0] = 0
    S[n - 1] = 0
    
    # Coeficientes
    a = np.zeros(n - 1, dtype=float)
    b = np.zeros(n - 1, dtype=float)
    c = np.zeros(n - 1, dtype=float)
    d = np.zeros(n - 1, dtype=float)
    for j in range(0, n - 1):
        a[j] = (S[j + 1] - S[j]) / (6 * h[j])
        b[j] = S[j] / 2
        c[j] = (yi[j + 1] - yi[j]) / h[j] - (2 * h[j] * S[j] + h[j] * S[j + 1]) / 6
        d[j] = yi[j]
    
    # Polinomio trazador
    x = sym.Symbol('x')
    px_tabla = []
    for j in range(0, n - 1):
        pxtramo = a[j] * (x - xi[j]) ** 3 + b[j] * (x - xi[j]) ** 2 + c[j] * (x - xi[j]) + d[j]
        pxtramo = pxtramo.expand()
        px_tabla.append(pxtramo)
    
    # SALIDA
    print('Polinomios por tramos:')
    for tramo in range(1, n):
        print(f' x = [{xi[tramo - 1]}, {xi[tramo]}]')
        print(str(px_tabla[tramo - 1]))

# Trazador cúbico de grado 2
def grado2():
    xi = np.array([6, 7, 8, 10, 12])
    yi = np.array([3, 4, 7, 9, 15])
    n = len(xi)
    num_vars = 3 * (n - 1) - 1
    
    A = np.zeros((num_vars, num_vars))
    B = np.zeros(num_vars)
    
    idx = 0
    
    # Ecuaciones de paso por los puntos
    for i in range(n - 1):
        x0 = xi[i]
        x1 = xi[i + 1]
        
        A[idx, 3 * i:3 * i + 2] = [x0**2, x0]
        B[idx] = yi[i]
        if i > 0:
            A[idx, 3 * i - 1] = 1
        
        idx += 1
        
        A[idx, 3 * i:3 * i + 2] = [x1**2, x1]
        B[idx] = yi[i + 1]
        if i > 0:
            A[idx, 3 * i - 1] = 1
        
        idx += 1
    
    for i in range(1, n - 1):
        x0 = xi[i]
        
        A[idx, 3 * (i - 1):3 * (i - 1) + 2] = [2 * x0, 1]
        A[idx, 3 * i:3 * i + 2] = [-2 * x0, -1]
        
        idx += 1
    
    coeffs = np.linalg.solve(A, B)
    
    a = np.zeros(n - 1)
    b = np.zeros(n - 1)
    c = np.zeros(n - 1)
    
    for i in range(n - 1):
        a[i] = coeffs[3 * i]
        b[i] = coeffs[3 * i + 1]
        if i > 0:
            c[i] = coeffs[3 * i - 1]
    
    c[0] = 0
    
    x = sym.Symbol('x')
    px_tabla = []
    for i in range(n - 1):
        pxtramo = a[i] * (x - xi[i]) ** 2 + b[i] * (x - xi[i]) + c[i]
        pxtramo = pxtramo.expand()
        px_tabla.append(pxtramo)
    
    # SALIDA
    print('Polinomios por tramos:')
    for tramo in range(1, len(xi)):
        print(f' x = [{xi[tramo - 1]}, {xi[tramo]}]')
        print(str(px_tabla[tramo - 1]))

# Trazador cúbico de grado 1
def grado1():
    xi = np.array([6, 7, 8, 10, 12])
    yi = np.array([3, 4, 7, 9, 15])
    n = len(xi)
    
    a = np.zeros(n - 1, dtype=float)
    b = np.zeros(n - 1, dtype=float)
    
    for j in range(n - 1):
        a[j] = (yi[j + 1] - yi[j]) / (xi[j + 1] - xi[j])
        b[j] = yi[j] - a[j] * xi[j]
    
    x = sym.Symbol('x')
    px_tabla = []
    for j in range(n - 1):
        pxtramo = a[j] * x + b[j]
        pxtramo = pxtramo.expand()
        px_tabla.append(pxtramo)
    
    # SALIDA
    print('Polinomios por tramos:')
    for tramo in range(1, n):
        print(f' x = [{xi[tramo - 1]}, {xi[tramo]}]')
        print(str(px_tabla[tramo - 1]))

# PROCEDIMIENTO
print("GRADO 3 ------------")
grado3()
print("\nGRADO 2 ------------")
grado2()
print("\nGRADO 1 ------------")
grado1()
