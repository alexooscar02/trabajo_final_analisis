import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from sympy import sympify, symbols, lambdify, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor


import re

def pedir_funcion(mensaje):
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input(mensaje)
        if all(c not in expr_str for c in "#$%&\"'_`~{}[]@¿¡!?°|;:<>"):
            valid_chars_pattern = re.compile(r'^[a-zA-Z0-9\s\+\-\*/\^\(\)\|\.,]*$')
            if valid_chars_pattern.match(expr_str):
                try:
                    expr = parse_expr(expr_str, transformations=transformations)
                    exp_pol = Poly(expr)
                    print(f"➣ Ecuacion: {exp_pol}\n")
                    return expr
                except:
                    print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
            else:
                print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

def cuadratica_gaussiana(funcion, a, b, nodos, pesos):
    x = sp.symbols('x')
    try:
        funcion_expr = sp.sympify(funcion)
        f = sp.lambdify(x, funcion_expr, 'numpy')
    except (sp.SympifyError, TypeError) as e:
        print(f"La función ingresada es inválida: {e}")
        return None
    
    try:
        # Ajustar los nodos al intervalo [a, b]
        ajustando_nodos = 0.5 * (b - a) * nodos + 0.5 * (a + b)
        
        # Calcular la aproximación de la integral utilizando los nodos y pesos definidos globalmente
        integral = np.sum(pesos * f(ajustando_nodos))
        
        # Ajustar la integral al intervalo [a, b]
        integral *= 0.5 * (b - a)
        
        return integral
    except Exception as e:
        print(f"Error al calcular la integral: {str(e)}")

def main_gauss():
    print("-" * 150)
    print("Cuadrática Gaussiana Personalizada".center(150))
    print("-" * 150)
    
    # Pidiendo la función
    funcion_str = pedir_funcion("Digite la funcion: ")
    print("-" * 150)
    
    # Pidiendo los intervalos al usuario
    try:
        a = float(input("Ingrese el límite inferior del intervalo de integración: "))
        b = float(input("Ingrese el límite superior del intervalo de integración: "))
    except ValueError:
        print("Ingrese números válidos para los intervalos.")
        return
    
    print("-" * 150)
    
    # Pidiendo la cantidad de puntos para la cuadrática gaussiana
    try:
        n = int(input("Ingrese la cantidad de puntos para la Cuadrática Gaussiana: "))
        if n <= 0:
            raise ValueError("La cantidad de puntos debe ser un número positivo.")
    except ValueError as e:
        print(e)
        return
    
    print("-" * 150)
    
    # Definiendo los nodos y pesos para la cuadratura Gaussiana
    nodos, pesos = leggauss(n)
    
    # Calculando la aproximación de la integral utilizando cuadrática gaussiana 
    integral_approx = cuadratica_gaussiana(funcion_str, a, b, nodos, pesos)
    if integral_approx is not None:
        print(f"El valor aproximado de la integral ∫ {funcion_str} dx en el intervalo [{a}, {b}] utilizando cuadratura Gaussiana es: {integral_approx}")

if __name__ == "__main__":
    main_gauss()
