import math
from sympy import symbols, Poly, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication,convert_xor
import cmath

x = symbols('x')

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
                n, a, b, c = coeficientes
                print(f"➣ a:{a}, b:{b}, c:{c}\n")
                return a, b, c
            except:
                print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

def calcular_tartaglia():
    print("\t\tMETODO DE TARTAGLIA\n")
    raiz1 = 0
    raiz2 = 0
    raiz3 = 0
    a, b, c = pedir_funcion()

    # calcular p y q
    p = ((3 * b) - (a**2)) / (3)
    q = ((2 * a**3) - (9 * a * b) + (27 * c)) / (27)

    # calcular discriminante
    delta = (q / 2) ** 2 + (p / 3) ** 3

    print(f"➣ valor de p:{p}\n")
    print(f"➣ valor de q:{q}\n")
    print(f"➣ valor del discriminante:{delta}\n")

    if math.isclose(delta, 0, abs_tol=1e-9):
        print("\tSI Δ = 0\n")
        if p == 0 and q == 0:
            # tiene raiz triple
            raiz1, raiz2, raiz3 = -(a / 3)
            print(f"🢚 Las raices son[{raiz1}, {raiz2}, {raiz3}]")
            return raiz1
        if p != 0 and q != 0:
            # tiene raiz doble
            raiz1 = -(3 * q / (2 * p)) - (a / 3)
            raiz2 = -(3 * q / (2 * p)) - (a / 3)
            raiz3 = ((-4 * p**2) / (9 * q)) - (a / 3)
            print(f"🢚 Las raices son: [{raiz1}, {raiz2}, {raiz3}]")
            return raiz1
    elif delta > 0:
        print("\tSI Δ > 0\n")
        raiz1 = (math.cbrt((-(q / 2)) + (math.sqrt(delta)))+ math.cbrt((-(q / 2)) - (math.sqrt(delta)))- (a / 3))

        u = math.cbrt((-(q / 2)) + (math.sqrt(delta)))
        v = math.cbrt((-(q / 2)) - (math.sqrt(delta)))
        print(f"➣ valor de u: {u}\n")
        print(f"➣ valor de v: {v}\n")
        sub_raiz2 = (-(u + v) / (2)) - (a / 3)
        sub_raiz3 = (math.sqrt(3)) / (2) * (u - v)

        raiz2 = (-(u + v) / (2)) - (a / 3) + ((math.sqrt(3)) / (2) * (u - v))
        raiz3 = (-(u + v) / (2)) - (a / 3) - ((math.sqrt(3)) / (2) * (u - v))
        print(f"🢚 La raiz real es:{raiz1}\n🢚 La primera raiz imaginaria es:{sub_raiz2}+{sub_raiz3}i\n🢚 La segunda raiz imaginaria es:{sub_raiz2}-{sub_raiz3}i\n")
        print(f"🢚 Valor aproximado de la primera raiz imaginaria:{raiz2}i\n🢚 Valor aproximado de la segunda raiz imaginaria:{raiz3}i")
        return raiz1
    elif delta < 0:
        print("\tSI Δ < 0\n")
        coseno = (-(q / 2)) / (math.sqrt(-(((p) / (3)) ** 3)))
        print(f"Valor de cos θ ={coseno}")
        theta = math.acos(coseno)
        print(f"Valor de θ = {theta}")
        valor_angulo = math.acos((-q / 2) / (-((p / 3) ** 3)) ** 1 / 2)
        raiz1 = ( (2 * math.sqrt(-p / 3)) * (math.cos((theta + 2 * 0 * math.pi) / (3)))) - (a / 3)
        raiz2 = ( (2 * math.sqrt(-p / 3)) * (math.cos((theta + 2 * 1 * math.pi) / (3)))) - (a / 3)
        raiz2 = ( (2 * math.sqrt(-p / 3)) * (math.cos((theta + 2 * 2 * math.pi) / (3)))) - (a / 3)
        print(f"🢚 Las raices son:{raiz1}, {raiz2}, {raiz3} \n")
        return raiz1


def main():
    calcular_tartaglia()


if __name__ == "__main__":
    main()
