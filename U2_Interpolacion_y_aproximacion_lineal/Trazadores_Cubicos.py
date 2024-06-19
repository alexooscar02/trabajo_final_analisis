import numpy as np
from sympy import symbols, sympify

# Función para pedir cifras (números reales)
def pedir_cifras(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip():
            try:
                numero = sympify(valor)
                if numero.is_real:
                    return float(numero)
                else:
                    print("Error: Ingresa un número real válido.")
            except (ValueError, TypeError):
                print("Error: Ingresa un número válido.")
        else:
            print("Error: No puedes dejar este campo vacío.")

def pedir_lista_cifras(mensaje):
    while True:
        valores = input(mensaje)
        try:
            lista_valores = [float(val) for val in valores.split(',')]
            return lista_valores
        except ValueError:
            print("Error: Por favor, ingrese números válidos separados por comas.")

# Trazador Cúbico Grado Uno
def trazador_cubico_grado_uno(x, y):
    print("TRAZADORES CUBICOS, GRADO UNO")

    n = len(x)
    A = np.zeros((2*(n-1), 2*(n-1)))
    B = np.zeros(2*(n-1))
    
    ecuacion = 0
    for i in range(n - 1):
        A[ecuacion, 2*i] = x[i]
        A[ecuacion, 2*i + 1] = 1
        B[ecuacion] = y[i]
        ecuacion += 1
        
        A[ecuacion, 2*i] = x[i + 1]
        A[ecuacion, 2*i + 1] = 1
        B[ecuacion] = y[i + 1]
        ecuacion += 1
    
    coeficientes = np.linalg.solve(A, B)
    
    a = coeficientes[::2]
    b = coeficientes[1::2]
    
    for i in range(len(a)):
        print(f"s(x) = {a[i]}x + {b[i]} en el intervalo [{x[i]}, {x[i+1]}]")
    
    return a, b

# Trazador Cúbico Grado Dos
def calcular_trazador_cubico_grado_dos(x, y):
    print("\nTRAZADORES CUBICOS, GRADO DOS")

    def trazador_cuadratico(x, y):
        n = len(x)
        A = np.zeros((3*(n-1), 3*(n-1)))
        B = np.zeros(3*(n-1))
        
        ecuacion = 0
        for i in range(n - 1):
            A[ecuacion, 3*i] = x[i]**2
            A[ecuacion, 3*i + 1] = x[i]
            A[ecuacion, 3*i + 2] = 1
            B[ecuacion] = y[i]
            ecuacion += 1
            
            A[ecuacion, 3*i] = x[i + 1]**2
            A[ecuacion, 3*i + 1] = x[i + 1]
            A[ecuacion, 3*i + 2] = 1
            B[ecuacion] = y[i + 1]
            ecuacion += 1
        
        # Derivadas
        for i in range(1, n - 1):
            A[ecuacion, 3*(i-1)] = 2 * x[i]
            A[ecuacion, 3*(i-1) + 1] = 1
            A[ecuacion, 3*i] = -2 * x[i]
            A[ecuacion, 3*i + 1] = -1
            ecuacion += 1
        
        # c0 = 0
        A[ecuacion, 2] = 1
        B[ecuacion] = 0
        
        # Resolver el sistema
        coeficientes = np.linalg.solve(A, B)
        
        a = coeficientes[::3]
        b = coeficientes[1::3]
        c = coeficientes[2::3]
        
        return a, b, c

    def evaluar_trazador(x_val, x, a, b, c):
        for i in range(len(a)):
            if x[i] <= x_val <= x[i+1]:
                return a[i] * x_val**2 + b[i] * x_val + c[i]
        raise ValueError("x está fuera del rango del trazador cuadrático")

    a, b, c = trazador_cuadratico(x, y)

    for i in range(len(a)):
        print(f"s(x) = {a[i]}x^2 + {b[i]}x + {c[i]} en el intervalo [{x[i]}, {x[i+1]}]")

    return a, b, c, evaluar_trazador

# Trazador Cúbico Grado Tres
def calcular_trazador_cubico_grado_tres(x, y):
    print("TRAZADORES CUBICOS, GRADO TRES")

    def trazador_cubico(x, y):
        n = len(x)
        A = np.zeros((4*(n-1), 4*(n-1)))
        B = np.zeros(4*(n-1))
        
        ecuacion = 0
        for i in range(n - 1):
            A[ecuacion, 4*i] = x[i]**3
            A[ecuacion, 4*i + 1] = x[i]**2
            A[ecuacion, 4*i + 2] = x[i]
            A[ecuacion, 4*i + 3] = 1
            B[ecuacion] = y[i]
            ecuacion += 1
            
            A[ecuacion, 4*i] = x[i + 1]**3
            A[ecuacion, 4*i + 1] = x[i + 1]**2
            A[ecuacion, 4*i + 2] = x[i + 1]
            A[ecuacion, 4*i + 3] = 1
            B[ecuacion] = y[i + 1]
            ecuacion += 1
        
        # 1ra derivada
        for i in range(1, n - 1):
            A[ecuacion, 4*(i-1)] = 3 * x[i]**2
            A[ecuacion, 4*(i-1) + 1] = 2 * x[i]
            A[ecuacion, 4*(i-1) + 2] = 1
            A[ecuacion, 4*(i-1) + 3] = 0
            A[ecuacion, 4*i] = -3 * x[i]**2
            A[ecuacion, 4*i + 1] = -2 * x[i]
            A[ecuacion, 4*i + 2] = -1
            A[ecuacion, 4*i + 3] = 0
            ecuacion += 1
        
        # 2da derivada
        for i in range(1, n - 1):
            A[ecuacion, 4*(i-1)] = 6 * x[i]
            A[ecuacion, 4*(i-1) + 1] = 2
            A[ecuacion, 4*(i-1) + 2] = 0
            A[ecuacion, 4*(i-1) + 3] = 0
            A[ecuacion, 4*i] = -6 * x[i]
            A[ecuacion, 4*i + 1] = -2
            A[ecuacion, 4*i + 2] = 0
            A[ecuacion, 4*i + 3] = 0
            ecuacion += 1
        
        # Condiciones para extremos
        A[ecuacion, 0] = 6 * x[0]
        A[ecuacion, 1] = 2
        B[ecuacion] = 0
        ecuacion += 1
        
        A[ecuacion, -4] = 6 * x[-1]
        A[ecuacion, -3] = 2
        B[ecuacion] = 0
        
        # Resolver sistema
        coeficientes = np.linalg.solve(A, B)
        
        a = coeficientes[::4]
        b = coeficientes[1::4]
        c = coeficientes[2::4]
        d = coeficientes[3::4]
        
        return a, b, c, d

    def evaluar_trazador(x_val, x, a, b, c, d):
        for i in range(len(a)):
            if x[i] <= x_val <= x[i+1]:
                return a[i] * x_val**3 + b[i] * x_val**2 + c[i] * x_val + d[i]
        raise ValueError("x está fuera del rango del trazador cúbico")

    a, b, c, d = trazador_cubico(x, y)

    for i in range(len(a)):
        print(f"s(x) = {a[i]}x^3 + {b[i]}x^2 + {c[i]}x + {d[i]} en el intervalo [{x[i]}, {x[i+1]}]")

    return a, b, c, d, evaluar_trazador

# Función principal con menú interactivo
def main_trazadores():
    print("Trazadores Cúbicos")

    # Menú principal
    while True:
        print("\nSeleccione el Grado del Trazador Cúbico:")
        print("1. Trazador Cúbico Grado Uno")
        print("2. Trazador Cúbico Grado Dos")
        print("3. Trazador Cúbico Grado Tres")
        print("4. Salir")

        opcion_metodo = input("Ingrese el número de opción: ")

        if opcion_metodo == "1":
            x = pedir_lista_cifras("Ingrese los valores de x separados por comas: ")
            y = pedir_lista_cifras("Ingrese los valores de y separados por comas: ")
            trazador_cubico_grado_uno(x, y)

        elif opcion_metodo == "2":
            x = pedir_lista_cifras("Ingrese los valores de x separados por comas: ")
            y = pedir_lista_cifras("Ingrese los valores de y separados por comas: ")
            calcular_trazador_cubico_grado_dos(x, y)

        elif opcion_metodo == "3":
            x = pedir_lista_cifras("Ingrese los valores de x separados por comas: ")
            y = pedir_lista_cifras("Ingrese los valores de y separados por comas: ")
            calcular_trazador_cubico_grado_tres(x, y)

        elif opcion_metodo == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    main_trazadores()
