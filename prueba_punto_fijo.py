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

def calcular_punto_fijo():
    print("\t\tMETODO DEL PUNTO FIJO\n")
    f = Function('f')(x)
    g = Function('g')(x)
    p = Function('p')(x)

    # Función principal
    func = pedir_funcion("Ingrese la funcion principal: ")
    f = lambdify(x, func)

    # Función despejada, puede variar la convergencia dependiendo del despeje
    desp = pedir_funcion("Ingrese la funcion despejada: ")
    g = lambdify(x, desp)

    derivada = desp.diff(x)
    p = lambdify(x, derivada)

    df = pd.DataFrame(columns=["iteracion", "x", "g(x)", "Ea"])

    iteracion = 1

    x0 = pedir_cifras("Ingrese el valor inicial: ")

    Ea = 100

    opcion = input("¿Desea ingresar las cifras significativas o la tolerancia directamente? (c/t): ")
    while opcion.lower() not in ['c', 't']:
        opcion = input("Opción inválida. Ingrese 'c' para cifras significativas o 't' para tolerancia: ")

    if opcion.lower() == 'c':
        cifras = pedir_cifras("Ingrese las cifras significativas: ")
        Es = 0.5 * 10 ** (2 - cifras)
    else:
        Es = pedir_cifras("Ingrese la tolerancia: ")

    convergencia = p(x0)
    if convergencia < 1:
        print("Converge")

        while Ea > Es:
            xi_actual = g(x0)
            Ea = abs(((xi_actual - x0) / xi_actual)) if opcion.lower() == 't' else abs(((xi_actual - x0) / xi_actual) * 100)

            df.loc[iteracion - 1] = [iteracion, x0, xi_actual, Ea]

            x0=xi_actual
            iteracion += 1

        print("\n\t\tMETODO DEL PUNTO FIJO")
        print(f"Funcion: F(x) = {func} con un nivel de tolerancia del {Es}%. Con x0 = {x0}")
        print(df)
        print(f"La raíz de la ecuación es {xi_actual} con un error de {Ea}% en la {iteracion - 1}° iteración")
    else:
        print("NO CONVERGE")

calcular_punto_fijo()
