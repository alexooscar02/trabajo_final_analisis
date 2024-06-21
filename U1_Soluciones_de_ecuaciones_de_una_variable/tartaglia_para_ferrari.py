import math
from sympy import symbols, Poly

# Definir la variable simbólica x
x = symbols("x")

# Función que implementa el método de Tartaglia
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


def main():
    print("\t\tMÉTODO DE TARTAGLIA\n")

    # Ecuación a trabajar
    expr = 3 * x**3 + 4 * x**2 - 12 * x - 4  # Cambia esto a la ecuación que deseas
    exp_pol = Poly(expr, x)
    print(f"➣ Ecuación: {exp_pol}")

    coeficientes = exp_pol.all_coeffs()
    coef_principal = coeficientes[0]
    
    # Normalizar los coeficientes
    coeficientes_normalizados = [coef / coef_principal for coef in coeficientes]
    
    # Extraer los coeficientes normalizados a, b, c
    a, b, c = coeficientes_normalizados[1:]
    print(f"➣ Ecuación normalizada: x^3 + ({a})*x^2 + ({b})*x + ({c}) = 0\n")

    tartaglia1(a, b, c)


if __name__ == "__main__":
    main()
