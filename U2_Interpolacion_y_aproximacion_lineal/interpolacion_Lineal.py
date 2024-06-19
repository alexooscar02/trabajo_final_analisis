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

def Interpolacion_Lineal(X, Y, x_inter):
    # Encontrar los puntos cercanos
    x1 = min(X, key=lambda x: abs(x - x_inter))
    x2 = max(X, key=lambda x: abs(x - x_inter))

    # Índices de los puntos más cercanos
    id_x1 = X.index(x1)
    id_x2 = X.index(x2)

    # Calculamos la interpolación lineal
    y1 = Y[id_x1]
    y2 = Y[id_x2]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    # Interpolación en y
    y_inter = m * x_inter + b
    return y_inter, m, b

def ejecutar_interpolacion_lineal():
    # Pedir al usuario que ingrese la función
    funcion_str = pedir_funcion()
    try:
        x = sym.Symbol('x')
        funcion = sym.sympify(funcion_str)
    except (ValueError, sym.SympifyError):
        print("Error: La función ingresada no es válida.")
        return

    # Solicitar al usuario que ingrese los valores conocidos de X
    X = []
    num_valores = int(input("Ingrese la cantidad de valores conocidos de x: "))
    for i in range(num_valores):
        while True:
            x_val_input = input(f"Ingrese el valor conocido de x{i+1}: ")
            try:
                x_val = float(x_val_input)
                X.append(x_val)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número válido para x.")

    # Evaluar la función en los valores conocidos de X para obtener Y
    Y = [float(funcion.subs(x, x_val)) for x_val in X]

    # Valor que desea interpolar
    while True:
        try:
            x_inter = float(input("Ingrese el punto que desea interpolar: "))
            if x_inter < min(X) or x_inter > max(X):
                raise ValueError("El punto de interpolación está fuera del rango de los datos conocidos.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Realizar la interpolación y obtener los coeficientes
    try:
        y_inter, m, b = Interpolacion_Lineal(X, Y, x_inter)

        # Mostrar resultados
        print("-"*90)
        print("                              Interpolación lineal                   ")
        print("-"*90)
        print(f"Valor en x que desea interpolar: {x_inter}")
        print("-"*90)
        print(f"Ecuación del polinomio lineal: y = {m}x + {b}")
        print(f"Interpolación lineal en x = {x_inter}: y = {y_inter}")
    except ValueError as e:
        print(f"Error: {e}")

# Ejecutar la función principal encapsulada

