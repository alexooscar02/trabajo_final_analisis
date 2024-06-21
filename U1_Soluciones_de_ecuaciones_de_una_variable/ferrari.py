import sympy as sp
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication,convert_xor
import math
from sympy import symbols
from sympy import Poly

x = symbols("x")

def tartaglia1(a, b, c):

    # Inicializar las raíces
    raiz1 = raiz2 = raiz3 = 0
    
    # Calcular p y q
    p = (3 * b - a**2) / 3
    q = (2 * a**3 - 9 * a * b + 27 * c) / 27

    # Calcular el discriminante
    delta = (q / 2) ** 2 + (p / 3) ** 3

    print(f"➣ Valor de p: {p}\n")
    print(f"➣ Valor de q: {q}\n")
    print(f"➣ Valor del discriminante: {delta}\n")

    if math.isclose(delta, 0, abs_tol=1e-9):
        print("\tSI Δ = 0\n")
        if p == 0 and q == 0:
            # Tiene raíz triple
            raiz1 = raiz2 = raiz3 = -a / 3
            print(f"🢂 Las raíces son: [{raiz1}, {raiz2}, {raiz3}]")
            return raiz1
        if p != 0 and q != 0:
            # Tiene raíz doble
            raiz1 = raiz2 = -(3 * q / (2 * p)) - a / 3
            raiz3 = -4 * p**2 / (9 * q) - a / 3
            print(f"🢂 Las raíces son: [{raiz1}, {raiz2}, {raiz3}]")
            return raiz1
    elif delta > 0:
        print("\tSI Δ > 0\n")
        u = math.cbrt(-q / 2 + math.sqrt(delta))
        v = math.cbrt(-q / 2 - math.sqrt(delta))
        raiz1 = u + v - a / 3

        sub_raiz2 = -(u + v) / 2 - a / 3
        sub_raiz3 = (math.sqrt(3) / 2) * (u - v)

        raiz2 = sub_raiz2 + sub_raiz3 * 1j
        raiz3 = sub_raiz2 - sub_raiz3 * 1j

        print(f"🢂 La raíz real es: {raiz1}")
        print(f"🢂 La primera raíz imaginaria es: {raiz2}")
        print(f"🢂 La segunda raíz imaginaria es: {raiz3}")
        return raiz1
    elif delta < 0:
        print("\tSI Δ < 0\n")
        cos_theta = -q / 2 / math.sqrt(-(p / 3) ** 3)
        theta = math.acos(cos_theta)

        sqrt_term = 2 * math.sqrt(-p / 3)

        raiz1 = sqrt_term * math.cos(theta / 3) - a / 3
        raiz2 = sqrt_term * math.cos((theta + 2 * math.pi) / 3) - a / 3
        raiz3 = sqrt_term * math.cos((theta + 4 * math.pi) / 3) - a / 3

        print(f"🢂 Las raíces son: [{raiz1}, {raiz2}, {raiz3}]")
        return raiz1

def pedir_funcion():
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input("Ingrese la función en términos de x: ")
        caracteres_permitidos = set('x+-**/^() ')
        if all(c.isalnum() or c in caracteres_permitidos for c in expr_str):
            try:
                expr = parse_expr(expr_str, transformations=transformations)
                exp_pol = Poly(expr)
                print(f"➣ Ecuacion: {exp_pol}")
                coeficientes = exp_pol.all_coeffs()
                n, a, b, c, d = coeficientes
                print(f"➣ a:{a}, b:{b}, c:{c}, d:{d}\n")
                return a, b, c, d
            except:
                print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")


def ferrari():
    print("\t\tMETODO DE FERRARI\n")

    a,b,c,d=pedir_funcion()
    # calcular valores de p, q y R
    p = ((8 * b) - (3 * a**2)) / (8)
    q = (((8 * c) - (4 * a * b)) + (a**3)) / (8)
    R = (((256 * d) - (64 * a * c)) + ((16 * a**2) * b) - (3 * a**4)) / (256)

    print(f"El valor de p es: {p}")
    print(f"El valor de q es: {q}")
    print(f"El valor de R es: {R}\n")

    u1 = -p / 2
    u2 = -R
    u3 = ((4 * p * R) - (q**2)) / (8)

    print("U**3 - (p / 2) * U**2 - R * U + (((4 * p * R) - (q**2)) / (8))=0")
    print(f"El valor de u1 es: {u1}")
    print(f"El valor de u2 es: {u2}")
    print(f"El valor de u3 es: {u3}\n")
    
    # Esto creo que se puede hacer con sympy para que vaya cambiando la ecuacion el solo
    print(f"u^3+({u1})u^2+({u2})u+({u3})=0\n")

    # aplicamos tartaglia
    print("Aplicar Tartaglia\n")

    u = tartaglia1(u1, u2, u3)
    print(f"El valor de U es: {u}")

    # calculamos V y W
    v = sp.sqrt(2 * u - p)
    w = -((q) / (2 * v))

    print(f"El valor de v es: {v}")
    print(f"El valor de w es: {w}\n")

    raiz1 = ((v + sp.sqrt((v**2) - (4 * (u - w)))) / (2)) - (a / 4)
    raiz2 = ((v - sp.sqrt((v**2) - (4 * (u - w)))) / (2)) - (a / 4)
    raiz3 = ((-v + sp.sqrt((v**2) - (4 * (u + w)))) / (2)) - (a / 4)
    raiz4 = ((-v - sp.sqrt((v**2) - (4 * (u + w)))) / (2)) - (a / 4)

    print(f"Raices: [{raiz4}, {raiz3}, {raiz2}, {raiz1}]")


def main():
    ferrari()

if __name__ == "__main__":
    main()
