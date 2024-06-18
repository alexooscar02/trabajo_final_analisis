from sympy import symbols, Poly, parse_expr, exp
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
import re
import sympy as sp
import numpy as np
import pandas as pd

x = symbols('x')

# Función para pedir valores de xk o yk
def pedir_valores(nombre):
    while True:
        try:
            valores = input(f"Ingrese los valores de {nombre} separados por comas: ")
            lista_valores = [float(val) for val in valores.split(',')]
            return lista_valores
        except ValueError:
            print("Error: Por favor, ingrese números válidos separados por comas.")

# Función para pedir la función matemática
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
                    print(f"➣ Ecuacion: {exp_pol}")
                    return expr
                except:
                    print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
            else:
                print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

def eval_func(func, x_val, y_val):
    x, y = sp.symbols('x y')
    return float(func.subs({x: x_val, y: y_val}).evalf())

def runge_kutta_method(func, x0, y0, xf, h, order):
    x0, y0, xf, h = float(x0), float(y0), float(xf), float(h)
    n = int((xf - x0) / h)

    x_vals = [x0]
    y_vals = [y0]

    if order == 2:
        method = runge_kutta_2
    elif order == 3:
        method = runge_kutta_3
    elif order == 4:
        method = runge_kutta_4
    else:
        print("Error: Orden no válido. Debe ser 2, 3 o 4.")
        return

    data = []
    for i in range(n):
        x_prev = x_vals[-1]
        y_prev = y_vals[-1]
        x_next, y_next, k1, k2, k3, k4 = method(func, x_prev, y_prev, h)
        x_vals.append(x_next)
        y_vals.append(y_next)
        data.append([i, x_prev, y_prev, k1, k2, k3, k4, y_next])

    df = pd.DataFrame(data, columns=['Iter', 'x_i', 'y_i', 'k1', 'k2', 'k3', 'k4', 'y_(i+1)'])
    df.fillna('', inplace=True)  # Reemplaza None con una cadena vacía para una mejor visualización
    print(df.to_string(index=False))

    return x_vals, y_vals

def runge_kutta_2(func, x_prev, y_prev, h):
    k1 = h * eval_func(func, x_prev, y_prev)
    k2 = h * eval_func(func, x_prev + h, y_prev + k1)
    y_next = y_prev + (k1 + k2) / 2
    x_next = x_prev + h
    return x_next, y_next, k1, k2, None, None

def runge_kutta_3(func, x_prev, y_prev, h):
    k1 = h * eval_func(func, x_prev, y_prev)
    k2 = h * eval_func(func, x_prev + h / 2, y_prev + k1 / 2)
    k3 = h * eval_func(func, x_prev + h, y_prev - k1 + 2 * k2)
    y_next = y_prev + (k1 + 4 * k2 + k3) / 6
    x_next = x_prev + h
    return x_next, y_next, k1, k2, k3, None

def runge_kutta_4(func, x_prev, y_prev, h):
    k1 = h * eval_func(func, x_prev, y_prev)
    k2 = h * eval_func(func, x_prev + h / 2, y_prev + k1 / 2)
    k3 = h * eval_func(func, x_prev + h / 2, y_prev + k2 / 2)
    k4 = h * eval_func(func, x_prev + h, y_prev + k3)
    y_next = y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x_next = x_prev + h
    return x_next, y_next, k1, k2, k3, k4

def main_runge_kutta():
    funcion = pedir_funcion("Ingrese la función f(x,y): ")  # Función a trabajar
    x0 = float(input("Ingrese el valor inicial de x (x0): "))  # Valor inicial de x
    y0 = float(input("Ingrese el valor inicial de y (y0): "))  # Valor inicial de y
    xf = float(input("Ingrese el valor final de x (xf): "))  # Valor final de x
    h = float(input("Ingrese el paso (h): "))  # Paso

    print("Seleccione el orden del método de Runge-Kutta:")
    print("1. Orden 2")
    print("2. Orden 3")
    print("3. Orden 4")
    orden = int(input("Ingrese el número de opción: "))

    if orden == 1:
        runge_kutta_method(funcion, x0, y0, xf, h, order=2)
    elif orden == 2:
        runge_kutta_method(funcion, x0, y0, xf, h, order=3)
    elif orden == 3:
        runge_kutta_method(funcion, x0, y0, xf, h, order=4)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main_runge_kutta()
