import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor

x = sp.symbols('x')

def pedir_funcion():
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    caracteres_permitidos = set('x+-**/^() ')
    while True:
        expr_str = input("Ingrese la función en términos de x: ")
        if all(c.isalnum() or c in caracteres_permitidos for c in expr_str):
            try:
                expr = sp.parse_expr(expr_str, transformations=transformations)
                exp_pol = sp.Poly(expr)
                print(f"➣ Ecuacion: {exp_pol}")
                return exp_pol
            except Exception as e:
                print(f"Error: La función ingresada no es válida.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

def calcular_metodo_grafico():
    print("")
    print(f"\tMETODO GRAFICO\n")
    tiene_raices_reales = False
    while not tiene_raices_reales:
       
        f_x = pedir_funcion()

        roots = sp.solve(f_x, x)

        # Filtrar raíces reales e imaginarias
        real_roots = [root.evalf() for root in roots if root.is_real]
        imaginary_roots = [root.evalf() for root in roots if not root.is_real]

        if real_roots:
            tiene_raices_reales = True
        else:
            print("La función no tiene raíces reales. Por favor, ingrese otra función.")

    if imaginary_roots:
        print("La función también tiene raíces imaginarias.")

    # Determinar dominio para graficar
    dominio = sp.calculus.util.continuous_domain(f_x, x, sp.S.Reals)
    if dominio.start.is_infinite and dominio.end.is_infinite:
        x_vals = np.linspace(float(real_roots[0] - 10), float(real_roots[-1] + 10), 1000)
    else:
        x_start = float(dominio.start) if dominio.start.is_finite else float(real_roots[0] - 10)
        x_end = float(dominio.end) if dominio.end.is_finite else float(real_roots[-1] + 10)
        x_vals = np.linspace(x_start, x_end, 1000)

    y_vals = [f_x.subs(x, x_val).evalf() for x_val in x_vals]

    # Graficar la función y las raíces
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"${sp.latex(f_x)}$", color="blue")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, which='both')

    for i, root in enumerate(real_roots):
        ax.scatter(root, 0, color="red", label=f"Raíz {i+1}: {root}")

    ax.set_title("Método Gráfico")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    plt.show()

def main():
    calcular_metodo_grafico()

if __name__ == "__main__":
    main()