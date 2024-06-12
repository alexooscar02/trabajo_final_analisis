import pandas as pd
from sympy import *
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
from sympy.abc import *
import re

x = symbols('x')

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


def calcular_newton_raphson():
    print("\n\t\tMETODO DE NEWTON-RAPHSON") 

    # Pedir la función principal
    func = pedir_funcion("Ingrese la función principal: ")
    f = lambdify(x, func)

    # Calcular la derivada de la función
    derivada = diff(func, x)
    print(f"Derivada de la función: {derivada}")
    g = lambdify(x, derivada)

    segunda = diff(derivada, x)
    print(f"Segunda derivada de la funcion {segunda}")
    t =lambdify(x, segunda)

    # Verificar la derivada calculada
    print(f"f(x) = {func}")
    print(f"f'(x) = {derivada}")

    x0=0

    convergencia=(f(x0)*t(x0))/((g(x0))**2)
    print(convergencia)

    if convergencia<1:
        print("converge")
    else:
        print("no converge")

calcular_newton_raphson()