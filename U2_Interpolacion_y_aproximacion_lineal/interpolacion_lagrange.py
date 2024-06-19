import sympy as sp
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
import re

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

# Función principal para calcular interpolación de Lagrange
def calcular_lagrange():
    print("METODO DE INTERPOLACION DE LAGRANGE\n")
    
    print("Seleccione el método de entrada:")
    print("1. Ingresar los valores de x y y directamente.")
    print("2. Definir una función f(x) y proporcionar los valores de x.")
    opcion = int(input("Ingrese el número de opción: "))
    
    if opcion == 1:
        xk = pedir_valores("xk")
        yk = pedir_valores("yk")
    elif opcion == 2:
        funcion = pedir_funcion("Ingrese la función f(x): ")
        xk = pedir_valores("xk")
        yk = [funcion.subs(x, xi).evalf() for xi in xk]
    else:
        print("Opción no válida.")
        return

    if len(xk) != len(yk):
        print("Error: Las listas de xk y yk deben tener la misma longitud.")
        return

    while True:
        try:
            punto = float(input("Ingrese el punto donde evaluar el polinomio: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    lagrange_poli = 0
    for i in range(len(xk)):
        term = yk[i]
        for j in range(len(xk)):
            if i != j:
                term *= (x - xk[j]) / (xk[i] - xk[j])
        lagrange_poli += term

    lagrange_poli_exp = sp.expand(lagrange_poli)

    print(f"\nPolinomio resultante P(x) = {lagrange_poli}")
    print(f"Polinomio reducido P(x) = {lagrange_poli_exp}\n")

    resultado = lagrange_poli.subs(x, punto).evalf()
    print(f"P({punto}) = {resultado}")

    return lagrange_poli_exp, resultado

# Ejecutar la función principal

