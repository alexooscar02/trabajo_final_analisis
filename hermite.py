import numpy as np
import pandas as pd
from sympy import symbols, diff, expand, factorial

# Función para generar la tabla de diferencias divididas para Hermite
def generate_divided_differences_table(x_vals, y_vals, derivatives):
    n = len(x_vals) * 2  # Duplicamos cada punto por el valor y la derivada
    X = np.zeros(n)
    Y = np.zeros(n)
    
    # Llenar X y Y con valores y sus derivadas
    for i in range(len(x_vals)):
        X[2 * i] = x_vals[i]
        X[2 * i + 1] = x_vals[i]
        Y[2 * i] = y_vals[i]
        Y[2 * i + 1] = y_vals[i]
    
    Q = np.zeros((n, n))
    Q[:, 0] = Y

    # Primeras diferencias divididas (considerando derivadas)
    for i in range(1, n):
        for j in range(1, i + 1):
            if X[i] == X[i - j]:
                Q[i, j] = derivatives[i // 2][0] / factorial(j)
            else:
                Q[i, j] = (Q[i, j - 1] - Q[i - 1, j - 1]) / (X[i] - X[i - j])
    
    return X, Y, Q

# Función para construir el polinomio de Hermite
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

def main_hermite():
    # Solicitar los valores de x
    x_vals = list(map(float, input("Ingrese los valores de x separados por comas: ").split(',')))
    
    # Solicitar los valores de y
    y_vals = list(map(float, input("Ingrese los valores de y correspondientes, separados por comas: ").split(',')))
    
    # Solicitar las derivadas
    derivatives = []
    for i in range(len(x_vals)):
        print(f"Ingrese las derivadas para x = {x_vals[i]}")
        derivs = list(map(float, input("Derivadas (y'): ").split(',')))
        derivatives.append(derivs)

    # Generar la tabla de diferencias divididas y el polinomio de Hermite
    X, Y, Q = generate_divided_differences_table(x_vals, y_vals, derivatives)
    hermite_poly = build_hermite_polynomial(X, Q)
    
    # Crear un DataFrame para visualizar la tabla
    df = pd.DataFrame(Q, columns=[f'Diferencia {i}' for i in range(Q.shape[1])])
    df.insert(0, 'Y', Y)
    df.insert(0, 'x', X)
    
    print("\nTabla de diferencias divididas:")
    print(df)
    
    print(f"\nEl polinomio de Hermite es: {hermite_poly}")

if __name__ == "__main__":
    main_hermite()
