import pandas as pd
from sympy import *
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor
from sympy.abc import *
import re

x = symbols('x')

def pedir_funcion(mensaje):
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input(mensaje)
        if all(c not in expr_str for c in "#$%&\"'_`~{}[]@¿¡!?°|;:<>"):
            valid_chars_pattern = re.compile(r'^[a-zA-Z0-9\s\+\-\*/\^\(\)\|\.,]*$')
            if valid_chars_pattern.match(expr_str):
                try:
                    expr = parse_expr(expr_str, transformations=transformations)
                    exp_pol = Poly(expr)
                    print(f"➣ Ecuacion: {exp_pol}\n")
                    return expr
                except:
                    print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
            else:
                print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

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


def calcular_newton_raphson():
    print("\n\t\tMETODO DE NEWTON-RAPHSON") 

    # Pedir la función principal
    func = pedir_funcion("Ingrese la función principal: ")
    f = lambdify(x, func)

    # Calcular la derivada de la función
    derivada = diff(func, x)
    g = lambdify(x, derivada)

    segunda = diff(derivada, x)
    t =lambdify(x, segunda)

    # Verificar la derivada calculada
    print(f"f(x) = {func}\n")
    print(f"f'(x) = {derivada}\n")

    xi_inicial=pedir_cifras("Ingrese el valor incial: ")
    Ea=1

    iteracion = 1

    df = pd.DataFrame(columns=["iteracion", "xi", "f(xi)", "f'(xi)", "xi+1", "Ea"])

    opcion = input("¿Desea ingresar las cifras significativas o la tolerancia directamente? (c/t): ")
    while opcion.lower() not in ['c', 't']:
        opcion = input("Opción inválida. Ingrese 'c' para cifras significativas o 't' para tolerancia: ")

    if opcion.lower() == 'c':
        cifras = pedir_cifras("Ingrese las cifras significativas: ")
        Es = 0.5 * 10 ** (2 - cifras)
    else:
        Es = pedir_cifras("Ingrese la tolerancia: ")

    convergencia=(f(xi_inicial)*t(xi_inicial))/((g(xi_inicial))**2)
    print(convergencia)

    if convergencia<1:
        while Ea > Es:    
            xi_actual = xi_inicial - (f(xi_inicial)/g(xi_inicial))
            Ea = abs(((xi_actual - xi_inicial) / xi_actual)) if opcion.lower() == 't' else abs(((xi_actual - xi_inicial) / xi_actual) * 100)

            df.loc[iteracion - 1] = [iteracion, xi_inicial, f(xi_inicial), g(xi_inicial), xi_actual, Ea]
            
            xi_inicial = xi_actual
            iteracion += 1

        print(f"Funcion: F(x)= {func} con un nivel de toleracia del {Es}%")
        print(df)
        print(f"La raíz de la ecuación es {xi_actual} con un error de {Ea}% en la {iteracion-1}° iteración")
    else:
        print("El criterio de convergencia no cumple.")

