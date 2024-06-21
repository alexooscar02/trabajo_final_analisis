from sympy import symbols, simplify, diff, log
import numpy as np
from sympy import sympify

def pedir_tabla_her():
    valores_x = input("Ingrese los valores de 'x' separados por comas: ")
    valores_y = input("Ingrese los valores de 'y' separados por comas: ")
    
    valores_x = np.array([float(x.strip()) for x in valores_x.split(",")])
    valores_y = np.array([sympify(y.strip()) for y in valores_y.split(",")])
    
    return valores_x, valores_y
import re

def pedir_funcion():
    allowed_chars = r"[a-zA-Z\s\+\-\*/\^0-9\(\)\.,]"
    while True:
        funcion = input("Ingrese la función (solo se permiten letras y caracteres matemáticos): ")
        if re.match(allowed_chars, funcion):
            return funcion
        else:
            print("Función inválida. Por favor, inténtelo de nuevo.")

x = symbols("x")

def hermite_dife(valores_x, valores_y, derivadas):
    n = len(valores_x)
    
    # Verificar que derivadas tiene la misma longitud que valores_x
    if len(derivadas) != n and derivadas != []:
        raise ValueError("La lista de derivadas no tiene la misma longitud que la lista de valores_x")
    
    tabla = [[0]*(2*n) for _ in range(2*n)]

    for i in range(n):
        tabla[2*i][0] = valores_y[i]
        tabla[2*i + 1][0] = valores_y[i]

    for i in range(n):
        tabla[2*i + 1][1] = derivadas[i] if derivadas else 0  # Si derivadas está vacío, asignamos cero

    for j in range(1, 2*n):
        for i in range(2*n-j):
            if j % 2 == 0:
                tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1]) / (valores_x[i//2 + j//2] - valores_x[i//2])
            else:
                tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1])
    return tabla

def Hermite(x, valores_x, tabla):
    n = len(valores_x)
    polinomio = 0
    for j in range(2*n):
        terminos = tabla[0][j]
        for i in range(j):
            terminos *= (x - valores_x[i//2])
        polinomio += terminos
    return simplify(polinomio)

def main_hermite():
    print("-"*90)
    print("                  Interpolación de Hermite  ")
    print("-"*90)
    opcion = input("¿Cómo desea realizar la interpolación? (funcion/tabla): ")
    
    if opcion.lower() == 'funcion':
        print("-"*50)
        funcion = pedir_funcion()
        valores_x = [float(x.strip()) for x in input("Ingrese los valores de 'x' separados por comas: ").split(",")]
        
        # Define X como un símbolo de SymPy
        X = symbols('X')
        
        # Evalúa la función utilizando log de SymPy
        valores_y = [log(X).subs(X, xi) for xi in valores_x]

        derivadas = []  # No se necesitan derivadas en este caso

        tabla = hermite_dife(valores_x, valores_y, derivadas)
        poli = Hermite(x, valores_x, tabla)

        print("-"*90)
        print("             Polinomio de Hermite  ")
        print("-"*90)
        print("P(x) =", poli.expand())

    elif opcion.lower() == 'tabla':
        valores_x, valores_y = pedir_tabla_her()  # Obtiene los valores de la tabla ingresada por el usuario

        # Obtén derivadas si es necesario
        derivadas = [diff(valores_y[i], x).subs(x, valores_x[i]) for i in range(len(valores_x))]

        if len(derivadas) != len(valores_x):
            raise ValueError("La lista de derivadas no tiene la misma longitud que la lista de valores_x")

        tabla = hermite_dife(valores_x, valores_y, derivadas)
        poli = Hermite(x, valores_x, tabla)

        print("-"*90)
        print("             Polinomio de Hermite  ")
        print("-"*90)
        print("P(x) =", poli)

    else:
        print("Opción no válida. Por favor, elija 'funcion' o 'tabla'.")

if __name__ == "__main__":
    main_hermite()
