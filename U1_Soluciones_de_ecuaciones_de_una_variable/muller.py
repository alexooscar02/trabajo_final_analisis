import tabulate
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


def calcular_muller():
    print("\t\tMETODO DE MULLER\n")
    f = Function('f')(x)
    func=pedir_funcion("➔ Digite la funcion a trabajar: ")
    f=lambdify(x,func)

    x0 = pedir_cifras("➔ Digite el valor de x0: ")
    x1 = pedir_cifras("➔ Digite el valor de x1: ")
    x2 = pedir_cifras("➔ Digite el valor de x2: ")
    iteracion = 1
    Ea=1
    Es=None
    print(f"Funcion: F(x)= {func} con un nivel de toleracia del {Es}%. Con x0 = {x0}, x1 = {x1} y x2 = {x2}\n")
    df = pd.DataFrame(columns=["Iteración", "x0", "x1",  "x2", "f(x0)", "f(x1)", "f(x2)", "x3", "f(x3)", "Ea"])

    opcion = input("¿Desea ingresar las cifras significativas o la tolerancia directamente? (c/t): ")
    while opcion.lower() not in ['c', 't']:
        opcion = input("Opción inválida. Ingrese 'c' para cifras significativas o 't' para tolerancia: ")

    if opcion.lower() == 'c':
        cifras = pedir_cifras("Ingrese las cifras significativas: ")
        Es = 0.5 * 10 ** (2 - cifras)
    else:
        Es = pedir_cifras("Ingrese la tolerancia: ")

    while Ea > Es:
        #Calcular valores de h
        h0=x1-x0
        h1=x2-x1

        #Calcular valores de S
        s0=(f(x1)-f(x0))/(h0)
        s1=(f(x2)-f(x1))/(h1)

        #calcular a, b y c
        a=(s1-s0)/(h1+h0)
        b=a*h1+s1
        c=f(x2)

        #Calcular D
        D=((b**2)-4*a*c)**(1/2)

        if abs(b+D)>abs(b-D):
            x3=x2+((-2*c)/((b)+D))
        else:
            x3=x2+((-2*c)/((b)-D))
        
        Ea=abs((x3-x2)/(x3)) if opcion.lower() == 't' else abs(((x3 - x2) / x3) * 100)

        df.loc[iteracion - 1] = [iteracion, x0, x1,x2, f(x0), f(x1), f(x2), x3, f(x3), Ea]

        x0=x1
        x1=x2
        x2=x3
        iteracion+=1

    print(df)
    print(f"La raíz de la ecuación es {x3} con un error de {Ea}% en la {iteracion-1}° iteración")

def main():
    calcular_muller()
    

if __name__ == "__main__":
    main()