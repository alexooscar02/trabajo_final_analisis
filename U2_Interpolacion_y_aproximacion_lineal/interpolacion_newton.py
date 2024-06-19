import sympy as sp
import pandas as pd
import re
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication, convert_xor
from sympy import Poly

# Definir la variable simbólica 'x'
x = sp.symbols("x")

# Función para solicitar y validar la función del usuario
def pedir_funcion(mensaje):
    transformations = standard_transformations + (implicit_multiplication, convert_xor)
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

# Función para interpolación de Newton con diferencias divididas
def interpolacion_newton_diferencias_divididas(funcion, valores_x, valores_y, punto_evaluacion):
    print("METODO DE INTERPOLACION DE NEWTON POR DIFERENCIAS DIVIDIDAS\n")
    if funcion is not None:
        print(f"Para f(x) = {funcion}\n")
    
    n = len(valores_x)
    tabla_diferencias = [[None] * n for _ in range(n)]
    
    for i in range(n):
        tabla_diferencias[i][0] = valores_y[i]

    for j in range(1, n):
        for i in range(n - j):
            tabla_diferencias[i][j] = (tabla_diferencias[i + 1][j - 1] - tabla_diferencias[i][j - 1]) / (valores_x[i + j] - valores_x[i])
    
    df = pd.DataFrame(tabla_diferencias, index=valores_x, columns=[f"f[x{i}]" for i in range(len(valores_x))])
    print("Tabla de diferencias divididas:")
    print(df, "\n")
    
    polinomio = tabla_diferencias[0][0]
    producto = 1

    for j in range(1, n):
        producto *= (x - valores_x[j - 1])
        polinomio += tabla_diferencias[0][j] * producto
    
    polinomio_expandido = sp.expand(polinomio)
    print("Polinomio de Newton:")
    print(polinomio_expandido, "\n")
    
    valor_evaluado = polinomio_expandido.subs(x, punto_evaluacion)
    if funcion is not None:
        valor_verdadero = funcion.subs(x, punto_evaluacion).evalf()
        error_porcentual = abs((valor_evaluado - valor_verdadero) / valor_verdadero) * 100
        print(f"Evaluación en x = {punto_evaluacion}:")
        print(f"f({punto_evaluacion}) =", valor_evaluado)
        print(f"Valor verdadero =", valor_verdadero)
        print(f"Error porcentual = {error_porcentual}%\n")
    else:
        print(f"Evaluación en x = {punto_evaluacion}:")
        print(f"f({punto_evaluacion}) =", valor_evaluado)

    # Calcular el error teórico si se proporciona una función
    if funcion is not None:
        n = len(valores_x) - 1  
        a, b = valores_x[0], valores_x[-1]  
        xi = (a + b) / 2  

        derivada_n_mas_1 = sp.diff(funcion, x, n+1).subs(x, xi).evalf()

        factorial_n_mas_1 = sp.factorial(n+1)

        producto_terminos = 1
        for xi_valor in valores_x:
            producto_terminos *= (punto_evaluacion - xi_valor)

        # Error teórico
        error_teorico = abs(derivada_n_mas_1 / factorial_n_mas_1) * producto_terminos
        print(f"Error Teórico = {error_teorico.evalf()}\n")

# Función para calcular el polinomio de interpolación de Newton en forma recursiva
def calculo_newton_interpolacion_recursiva(valores_x, valores_y, punto_evaluacion):
    print("\n\tINTERPOLACIÓN DE NEWTON (FORMA RECURSIVA)\n")
    
    # Inicializar los coeficientes
    n = len(valores_x)
    b = [valores_y[0]]  # Primer coeficiente es simplemente f(x0)

    # Cálculo de coeficientes b recursivamente
    for j in range(1, n):
        numerador = valores_y[j]
        for k in range(j):
            producto = 1
            for m in range(k):
                producto *= (valores_x[j] - valores_x[m])
            numerador -= b[k] * producto
        denominador = 1
        for m in range(j):
            denominador *= (valores_x[j] - valores_x[m])
        b.append(numerador / denominador)

    # Mostrar los coeficientes calculados
    for i, bi in enumerate(b):
        print(f"b{i} = {bi}")

    # Construir el polinomio de Newton
    polinomio = b[0]
    for j in range(1, n):
        termino = b[j]
        for i in range(j):
            termino *= (x - valores_x[i])
        polinomio += termino

    # Expandir el polinomio para simplificarlo
    polinomio_expandido = sp.expand(polinomio)
    print("\nPolinomio de Newton:")
    print(polinomio_expandido.expand())

    # Evaluar el polinomio en el punto de evaluación
    valor_evaluado = polinomio_expandido.subs(x, punto_evaluacion)
    print(f"\nEvaluación en x = {punto_evaluacion}:")
    print(f"f({punto_evaluacion}) = {valor_evaluado}")

# Función principal para elegir el método de interpolación
def calcular_interpolacion_newton():
    print("Seleccione el método de interpolación de Newton:")
    print("1. Diferencias divididas")
    print("2. Forma recursiva")
    metodo = int(input("Ingrese el número del método que desea utilizar: "))

    print("Seleccione el método de entrada:")
    print("1. Ingresar los valores de x y y directamente.")
    print("2. Definir una función f(x) y proporcionar los valores de x.")
    opcion = int(input("Ingrese el número de opción: "))

    funcion = None
    valores_x = []
    valores_y = []

    if opcion == 1:
        # Ingresar valores de x y y directamente
        valores_x = list(map(float, input("Ingrese los valores de x separados por comas: ").split(',')))
        valores_y = list(map(float, input("Ingrese los valores de y separados por comas: ").split(',')))
    elif opcion == 2:
        # Utilizar la función pedir_funcion para solicitar la función f(x)
        funcion = pedir_funcion("Ingrese la función f(x) en términos de x (ejemplo: x**2 + 2*x + 1): ")
        valores_x = list(map(float, input("Ingrese los valores de x separados por comas: ").split(',')))
        valores_y = [float(funcion.subs(x, xi)) for xi in valores_x]
    else:
        print("Opción no válida.")
        return

    # Ingresar el punto de evaluación
    punto_evaluacion = float(input("Ingrese el valor de x para evaluar el polinomio: "))

    # Llamar a la función de interpolación seleccionada
    if metodo == 1:
        interpolacion_newton_diferencias_divididas(funcion, valores_x, valores_y, punto_evaluacion)
    elif metodo == 2:
        calculo_newton_interpolacion_recursiva(valores_x, valores_y, punto_evaluacion)
    else:
        print("Método de interpolación no válido.")

# Ejecutar la función principal
