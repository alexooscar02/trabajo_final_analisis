from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
import cmath

x = symbols('x')

def pedir_funcion():
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input("Ingrese la función en términos de x: ")
        caracteres_permitidos = set('x+-*/^() ')
        if all(c.isalnum() or c in caracteres_permitidos for c in expr_str):
            try:
                expr = parse_expr(expr_str, transformations=transformations)
                exp_pol = Poly(expr, x)
                coeficientes = exp_pol.all_coeffs()
                
                if len(coeficientes) < 3:
                    print("Error: La función debe ser una ecuación cuadrática de grado dos. Por favor, inténtalo de nuevo.")
                    continue
                elif len(coeficientes) > 3:
                    print("Error: La función no debe ser de un grado mayor que dos. Por favor, inténtalo de nuevo.")
                    continue

                while len(coeficientes) < 3:
                    coeficientes.insert(0, 0)
                
                print(f"➣ Ecuacion: {exp_pol}")
                print(f"Coeficientes: {coeficientes}")
                return coeficientes, expr
            except Exception as e:
                print(f"Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

def calcular_ec_cuadratica():
    coeficientes, expr = pedir_funcion()
    a, b, c = coeficientes

    discriminante = b**2 - 4*a*c

    if discriminante >= 0:
        # Raíces reales
        raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    else:
        # Raíces complejas
        raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)

    print(f"Las raíces de la ecuación son: {raiz1} y {raiz2}")

calcular_ec_cuadratica()
