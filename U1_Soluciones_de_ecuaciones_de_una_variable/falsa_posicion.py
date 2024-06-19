import pandas as pd
import sympy as sp
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import (
    standard_transformations,
    split_symbols,
    implicit_multiplication,
    convert_xor,
)

x = symbols("x")

def pedir_funcion():
    transformations = standard_transformations + (
        split_symbols,
        implicit_multiplication,
        convert_xor,
    )
    caracteres_permitidos = set("x+-**/^() ")
    while True:
        expr_str = input("Ingrese la función en términos de x: ")
        if all(c.isalnum() or c in caracteres_permitidos for c in expr_str):
            try:
                expr = parse_expr(expr_str, transformations=transformations)
                exp_pol = Poly(expr)
                print(f"➣ Ecuacion: {exp_pol}")
                return expr
            except Exception as e:
                print(f"Error: La función ingresada no es válida.")
        else:
            print(
                "Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo."
            )

def pedir_cifras(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip():
            try:
                numero = sp.sympify(valor)
                if numero.is_real:
                    return float(numero)
                else:
                    print("Error: Ingresa un número real válido.")
            except (ValueError, TypeError):
                print("Error: Ingresa un número válido.")
        else:
            print("Error: No puedes dejar este campo vacío.")

def calcular_falsa_posicion():
    print("\t\t\n METODO DE LA FALSA POSISCION")
    iteracion = 1
    df = pd.DataFrame(columns=["Iteración", "xa", "xb", "xr", "f(xa)", "f(xb)", "f(xr)", "f(xa)*f(xr)", "Condición", "Ea"])

    func = pedir_funcion()
    f = sp.lambdify(x, func)
    a = pedir_cifras("Ingrese el valor de a: ")
    b = pedir_cifras("Ingrese el valor de b: ")

    opcion = input(
        "¿Deseas ingresar las cifras significativas o la tolerancia directamente? (c/t): "
    )
    while opcion.lower() not in ["c", "t"]:
        opcion = input(
            "Opción inválida. Ingresa 'c' para cifras significativas o 't' para tolerancia: "
        )

    # Definir Es y el factor de conversión para Ea
    if opcion.lower() == "c":
        cifras = pedir_cifras("Ingrese las cifras significativas: ")
        Es = 0.5 * 10 ** (2 - cifras)
        factor_conversion = 100  # Factor de conversión para Ea en porcentaje
    else:
        Es = pedir_cifras("Ingrese la tolerancia: ")
        factor_conversion = 1  # No se convierte a porcentaje

    Ea = float('inf')  # Inicializamos con un valor grande
    x_anterior = None
    primera_iteracion = True

    # Comprobar que hay un cambio de signo en el intervalo
    if f(a) * f(b) < 0:
        while Ea > Es:
            # Calcular xr usando el método de falsa posición
            xr = (a * f(b) - b * f(a)) / (f(b) - f(a))
            
            if not primera_iteracion:
                Ea = abs(((xr - x_anterior) / xr) * factor_conversion)

            # Decidir el nuevo intervalo
            if f(xr) * f(a) < 0:
                b = xr
            else:
                a = xr

            condicion = "f(xa)*f(xr) < 0" if f(a) * f(xr) < 0 else "f(xa)*f(xr) > 0"
            
            # Registrar la iteración en el DataFrame
            df.loc[iteracion - 1] = [iteracion, a, b, xr, f(a), f(b), f(xr), f(a) * f(xr), condicion, Ea]
            
            # Actualizar el valor de xr anterior
            x_anterior = xr
            primera_iteracion = False
            iteracion += 1
    else:
        print("La función no cambia de signo en el intervalo inicial")

    # Mostrar el DataFrame y la raíz encontrada
    print(df)
    print(f"La raíz de la ecuación es {xr} con un error de {Ea}% en la {iteracion-1}° iteración")

