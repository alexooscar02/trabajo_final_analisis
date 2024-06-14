import sympy as sp
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
from sympy.abc import *

x = symbols('x')

def pedir_valores(nombre):
    while True:
        try:
            valores = input(f"Ingrese los valores de {nombre} separados por comas: ")
            lista_valores = [float(val) for val in valores.split(',')]
            return lista_valores
        except ValueError:
            print("Error: Por favor, ingrese números válidos separados por comas.")

def calcular_lagrange():
    print("METODO DE INTERPOLACION DE LAGRANGE\n")

    # Pedir valores de xk y yk al usuario
    xk = pedir_valores("xk")
    yk = pedir_valores("yk")

    # Validar que xk y yk tengan la misma longitud
    if len(xk) != len(yk):
        print("Error: Las listas de xk y yk deben tener la misma longitud.")
        return

    # Pedir el punto donde se evaluará el polinomio
    while True:
        try:
            punto = float(input("Ingrese el punto donde evaluar el polinomio: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    lagrange_poli = 0

    # Construir el polinomio de Lagrange
    for i in range(len(xk)):
        term = yk[i]
        for j in range(len(xk)):
            if i != j:
                term *= (x - xk[j]) / (xk[i] - xk[j])
        lagrange_poli += term

    # Expandir el polinomio para una forma más simplificada
    lagrange_poli_exp = sp.expand(lagrange_poli)

    print(f"\nPolinomio resultante P(x) = {lagrange_poli}")
    print(f"Polinomio reducido P(x) = {lagrange_poli_exp}\n")

    # Evaluar el polinomio en el punto dado
    resultado = lagrange_poli.subs(x, punto).evalf()
    print(f"P({punto}) = {resultado}")

    return lagrange_poli_exp, resultado

calcular_lagrange()
