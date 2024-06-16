import numpy as np
import re

def pedir_tabla():
    x_valores = input("Ingrese los valores de 'x' separados por comas: ")
    y_valores = input("Ingrese los valores de 'y' separados por comas: ")
    x_valores = np.array([float(x.strip()) for x in x_valores.split(",")])
    y_valores = np.array([float(y.strip()) for y in y_valores.split(",")])
    return x_valores, y_valores


def trazador_cubico_grado1(x, y):
    n = len(x)
    a = y[0]
    h = np.diff(x)
    b = np.diff(y) / h
    
    trazadores = []
    for i in range(n - 1):
        trazador = "{:.2f} + {:.2f}(x - {:.2f})".format(a, b[i], x[i])
        trazadores.append(trazador)
        a = y[i] + b[i] * (x[i+1] - x[i]) 
        
    return trazadores

def trazador_cubico_grado2(x, y):
    n = len(x)
    h = np.diff(x)
    alfa = np.zeros(n)
    for i in range(1, n-1):
        alfa[i] = 3 * ((y[i+1] - y[i])/h[i]) - 3 * ((y[i] - y[i-1])/h[i-1])
    l = np.zeros(n)
    miu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    miu[0] = 0
    z[0] = 0
    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * miu[i-1]
        miu[i] = h[i] / l[i]
        z[i] = (alfa[i] - h[i-1] * z[i-1]) / l[i]
    l[n-1] = 1
    z[n-1] = 0
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)
    c[n-1] = 0
    for j in range(n-2, -1, -1):
        c[j] = z[j] - miu[j] * c[j+1]
        b[j] = ((y[j+1] - y[j])/h[j]) - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
        
    trazadores = []
    for i in range(n - 1):
        trazador = "{:.2f}x^2 + {:.2f}x + {:.2f}".format(y[i], b[i], c[i])
        trazadores.append(trazador)
        
    return trazadores

def trazador_cubico_grado3(x, y):
    n = len(x)
    h = np.diff(x)
    alfa = np.zeros(n)
    for i in range(1, n-1):
        alfa[i] = 3 * ((y[i+1] - y[i])/h[i]) - 3 * ((y[i] - y[i-1])/h[i-1])
    l = np.zeros(n)
    miu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    miu[0] = 0
    z[0] = 0
    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * miu[i-1]
        miu[i] = h[i] / l[i]
        z[i] = (alfa[i] - h[i-1] * z[i-1]) / l[i]
    l[n-1] = 1
    z[n-1] = 0
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)
    c[n-1] = 0
    for j in range(n-2, -1, -1):
        c[j] = z[j] - miu[j] * c[j+1]
        b[j] = ((y[j+1] - y[j])/h[j]) - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
        
    trazadores = []
    for i in range(n - 1):
        trazador = "{:.2f}x^3 + {:.2f}x^2 + {:.2f}x + {:.2f}".format(y[i], b[i], c[i], d[i])
        trazadores.append(trazador)
        
    return trazadores

print("-"*70)
print("                     Trazadores Cubicos")
print("-"*70)
# Entrada de datos
x,y=pedir_tabla()
# Validación de entrada
if len(x) != len(y):
    print("Error: Las listas X y Y deben tener la misma longitud.")
else:
    # Selección del grado del trazador
    opcion = input("¿Qué trazador cúbico desea implementar? (grado1, grado2, grado3): ")

    # Salida
    if opcion == "grado1":
        trazadores = trazador_cubico_grado1(x, y)
    elif opcion == "grado2":
        trazadores = trazador_cubico_grado2(x, y)
    elif opcion == "grado3":
        trazadores = trazador_cubico_grado3(x, y)
    else:
        print("Opción no válida")

    print("-"*70)
    # Impresión de resultados
    for i, trazador in enumerate(trazadores):
        print("Trazador para el intervalo [", x[i], ",", x[i+1], "]:", trazador)
