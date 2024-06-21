import numpy as np
import pandas as pd
from sympy import symbols, diff, lambdify, expand, cos, sin, exp, log
from sympy.parsing.sympy_parser import parse_expr
from math import factorial

def generate_divided_differences_table(f, x_vals, derivatives_count):
    x = symbols('x')
    f_expr = parse_expr(f, local_dict={'cos': cos, 'sin': sin, 'exp': exp, 'log': log, 'x': x})

    # Crear las derivadas necesarias
    f_prime = [f_expr] + [diff(f_expr, x, i) for i in range(1, derivatives_count + 1)]

    n = len(x_vals) * (derivatives_count + 1)
    X = np.repeat(x_vals, derivatives_count + 1)
    Y = np.zeros(n)

    index = 0
    for i in range(len(x_vals)):
        for j in range(derivatives_count + 1):
            if j == 0:  # Valor de la función en el punto
                Y[index] = lambdify(x, f_prime[0], modules=['numpy'])(x_vals[i])
            else:  # Derivada en el punto
                Y[index] = lambdify(x, f_prime[j], modules=['numpy'])(x_vals[i])
            index += 1

    Q = np.zeros((n, n))
    Q[:, 0] = Y

    for i in range(1, n):
        if X[i] == X[i-1]:
            Q[i, 1] = Y[i] / factorial(int(i % (derivatives_count + 1)))
        else:
            Q[i, 1] = (Q[i, 0] - Q[i-1, 0]) / (X[i] - X[i-1])

    for j in range(2, n):
        for i in range(j, n):
            if X[i] == X[i-j]:
                Q[i, j] = lambdify(x, diff(f_expr, x, j-1), modules=['numpy'])(X[i]) / factorial(j-1)
            else:
                Q[i, j] = (Q[i, j-1] - Q[i-1, j-1]) / (X[i] - X[i-j])

    return X, Y, Q

def build_hermite_polynomial(X, Q):
    coeffs = Q.diagonal()
    x = symbols('x')
    hermite_poly = coeffs[0]
    for i in range(1, len(coeffs)):
        term = coeffs[i]
        for j in range(i):
            term *= (x - X[j])
        hermite_poly += term
    return expand(hermite_poly)

def main():
    f = input("Ingrese la función f(x): ")
    x_vals = list(map(float, input("Ingrese los valores de x separados por comas: ").split(',')))
    derivatives_count = int(input("Ingrese el número máximo de derivadas: "))

    X, Y, Q = generate_divided_differences_table(f, x_vals, derivatives_count)
    hermite_poly = build_hermite_polynomial(X, Q)

    df = pd.DataFrame(Q, columns=[f'Diferencia {i}' for i in range(Q.shape[1])])
    df.insert(0, 'Y', Y)
    df.insert(0, 'x', X)

    print("\nTabla de diferencias divididas:")
    print(df)

    print(f"\nEl polinomio de Hermite es: {hermite_poly}")

if __name__ == "__main__":
    main()