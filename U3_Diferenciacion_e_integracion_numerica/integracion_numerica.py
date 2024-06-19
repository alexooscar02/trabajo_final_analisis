import sympy
from sympy import symbols, lambdify, sympify
import re

def pedir_funcion():
    allowed_chars = r"[a-zA-Z\s\+\-\*/\^0-9\(\)\.,]"
    while True:
        funcion = input("Ingrese la función (solo se permiten letras y caracteres matemáticos): ")
        if re.match(allowed_chars, funcion):
            return funcion
        else:
            print("Función inválida. Por favor, inténtelo de nuevo.")

def pedir_intervalos():
    while True:
        try:
            a = float(input("Ingrese el valor del intervalo a: "))
            b = float(input("Ingrese el valor del intervalo b: "))
            if a == b:
                print("Los valores de a y b no deben ser iguales. Intente de nuevo.")
                continue
            return a, b
        except ValueError:
            print("Ingrese un valor numérico válido para a y b.")

# Método de Simpson 1/3
def Simpson_1_3_simple(f, a, b):
    h = (b - a) / 2
    X0 = a
    X1 = a + h
    X2 = b
    integral = (h / 3) * (f(X0) + 4 * f(X1) + f(X2))
    return integral

def Simpson_1_3_compuesto(f, a, b, n):
    if n <= 0:
        print("Advertencia: El número de subintervalos 'n' debe ser positivo para usar Simpson compuesto.")
        return None
    h = (b - a) / n
    puntos_evaluacion = [a + i * h for i in range(n+1)]
    suma_impares = sum(f(x) for i, x in enumerate(puntos_evaluacion) if i % 2 == 1)
    suma_pares = sum(f(x) for i, x in enumerate(puntos_evaluacion) if i % 2 == 0 and i != 0)
    integral = (b - a) * (f(a) + 4 * suma_impares + 2 * suma_pares + f(b)) / (6 * n)
    return integral

# Método de Simpson 3/8
def Simpson_3_8_simple(f, a, b):
    h = (b - a) / 3
    X0 = a
    X1 = (2 * a + b) / 3
    X2 = (a + 2 * b) / 3
    X3 = b
    integral = (b - a) * ((f(X0) + 3 * f(X1) + 3 * f(X2) + f(X3)) / 8)
    return integral

def Simpson_3_8_compuesto(f, a, b, n):
    if n <= 0:
        print("Advertencia: El número de subintervalos 'n' debe ser positivo para usar Simpson compuesto.")
        return None
    h = (b - a) / n
    puntos_evaluacion = [a + i * h for i in range(n+1)]
    suma_impares = sum(f(puntos_evaluacion[2*i-1]) for i in range(1, (n // 2) + 1))
    suma_pares = sum(f(puntos_evaluacion[2*i]) for i in range(1, (n // 2)))
    integral = h / 3 * (f(a) + 4 * suma_impares + 2 * suma_pares + f(b))
    return integral

# Método del Trapecio
def trapecio_simple(f, a, b):
    integral = (b - a) * ((f(a) + f(b)) / 2)
    return integral

def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    suma = 0
    for k in range(1, n):
        x_k = a + k * h
        suma += f(x_k)
    integral = (b - a) * ((f(a) + 2 * suma + f(b)) / (2 * n))
    return integral

# Función para calcular la integral
def calcular_integral(f, a, b):
    print("Seleccione el método de integración numérica:")
    print("1. Simpson 1/3 Simple")
    print("2. Simpson 1/3 Compuesto")
    print("3. Simpson 3/8 Simple")
    print("4. Simpson 3/8 Compuesto")
    print("5. Trapecio Simple")
    print("6. Trapecio Compuesto")

    while True:
        try:
            metodo = int(input("Ingrese el número del método deseado: "))
            if metodo == 1:
                resultado = Simpson_1_3_simple(f, a, b)
            elif metodo == 2:
                n = int(input("Ingrese el número de intervalos para Simpson Compuesto (debe ser un número positivo): "))
                resultado = Simpson_1_3_compuesto(f, a, b, n)
            elif metodo == 3:
                resultado = Simpson_3_8_simple(f, a, b)
            elif metodo == 4:
                n = int(input("Ingrese el número de intervalos para Simpson Compuesto (debe ser un número positivo): "))
                resultado = Simpson_3_8_compuesto(f, a, b, n)
            elif metodo == 5:
                resultado = trapecio_simple(f, a, b)
            elif metodo == 6:
                n = int(input("Ingrese el número de intervalos para el Trapecio Compuesto (debe ser un número positivo): "))
                resultado = trapecio_compuesto(f, a, b, n)
            else:
                print("Número de método no válido. Intente de nuevo.")
                continue
            
            print("-" * 70)
            print(f"Resultado de la integral con el método seleccionado:")
            print(f"Integral aproximada: {resultado:.10f}")
            print("-" * 70)
            return resultado
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

# Función principal para ejecutar el programa
def main_integracion_numerica():
    print("-" * 70)
    print("Métodos de Integración Numérica".center(70))
    print("-" * 70)

    x = symbols('x')
    funcion_str = pedir_funcion()

    try:
        expr = sympify(funcion_str)
        f = lambdify(x, expr, 'numpy')
    except Exception as e:
        print("Error al definir la función:", e)
        return

    print("-" * 70)
    a, b = pedir_intervalos()
    calcular_integral(f, a, b)

if __name__ == "__main__":
    main_integracion_numerica()
