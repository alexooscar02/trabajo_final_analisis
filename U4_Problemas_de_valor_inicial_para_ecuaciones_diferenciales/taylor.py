from sympy import symbols, Poly, parse_expr, diff, sympify
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
import re
import numpy as np
import pandas as pd
from math import pow, factorial

x, y = symbols('x y')

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

def pedir_cifras(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip():
            try:
                numero = sympify(valor)
                if numero.is_real:
                    return float(numero)
                else:
                    print("Error: Ingresa un número real válido.")
            except (ValueError, TypeError):
                print("Error: Ingresa un número válido.")
        else:
            print("Error: No puedes dejar este campo vacío.")

class Taylor:
    def __init__(self, funct, xi, yi, xf, grado=2, h=0, n=0, derivadas=[]):
        self.funct_str = funct  # Guardamos la cadena de la función
        self.funct = sympify(funct.replace("^", "**"))  # Convertimos la cadena en una expresión sympy
        self.xi = sympify(xi)
        self.yi = sympify(yi)
        self.xf = sympify(xf)
        self.grado = grado
        self.h = float(h) if h else 0
        self.n = int(n) if n else 0
        self.derivadas = derivadas

    def parciales(self, funcion):
        parcial_x = diff(funcion, x)
        parcial_x = parcial_x + y
        derivada = parcial_x.subs(y, self.funct)
        return derivada.expand()

    def eval(self, funcion, valor_x, valor_y):
        return funcion.subs([(x, float(valor_x)), (y, float(valor_y))])

    def taylor(self):
        if self.n == 0 and self.h == 0:
            print("Error: Debes proporcionar un tamaño de paso (h) o una cantidad de puntos (n).")
            return

        if self.h == 0:
            try:
                self.h = (float(self.xf) - float(self.xi)) / self.n
            except ZeroDivisionError:
                print("Error: División por cero al calcular h.")
                return
            except TypeError:
                print("Error: Valor no numérico para n.")
                return

        if self.n == 0:
            try:
                self.n = (float(self.xf) - float(self.xi)) / self.h
            except ZeroDivisionError:
                print("Error: División por cero al calcular n.")
                return
            except TypeError:
                print("Error: Valor no numérico para h.")
                return

        try:
            x_vals = np.linspace(float(self.xi), float(self.xf), int(self.n + 1))
        except ValueError as e:
            print(f"Error: {e}")
            return

        y_vals = [float(self.yi)]

        fi = [self.funct]
        if len(self.derivadas) == 0:
            for i in range(self.grado):
                fi.append(self.parciales(fi[-1]))
        else:
            fi += [sympify(funct) for funct in self.derivadas]

        data = {"x": [x_vals[0]], "y (Taylor)": [float(y_vals[0])]}

        for i in range(1, len(x_vals)):
            T = y_vals[i - 1]
            for k in range(len(fi)):
                T += (self.eval(fi[k], x_vals[i - 1], y_vals[i - 1])) * (pow(self.h, k + 1) / factorial(k + 1))
            y_vals.append(float(T))
            data["x"].append(x_vals[i])
            data["y (Taylor)"].append(float(T))

        df = pd.DataFrame(data)
        return df

def main_taylor():
    print("Método de Taylor para resolver ecuaciones diferenciales ordinarias (EDO) ")
    print("-----------------------------------------------------------------------")
    funcion = pedir_funcion("Ingrese la función f(x,y): ")
    xi = pedir_cifras("Ingrese el valor inicial de x (x0): ")
    yi = pedir_cifras("Ingrese el valor inicial de y (y0): ")
    xf = pedir_cifras("Ingrese el valor final de x (xf): ")
    h = pedir_cifras("Ingrese el paso (h): ")
    grado = int(pedir_cifras("Ingrese el grado del polinomio de Taylor: "))

    taylor_solver = Taylor(funct=str(funcion), xi=xi, yi=yi, xf=xf, grado=grado, h=h)
    results_df = taylor_solver.taylor()

    print("\nTabla de valores:")
    print(results_df.to_string(index=False))

    print("\nResultado final:")
    print(f"x final: {results_df.iloc[-1]['x']}, y final (Taylor): {results_df.iloc[-1]['y (Taylor)']}")

if __name__ == "__main__":
    main_taylor()
