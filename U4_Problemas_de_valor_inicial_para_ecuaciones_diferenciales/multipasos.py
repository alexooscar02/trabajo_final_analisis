from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
import re
import sympy as sp
import numpy as np
import pandas as pd

x, y = symbols('x y')

# Función para solicitar y parsear una función matemática del usuario
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

# Función para evaluar una función dada en valores específicos de x e y
def eval_func(func, x_val, y_val):
    return float(func.subs({x: x_val, y: y_val}).evalf())

# Métodos de Runge-Kutta
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
    df.fillna('', inplace=True)
    print(df.to_string(index=False))

    return x_vals, y_vals

class Adaptativo:
    def __init__(self, f, x0, y0, xf, h, pasos=4):
        self.funcion = f
        self.x0 = x0
        self.y0 = y0
        self.xf = xf
        self.h = h
        self.pasos = pasos
        self.n = int((self.xf - self.x0) / self.h)

    @property
    def adaptativo(self):
        if self.pasos not in [2, 3, 4]:
            return "Error: El número de pasos debe ser 2, 3 o 4."

        x, ykutta = runge_kutta_method(self.funcion, self.x0, self.y0, self.xf, self.h, self.pasos)

        print("Valores iniciales de Runge-Kutta:")
        for xi, yi in zip(x, ykutta):
            print(f"x = {xi}, y = {yi}")

        valores = []

        for k in range(self.pasos):
            valores.append(ykutta[k])

        for i in range(self.pasos - 1, self.n):
            print(f"\nIteración {i + 1}:")
            if self.pasos == 4:
                predictor = ykutta[i] + ((self.h / 24) * (
                        55 * eval_func(self.funcion, x[i], ykutta[i]) - 
                        59 * eval_func(self.funcion, x[i - 1], ykutta[i - 1]) +
                        37 * eval_func(self.funcion, x[i - 2], ykutta[i - 2]) - 
                        9 * eval_func(self.funcion, x[i - 3], ykutta[i - 3])))
                corrector = ykutta[i] + ((self.h / 24) * (
                        9 * eval_func(self.funcion, x[i + 1], predictor) + 
                        19 * eval_func(self.funcion, x[i], ykutta[i]) -
                        5 * eval_func(self.funcion, x[i - 1], ykutta[i - 1]) + 
                        eval_func(self.funcion, x[i - 2], ykutta[i - 2])))
            elif self.pasos == 3:
                predictor = ykutta[i] + ((self.h / 12) * (
                        23 * eval_func(self.funcion, x[i], ykutta[i]) - 
                        16 * eval_func(self.funcion, x[i - 1], ykutta[i - 1]) +
                        5 * eval_func(self.funcion, x[i - 2], ykutta[i - 2])))
                corrector = ykutta[i] + ((self.h / 12) * (
                        5 * eval_func(self.funcion, x[i + 1], predictor) + 
                        8 * eval_func(self.funcion, x[i], ykutta[i]) -
                        eval_func(self.funcion, x[i - 1], ykutta[i - 1])))
            elif self.pasos == 2:
                predictor = ykutta[i] + (self.h / 2) * (
                        3 * eval_func(self.funcion, x[i], ykutta[i]) - 
                        eval_func(self.funcion, x[i - 1], ykutta[i - 1]))
                corrector = ykutta[i] + (self.h / 2) * (
                        eval_func(self.funcion, x[i + 1], predictor) + 
                        eval_func(self.funcion, x[i], ykutta[i]))

            ykutta.append(corrector)
            valores.append(corrector)
            print(f"Predicción: {predictor}, Corrección: {corrector}")

        print("\nResultado final:")
        print(f"x final: {x[-1]}, y final (Adaptativo): {ykutta[-1]}")

        return x, valores

def main_multipasos():
    # Solicitar la función al usuario
    funcion = pedir_funcion("Ingrese la función f(x,y): ")

    # Solicitar otros parámetros al usuario
    x0 = float(input("Ingrese el valor inicial de x (x0): "))
    y0 = float(input("Ingrese el valor inicial de y (y0): "))
    xf = float(input("Ingrese el valor final de x (xf): "))
    h = float(input("Ingrese el paso (h): "))

    print("Seleccione el número de pasos para el método adaptativo:")
    print("1. 2 pasos")
    print("2. 3 pasos")
    print("3. 4 pasos")
    pasos = int(input("Ingrese el número de opción: "))

    if pasos in [1, 2, 3]:
        adaptativo = Adaptativo(funcion, x0, y0, xf, h, pasos=pasos + 1)  # Incrementar pasos para seleccionar entre 2, 3 y 4.
        adaptativo.adaptativo
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main_multipasos()
