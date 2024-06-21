import math
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import (standard_transformations, split_symbols, implicit_multiplication, convert_xor)

# Definir la variable simbólica x
x = symbols('x')

# Función para pedir la función y normalizarla
def pedir_funcion():
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input("Ingrese la función en términos de x: ")
        caracteres_permitidos = set('x+-**/^() ')
        if all(c.isalnum() or c in caracteres_permitidos for c in expr_str):
            try:
                expr = parse_expr(expr_str, transformations=transformations)
                exp_pol = Poly(expr, x)
                
                # Extraer los coeficientes de la ecuación
                coeficientes = exp_pol.all_coeffs()
                
                # Normalizar la ecuación para que el coeficiente de x^3 sea 1
                coef_principal = coeficientes[0]
                coeficientes_normalizados = [coef / coef_principal for coef in coeficientes]
                
                # Obtener los coeficientes a, b, c
                a, b, c = coeficientes_normalizados[1:] if len(coeficientes_normalizados) == 4 else (0, 0, 0)
                print(f"➣ Ecuación normalizada: x^3 + ({a})*x^2 + ({b})*x + ({c}) = 0\n")
                return a, b, c
            except:
                print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

# Función para calcular las raíces usando el método de Tartaglia
def calcular_tartaglia():
    print("\t\tMÉTODO DE TARTAGLIA\n")
    raiz1 = raiz2 = raiz3 = 0
    a, b, c = pedir_funcion()

    # Calcular p y q
    p = (3 * b - a**2) / 3
    q = (2 * a**3 - 9 * a * b + 27 * c) / 27

    # Calcular discriminante
    delta = (q / 2)**2 + (p / 3)**3

    print(f"➣ Valor de p: {p}\n")
    print(f"➣ Valor de q: {q}\n")
    print(f"➣ Valor del discriminante: {delta}\n")

    if math.isclose(delta, 0, abs_tol=1e-9):
        print("\tSI Δ = 0\n")
        if p == 0 and q == 0:
            # Tiene raíz triple
            raiz1 = raiz2 = raiz3 = -a / 3
            print(f"🢚 Las raíces son: [{raiz1}, {raiz2}, {raiz3}]")
            return raiz1
        if p != 0 and q != 0:
            # Tiene raíz doble
            raiz1 = raiz2 = -(3 * q / (2 * p)) - a / 3
            raiz3 = (-4 * p**2) / (9 * q) - a / 3
            print(f"🢚 Las raíces son: [{raiz1}, {raiz2}, {raiz3}]")
            return raiz1
    elif delta > 0:
        print("\tSI Δ > 0\n")
        u = math.cbrt(-q / 2 + math.sqrt(delta))
        v = math.cbrt(-q / 2 - math.sqrt(delta))
        raiz1 = u + v - a / 3

        sub_raiz2 = -(u + v) / 2 - a / 3
        sub_raiz3 = (math.sqrt(3) / 2) * (u - v)
        
        raiz2 = sub_raiz2 + sub_raiz3 * 1j
        raiz3 = sub_raiz2 - sub_raiz3 * 1j

        print(f"🢚 La raíz real es: {raiz1}")
        print(f"🢚 La primera raíz imaginaria es: {raiz2}")
        print(f"🢚 La segunda raíz imaginaria es: {raiz3}")
        return raiz1
    elif delta < 0:
        print("\tSI Δ < 0\n")
        coseno = -q / 2 / math.sqrt(-(p / 3)**3)
        theta = math.acos(coseno)
        sqrt_term = 2 * math.sqrt(-p / 3)

        raiz1 = sqrt_term * math.cos(theta / 3) - a / 3
        raiz2 = sqrt_term * math.cos((theta + 2 * math.pi) / 3) - a / 3
        raiz3 = sqrt_term * math.cos((theta + 4 * math.pi) / 3) - a / 3

        print(f"🢚 Las raíces son: [{raiz1}, {raiz2}, {raiz3}]")
        return raiz1

def main():
    calcular_tartaglia()

if __name__ == "__main__":
    main()
