import sympy as sp

# Definir símbolo x
x = sp.symbols("x")

def lagrange(xk, yk, punto):
    print("METODO DE INTERPOLACION DE LAGRANGE\n")
    lagrange_poli = 0

    # Construir el polinomio de Lagrange
    for i in range(len(xk)):
        term = yk[i]
        for j in range(len(xk)):
            if i != j:
                term *= (x - xk[j]) / (xk[i] - xk[j])
        lagrange_poli += term

    # Expandir el polinomio para una forma más simplificada
    lagrange_poli_exp = sp.expand(lagrange_poli)

    print(f"Polinomio resultante P(x) = {lagrange_poli}")
    print(f"Polinomio reducido P(x) = {lagrange_poli_exp}\n")

    # Evaluar el polinomio en el punto dado
    resultado = lagrange_poli.subs(x, punto).evalf()
    print(f"P({punto}) = {resultado}")

    return lagrange_poli_exp, resultado

def main():
    # Puntos de interpolación
    xk = [0, 0.5, 1]
    yk = [1, 1.648721271, 2.718281828]

    # Punto para evaluar el polinomio de Lagrange
    punto = 0.25  # Cambia este valor para evaluar en un punto diferente

    # Calcular el polinomio de Lagrange y evaluar en el punto
    polinomio, resultado = lagrange(xk, yk, punto)

    # Imprimir los resultados
    print("\nResultados finales:")
    print(f"Polinomio de Lagrange: {polinomio}")
    print(f"Evaluación en el punto {punto}: {resultado}")

if __name__ == "__main__":
    main()
