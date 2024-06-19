from sympy import symbols, sympify, parse_expr, Poly
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
import re
import numpy as np
import pandas as pd

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

class Euler:
    def __init__(self, funct, xi, yi, xf, h):
        self.funct = sympify(funct.replace("^", "**"))
        self.xi = sympify(xi)
        self.yi = sympify(yi)
        self.xf = sympify(xf)
        self.h = h
        self.n = int((float(self.xf) - float(self.xi)) / self.h)

    def eval(self, valorX, valorY=""):
        if "y" not in str(self.funct):
            return self.funct.subs(x, float(valorX))
        else:
            return self.funct.subs([(x, float(valorX)), (y, float(valorY))])

    def euler(self):
        x_vals = np.linspace(float(self.xi), float(self.xf), int(self.n + 1))
        y_vals = [self.yi]

        data = {"x": [x_vals[0]], "y (Euler)": [float(y_vals[0])]}

        for i in range(1, len(x_vals)):
            if "y" not in str(self.funct):
                new_y = y_vals[i - 1] + (self.eval(x_vals[i - 1]) * self.h)
            else:
                new_y = y_vals[i - 1] + (self.eval(x_vals[i - 1], y_vals[i - 1]) * self.h)
            y_vals.append(new_y)
            data["x"].append(x_vals[i])
            data["y (Euler)"].append(float(new_y))

        df = pd.DataFrame(data)
        return df

def main_euler():
    print("Método de Euler para resolver ecuaciones diferenciales ordinarias (EDO)")
    print("---------------------------------------------------------------")
    funcion = pedir_funcion("Ingrese la función f(x,y): ")
    xi = pedir_cifras("Ingrese el valor inicial de x (x0): ")
    yi = pedir_cifras("Ingrese el valor inicial de y (y0): ")
    xf = pedir_cifras("Ingrese el valor final de x (xf): ")
    h = pedir_cifras("Ingrese el paso (h): ")

    euler_solver = Euler(funct=str(funcion), xi=xi, yi=yi, xf=xf, h=h)
    results_df = euler_solver.euler()

    print("\nTabla de valores:")
    print(results_df.to_string(index=False))

    print("\nResultado final:")
    print(f"x final: {results_df.iloc[-1]['x']}, y final (Euler): {results_df.iloc[-1]['y (Euler)']}")

# Ejecución del programa
if __name__ == "__main__":
    main_euler()
