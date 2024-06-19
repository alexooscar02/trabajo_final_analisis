import math
import re
from sympy import symbols, sympify, lambdify
from pedir_funcion import pedir_funcion
from tabulate import tabulate

# Función para calcular la integral usando el método del trapecio compuesto para una dimensión
def trapecio_compuesto_simple(f, a, b, n):
    h = (b - a) / n
    suma = 0
    
    for k in range(1, n):
        x_k = a + k * h
        suma += f(x_k)
    
    integral = (b - a) * ((f(a) + 2 * suma + f(b)) / (2 * n))
    return integral

# Función para calcular la integral usando el método del trapecio compuesto para dos dimensiones
def trapecio_compuesto_doble(f, a1, b1, a2, b2, n):
    h1 = (b1 - a1) / n
    h2 = (b2 - a2) / n
    suma = 0
    
    for i in range(n):
        for j in range(n):
            x1_k = a1 + i * h1
            x2_k = a2 + j * h2
            suma += f(x1_k, x2_k)
        
    integral = (b1 - a1) * (b2 - a2) * ((f(a1, a2) + f(b1, a2) + f(a1, b2) + f(b1, b2) + 2 * suma) / (4 * n**2))
    return integral

# Función para calcular la integral usando el método del trapecio compuesto para tres dimensiones
def trapecio_compuesto_triple(f, a1, b1, a2, b2, a3, b3, n):
    h1 = (b1 - a1) / n
    h2 = (b2 - a2) / n
    h3 = (b3 - a3) / n
    suma = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x1_k = a1 + i * h1
                x2_k = a2 + j * h2
                x3_k = a3 + k * h3
                suma += f(x1_k, x2_k, x3_k)
    
    integral = (b1 - a1) * (b2 - a2) * (b3 - a3) * ((f(a1, a2, a3) + f(b1, a2, a3) + f(a1, b2, a3) + f(b1, b2, a3) + 
                   f(a1, a2, b3) + f(b1, a2, b3) + f(a1, b2, b3) + f(b1, b2, b3) + 2 * suma) / (8 * n**3))
    return integral

# Función para solicitar los intervalos de integración para una dimensión dada
def pedir_intervalos(dim):
    intervalos = []
    for d in range(dim):
        a = float(input(f"Ingrese el valor del intervalo a para la dimensión {d+1}: "))
        b = float(input(f"Ingrese el valor del intervalo b para la dimensión {d+1}: "))
        intervalos.append((a, b))
    return intervalos

# Función para detectar la dimensión de la función ingresada
def detect_dimension(funcion_str):
    try:
        expr = sympify(funcion_str)
        variables = expr.free_symbols 
    except Exception as e:
        print(f"Error al analizar la función: {e}")
        variables = []
    return len(variables)

