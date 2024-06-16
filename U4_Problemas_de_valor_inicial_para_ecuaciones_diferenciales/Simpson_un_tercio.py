import math
from tabulate import tabulate
from pedir_funcion import pedir_funcion

# Función para el método de Simpson simple
def Simpson_simple(f, a, b):
    h = (b - a) / 2
    X0 = a
    X1 = a + h
    X2 = b
    
    integral = (h / 3) * (f(X0) + 4 * f(X1) + f(X2))
    
    return integral

# Función para el método de Simpson compuesto
def Simpson_compuesto(f, a, b, n):
    if n <= 0:
        print("Advertencia: El número de subintervalos 'n' debe ser positivo para usar Simpson compuesto.")
        return None
    
    h = (b - a) / n
    suma_impares = sum(f(a + i * h) for i in range(1, n, 2))  # Suma de f(x1), f(x3), ..., f(x_{n-1})
    suma_pares = sum(f(a + i * h) for i in range(2, n, 2))   # Suma de f(x2), f(x4), ..., f(x_{n-2})
    
    integral = (b - a) * (f(a) + 4 * suma_impares + 2 * suma_pares + f(b)) / (6 * n)
    
    return integral

# Función para generar y mostrar la tabla de resultados para Simpson compuesto
def generar_tabla_resultados_compuesto(f, a, b, n):
    resultados = []
    
    for i in range(1, n+1):
        h = (b - a) / i
        puntos_medios = [(a + j * h + (a + (j + 1) * h)) / 2 for j in range(i)]
        resultado_compuesto = Simpson_compuesto(f, a, b, i)
        resultados.append([i, puntos_medios, resultado_compuesto])
    
    # Imprimir la tabla usando tabulate
    headers = ["n", "Puntos Medios", "Integral (Simpson Compuesto)"]
    tabla = tabulate(resultados, headers=headers, tablefmt="fancy_grid", numalign="center", stralign="center", floatfmt=".6f")
    
    print("-" *120)
    print("Tabla de resultados para Simpson Compuesto".center(120))
    print(tabla.center(120))
    print("-" * 120)

# Función para calcular la integral según la elección del usuario (simple o compuesto)
def calcular_integral(f, a, b):
    while True:
        metodo = input("¿Qué método desea usar para calcular la integral? (simple/compuesto): ").strip().lower()
        if metodo == "simple":
            resultado_simple = Simpson_simple(f, a, b)
            print("-" * 120)
            print("Resultado usando Simpson Simple:")
            print(f"Integral aproximada: {resultado_simple:.6f}")
            print("-" *120)
            return resultado_simple  # Retornar el resultado de la integral simple
        elif metodo == "compuesto":
            while True:
                try:
                    n = int(input("Ingrese el número de intervalos para Simpson Compuesto (debe ser un número positivo): "))
                    if n <= 0:
                        raise ValueError("El número de intervalos debe ser un número positivo.")
                    break
                except ValueError as ve:
                    print(ve)
            
            generar_tabla_resultados_compuesto(f, a, b, n)
            resultado_compuesto = Simpson_compuesto(f, a, b, n)
            print("-" *120)
            print(f"Resultado usando Simpson Compuesto con {n} subintervalos:")
            print(f"Integral aproximada: {resultado_compuesto:.6f}")
            print("-" * 120)
            return resultado_compuesto  # Retornar el resultado de la integral compuesta
        else:
            print("Por favor, ingrese 'simple' o 'compuesto'.")

# Función principal para ejecutar el programa
def main():
    print("-" * 120)
    print("Métodos de Simpson: Simple y Compuesto".center(120))
    print("-" * 120)

    # Pedir y evaluar la función usando la función pedir_funcion importada
    funcion_str = pedir_funcion()
    try:
        f = eval("lambda x: " + funcion_str)
    except Exception as e:
        print("Error al definir la función:", e)
        return

    print("-" * 120)

    # Pedir los intervalos para la integral
    while True:
        try:
            a = float(input("Ingrese el valor del intervalo a: "))
            b = float(input("Ingrese el valor del intervalo b: "))
            break
        except ValueError:
            print("Ingrese un valor numérico válido para a y b.")

    # Calcular e imprimir el resultado de la integral según la elección del usuario
    resultado_integral = calcular_integral(f, a, b)
    print(f"Resultado final de la integral: {resultado_integral:.6f}")  # Mostrar el resultado final

if __name__ == "__main__":
    main()
