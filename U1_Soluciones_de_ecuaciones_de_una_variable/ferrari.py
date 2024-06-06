import sympy as sp
from sympy import symbols, Poly, parse_expr
from tartaglia_para_ferrari import tartaglia1
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication,convert_xor

x = symbols("x")

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