if __name__ == "__main__":
    print("-" * 90)
    print("Trapecio compuesto para integrales simples, dobles o triples".center(90))
    print("-" * 90)
    funcion_str = pedir_funcion()
    print("-" * 90)
    dimension = detect_dimension(funcion_str)
    
    if dimension == 1:
        print("Se ha detectado una integral simple.".center(90))
        print("-"*90)
        intervalos = pedir_intervalos(1)
        a, b = intervalos[0]
        n = int(input("Ingrese el número de intervalos que desea: "))
        f = lambdify('x', funcion_str, 'numpy')
        resultado = trapecio_compuesto_simple(f, a, b, n)
        print("-" * 90)
        print("Integral a evaluar:", funcion_str)
        print("Intervalo a:", a, "Intervalo b:", b)
        print("-" * 90)
        
        # Construir la tabla de subintervalos y resultados de la función
        tabla = [
            ["Intervalo", "Subintervalo", "Valor de la función"]
        ]
        h = (b - a) / n
        for i in range(n):
            x_a = a + i * h
            x_b = a + (i + 1) * h
            valor_funcion = f((x_a + x_b) / 2)  # Evaluar en el punto medio del subintervalo
            tabla.append([f"{a:.2f}, {b:.2f}", f"{x_a:.2f}, {x_b:.2f}", valor_funcion])
        
        # Imprimir la tabla utilizando tabulate
        print(tabulate(tabla, headers="firstrow", tablefmt="fancy_grid"))
        print("-"*90)
        print(f"Resultado de la integración = {resultado}")
    
    elif dimension == 2:
        print("Se ha detectado una integral doble.".center(90))
        print("-" * 90)
        intervalos = pedir_intervalos(2)
        if len(intervalos) < 2:
            print("Error: No se han proporcionado suficientes intervalos para una integral doble.")
        else:
            a1, b1 = intervalos[0]
            a2, b2 = intervalos[1]
            n = int(input("Ingrese el número de intervalos que desea: "))
            f = lambdify(('x', 'y'), funcion_str, 'numpy')
            resultado = trapecio_compuesto_doble(f, a1, b1, a2, b2, n)
            print("-" * 90)
            print("Integral a evaluar:", funcion_str)
            print("Intervalos por dimensión:", intervalos)
            print("-" * 90)
            
            # Construir la tabla de subintervalos y resultados de la función
            tabla = [
                ["Intervalo", "Subintervalo", "Valor de la función"]
            ]
            h1 = (b1 - a1) / n
            h2 = (b2 - a2) / n
            for i in range(n):
                for j in range(n):
                    x1_a = a1 + i * h1
                    x1_b = a1 + (i + 1) * h1
                    x2_a = a2 + j * h2
                    x2_b = a2 + (j + 1) * h2
                    valor_funcion = f((x1_a + x1_b) / 2, (x2_a + x2_b) / 2)  # Evaluar en el punto medio del subintervalo
                    tabla.append([f"({a1:.2f}, {b1:.2f}), ({a2:.2f}, {b2:.2f})",
                                  f"({x1_a:.2f}, {x1_b:.2f}), ({x2_a:.2f}, {x2_b:.2f})",
                                  valor_funcion])
            
            # Imprimir la tabla utilizando tabulate
            print(tabulate(tabla, headers="firstrow", tablefmt="fancy_grid"))
            print("-" * 90)
            print(f"Resultado de la integración = {resultado}")
    
    elif dimension == 3:
        print("Se ha detectado una integral triple.".center(90))
        print("-" * 90)
        intervalos = pedir_intervalos(3)
        if len(intervalos) < 3:
            print("Error: No se han proporcionado suficientes intervalos para una integral triple.")
        else:
            a1, b1 = intervalos[0]
            a2, b2 = intervalos[1]
            a3, b3 = intervalos[2]
            n = int(input("Ingrese el número de intervalos que desea: "))
            f = lambdify(('x', 'y', 'z'), funcion_str, 'numpy')
            resultado = trapecio_compuesto_triple(f, a1, b1, a2, b2, a3, b3, n)
            print("-" * 90)
            print("Integral a evaluar:", funcion_str)
            print("Intervalos por dimensión:", intervalos)
            print("-" * 65)
            
            
            # Construir la tabla de subintervalos y resultados de la función
            tabla = [
                ["Intervalo", "Subintervalo", "Valor de la función"]
            ]
            h1 = (b1 - a1) / n
            h2 = (b2 - a2) / n
            h3 = (b3 - a3) / n
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        x1_a = a1 + i * h1
                        x1_b = a1 + (i + 1) * h1
                        x2_a = a2 + j * h2
                        x2_b = a2 + (j + 1) * h2
                        x3_a = a3 + k * h3
                        x3_b = a3 + (k + 1) * h3
                        valor_funcion = f((x1_a + x1_b) / 2, (x2_a + x2_b) / 2, (x3_a + x3_b) / 2)  # Evaluar en el punto medio del subintervalo
                        tabla.append([f"({a1:.2f}, {b1:.2f}), ({a2:.2f}, {b2:.2f}), ({a3:.2f}, {b3:.2f})",
                                      f"({x1_a:.2f}, {x1_b:.2f}), ({x2_a:.2f}, {x2_b:.2f}), ({x3_a:.2f}, {x3_b:.2f})",
                                      valor_funcion])
            
            # Imprimir la tabla utilizando tabulate
            print(tabulate(tabla, headers="firstrow", tablefmt="fancy_grid"))
            print("-" * 90)
            print(f"Resultado de la integración = {resultado}")
    
    else:
        print("No se puede manejar una integral de más de tres dimensiones.")

