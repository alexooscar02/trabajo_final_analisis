import sympy as sp

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

def metodo_boyle(funcion, a, b):
    # Definimos los puntos x0, x1, x2, x3, x4 dentro del intervalo [a, b]
    h = (b - a) / 4
    x0 = a
    x1 = a + h
    x2 = a + 2 * h
    x3 = a + 3 * h
    x4 = b
    
    # Evaluamos la función en los puntos x0, x1, x2, x3, x4
    f_x0 = float(funcion.subs('x', x0))
    f_x1 = float(funcion.subs('x', x1))
    f_x2 = float(funcion.subs('x', x2))
    f_x3 = float(funcion.subs('x', x3))
    f_x4 = float(funcion.subs('x', x4))
    
    # Aplicamos la fórmula del método de Boyle para la integral
    integral_aproximada = ((2 * h) / 45) * (7 * f_x0 + 32 * f_x1 + 12 * f_x2 + 32 * f_x3 + 7 * f_x4)
    
    return integral_aproximada

def main_boyle():
    print("-"*120)
    print("Método de Boyle para aproximación de integral".center(120))
    print("-"*120)
    
    # Solicitamos al usuario ingresar la función
    funcion_str = pedir_funcion("Ingrese la funcion en terminos de x: ")  # Esta función debería retornar la cadena de la función ingresada por el usuario
    funcion = sp.sympify(funcion_str)
    
    # Solicitamos al usuario ingresar los límites de integración
    while True:
        try:
            a = float(input("Ingrese el límite inferior 'a' del intervalo: "))
            b = float(input("Ingrese el límite superior 'b' del intervalo: "))
            
            # Verificar si a y b son números válidos
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                break  # Salir del bucle si ambos son números válidos
            else:
                print("Por favor, ingrese números válidos para los límites de integración.")
        except ValueError:
            print("Error: Por favor, ingrese números válidos para los límites de integración.")
    
    # Calculamos la integral aproximada usando el método de Boyle
    integral_aproximada = metodo_boyle(funcion, a, b)
    
    # Mostramos el resultado
    print("-"*120)
    print(f"\nLa aproximación de la integral de la función en el intervalo [{a}, {b}] es: {integral_aproximada}")

if __name__ == "__main__":
    main_boyle()

