import sympy as sym
import re

def pedir_funcion():
    allowed_chars = r"[a-zA-Z\s\+\-\*/\^0-9\(\)\.,]"
    while True:
        funcion = input("Ingrese la función (solo se permiten letras y caracteres matemáticos): ")
        if re.match(allowed_chars, funcion):
            return funcion
        else:
            print("Función inválida. Por favor, inténtelo de nuevo.")

def Interpolacion_Cuadratica():
    print("-" * 90)
    print("                         Interpolacion Cuadratica       ")
    print("-" * 90)

    # Pedir al usuario la función a evaluar
    funcion_str = pedir_funcion()
    try:
        x = sym.Symbol('x')
        funcion = sym.sympify(funcion_str)
    except (ValueError, sym.SympifyError):
        print("Error: La función ingresada no es válida.")
        exit()

    # Pedir al usuario los valores de x
    X = []
    Y = []
    for i in range(3):
        while True:
            try:
                vx = float(input(f"Introduce el valor de x{i+1}: "))
                X.append(vx)
                Y.append(float(funcion.subs(x, vx)))
                break
            except ValueError:
                print("Error: Por favor, introduce un número válido para x.")

    # Calculando los coeficientes de la interpolación cuadrática
    b0 = Y[0]
    b1 = (Y[1] - Y[0]) / (X[1] - X[0])
    b2 = (((Y[2] - Y[1]) / (X[2] - X[1])) - ((Y[1] - Y[0]) / (X[1] - X[0]))) / (X[2] - X[0])
    resultante= b0 + b1 * (x-X[0])+b2 * (x-X[0])*(x-X[1])

    # Mostrando la fórmula del polinomio
    print("-" * 90)
    print("La fórmula del polinomio de interpolación cuadrática es:")
    print(f"f(x) = {resultante.expand()}")
    print("-" * 90)

    # Mostrando los valores de f(x) 
    print("Los valores de f(x) son:", Y)

