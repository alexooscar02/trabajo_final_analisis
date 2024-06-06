import pandas as pd
from math import e
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


def calcular_biseccion():
    Es = 0.5 * 10 ** (2 - 3)
    iteracion = 1
    df = pd.DataFrame(
        columns=[
            "iteracion",
            "xa",
            "xb",
            "xr",
            "f(xa)",
            "f(xb)",
            "f(xr)",
            "f(xa)*f(xr)",
            "condicion",
            "Ea",
        ]
    )

    f = pedir_funcion()
    a = pedir_cifras("Ingrese el valor de a: ")
    b = pedir_cifras("Ingrese el valor de b: ")

    opcion = input(
        "¿Deseas ingresar las cifras significativas o la tolerancia directamente? (c/t): "
    )
    while opcion.lower() not in ["c", "t"]:
        opcion = input(
            "Opción inválida. Ingresa 'c' para cifras significativas o 't' para tolerancia: "
        )

    if opcion.lower() == "c":
        cifras = pedir_cifras("Ingrese las cifras significativas: ")
        Es = 0.5 * 10 ** (2 - cifras)
    else:
        Es = pedir_cifras("Ingrese la tolerancia: ")

    Ea = 1
    x_anterior = None

    if f.subs("x", a) * f.subs("x", b) < 0:
        while True:
            xr = (a + b) / 2

            if x_anterior is not None:
                Ea = abs(((xr - x_anterior) / xr) * 100)

            if f.subs("x", xr) * f.subs("x", a) < 0:
                b = xr
            else:
                a = xr

            df.loc[iteracion - 1] = [
                iteracion,
                a,
                b,
                xr,
                f.subs("x", a),
                f.subs("x", b),
                f.subs("x", xr),
                f.subs("x", a) * f.subs("x", xr),
                "< 0" if f.subs("x", a) * f.subs("x", xr) < 0 else " > 0",
                Ea,
            ]
            x_anterior = xr

            if Ea <= Es:
                break

            iteracion += 1
    else:
        print("El método de bisección no se pudo realizar")

    print(df)
    print(
        "La raiz de la ecuacion es ",
        xr,
        "con un error de ",
        Ea,
        "% en la",
        iteracion,
        "° iteracion",
    )


calcular_biseccion()
