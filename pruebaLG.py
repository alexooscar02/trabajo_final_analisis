import sympy as sp
import pandas as pd
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, 
                                        implicit_multiplication, split_symbols, convert_xor)

x = sp.symbols("x")

def pedir_funcion():
    transformations = (standard_transformations + (split_symbols, implicit_multiplication, convert_xor))
    while True:
        try:
            expr_str = input("Ingrese la función en términos de x (ej: log(x), x**2 + 3*x - 1): ")
            funcion = parse_expr(expr_str, transformations=transformations)
            return funcion
        except Exception as e:
            print(f"Error al parsear la función: {e}. Por favor, inténtelo de nuevo.")

def pedir_valores_x():
    while True:
        try:
            valores_str = input("Ingrese los valores de x separados por comas (ej: 1, 2, 3, 4): ")
            valores_x = [float(val.strip()) for val in valores_str.split(',')]
            return valores_x
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para x, separados por comas.")

def pedir_punto_evaluacion():
    while True:
        try:
            punto = float(input("Ingrese el punto de evaluación: "))
            return punto
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el punto de evaluación.")

# Función principal para realizar la interpolación de Newton
def calculo_newton_interpolacion(funcion, valores_x, punto_evaluacion):
    print("\n\tINTERPOLACIÓN DE NEWTON RECURSIVO\n")
    print(f"Para f(x) = {funcion}\n")

    # Calculamos los valores de y evaluando la función en cada valor de x
    valores_y = [funcion.subs(x, v).evalf() for v in valores_x]

    # Mostramos los valores de x y y en una tabla
    df = pd.DataFrame({"x": valores_x, "f(x)": valores_y}).transpose()
    print(f"{df}\n")

    # Calcular los coeficientes b de Newton
    b = [valores_y[0]]  # Primer coeficiente

    for j in range(1, len(valores_x)):
        bn = (((valores_y[j] - valores_y[j - 1]) / (valores_x[j] - valores_x[j - 1])) - b[j - 1]) / (valores_x[j] - valores_x[0])
        b.append(bn)

    for i, bn in enumerate(b):
        print(f"b{i} = {bn}")

    # Construir el polinomio de Newton
    polinomio = b[0]
    for j in range(1, len(valores_x)):
        termino = b[j]
        for i in range(j):
            termino *= (x - valores_x[i])
        polinomio += termino

    # Expandir el polinomio para simplificarlo
    polinomio_expandido = sp.expand(polinomio)
    print("\nPolinomio de Newton:")
    print(polinomio_expandido)

    # Evaluar el polinomio en el punto de evaluación
    valor_evaluado = polinomio_expandido.subs(x, punto_evaluacion)
    print(f"\nEvaluación en x = {punto_evaluacion}:")
    print(f"f({punto_evaluacion}) =", valor_evaluado)

    # Valor real de la función en el punto de evaluación
    valor_real = funcion.subs(x, punto_evaluacion).evalf()
    print(f"(Valor Verdadero) =", valor_real)

    # Calcular el error porcentual
    error_porcentual = abs((valor_evaluado - valor_real) / valor_real) * 100
    print(f"Error porcentual = {error_porcentual}%\n")

    # Calcular el error teórico
    n = len(valores_x) - 1  # Grado del polinomio
    a, b = valores_x[0], valores_x[-1]  # Intervalo de interpolación
    xi = (a + b) / 2  # Punto medio del intervalo

    derivada_n_mas_1 = sp.diff(funcion, x, n + 1).subs(x, xi).evalf()

    factorial_n_mas_1 = sp.factorial(n + 1)

    producto_terminos = 1
    for xi_valor in valores_x:
        producto_terminos *= (punto_evaluacion - xi_valor)

    error_teorico = abs(derivada_n_mas_1 / factorial_n_mas_1) * producto_terminos
    print(f"Error Teórico = {error_teorico.evalf()}\n")

def main():
    funcion = pedir_funcion()
    valores_x = pedir_valores_x()
    punto_evaluacion = pedir_punto_evaluacion()

    calculo_newton_interpolacion(funcion, valores_x, punto_evaluacion)

if __name__ == "__main__":
    main()


    
