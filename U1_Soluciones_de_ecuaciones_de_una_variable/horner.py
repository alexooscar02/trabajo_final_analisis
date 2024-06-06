import pandas as pd
from sympy import *
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
from sympy.abc import *

x = symbols('x')

def pedir_funcion():
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input("Ingrese la función en términos de x: ")
        caracteres_permitidos = set('x+-**/^() ')
        if all(c.isalnum() or c in caracteres_permitidos for c in expr_str):
            try:
                expr = parse_expr(expr_str, transformations=transformations)
                exp_pol = Poly(expr)
                print(f"➣ Ecuacion: {exp_pol}")
                coeficientes = exp_pol.all_coeffs()
                return coeficientes, expr
            except:
                print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
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

def division_sintetica(coeficientes, a):
    n = len(coeficientes)
    n_coeficientes = [coeficientes[0]]
    b = coeficientes[0]

    for i in range(1, n):
        b = b * a + coeficientes[i]
        n_coeficientes.append(b)

    return n_coeficientes[:-1], n_coeficientes[-1]

def calcular_horner():
    print("\n\t\tMETODO DE HORNER")
    print("\n")
    coeficientes, func = pedir_funcion()
    x0 = pedir_cifras("➔ Digite el valor inicial x0: ")

    opcion = input("¿Deseas ingresar las cifras significativas o la tolerancia directamente? (c/t): ")
    while opcion.lower() not in ['c', 't']:
        opcion = input("Opción inválida. Ingresa 'c' para cifras significativas o 't' para tolerancia: ")

    if opcion.lower() == 'c':
        cifras = pedir_cifras("➔ Digite las cifras significativas: ")
        Es = 0.5 * 10 ** (2 - cifras)
    else:
        Es = pedir_cifras("➔ Digite la tolerancia: ")

    Ea = 100 if opcion.lower() == 'c' else 1
    i = 0
    df = pd.DataFrame(columns=["Iteración", "xi-1", "xi", "Ea(%)"])
    while Ea > Es:
        x0 = float(x0)
        n_coeficientes, R = division_sintetica(coeficientes, x0)
        na, S = division_sintetica(n_coeficientes, x0)
        xi = x0 - (R / S)
        Ea = abs((xi - x0) / xi) * 100 if opcion.lower() == 'c' else abs((xi - x0) / xi)
        x0 = xi
        i += 1
        df.loc[i - 1] = [i, x0, xi, Ea]

    print(f"Función: ƒ(x) = {sympify(func)} con un nivel de tolerancia del {Es}%. Con x0 = {x0}")
    print(df)
    print(f"La raíz de la ecuación es {x0} con un error de {Ea:.{int(cifras)}f}% en la {i}° iteración") if opcion.lower() == 'c' else print(f"La raíz de la ecuación es {x0} con un error de {Ea:.6f} en la {i}° iteración")

if __name__ == "__main__":
    calcular_horner()
