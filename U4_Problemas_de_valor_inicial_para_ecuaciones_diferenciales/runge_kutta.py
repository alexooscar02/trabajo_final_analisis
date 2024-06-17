import sympy as sp
import numpy as np

class RungeKutta4:
    def __init__(self, func, x0, y0, xf, h):
        self.func = sp.sympify(func.replace("^", "**"))  # Función a trabajar
        self.x0 = float(x0)  # Valor inicial de x
        self.y0 = float(y0)  # Valor inicial de y
        self.xf = float(xf)  # Valor final de x
        self.h = float(h)    # Paso
        self.n = int((self.xf - self.x0) / self.h)  # Número de iteraciones calculado automáticamente

    def eval_func(self, x_val, y_val):
        x, y = sp.symbols('x y')
        return float(self.func.subs({x: x_val, y: y_val}).evalf())

    def run(self):
        x_vals = [self.x0]
        y_vals = [self.y0]

        print(f"{'Iter':<10}{'x_i':<10}{'y_i':<15}{'k1':<15}{'k2':<15}{'k3':<15}{'k4':<15}{'y_(i+1)':<15}")
        print("="*100)

        for i in range(self.n):
            x_prev = x_vals[-1]
            y_prev = y_vals[-1]

            k1 = self.h * self.eval_func(x_prev, y_prev)
            k2 = self.h * self.eval_func(x_prev + self.h / 2, y_prev + k1 / 2)
            k3 = self.h * self.eval_func(x_prev + self.h / 2, y_prev + k2 / 2)
            k4 = self.h * self.eval_func(x_prev + self.h, y_prev + k3)

            y_next = y_prev + (k1 + 2*k2 + 2*k3 + k4) / 6
            x_next = x_prev + self.h

            x_vals.append(x_next)
            y_vals.append(y_next)

            print(f"{i:<10}{x_prev:<10.5f}{y_prev:<15.5f}{k1:<15.5f}{k2:<15.5f}{k3:<15.5f}{k4:<15.5f}{y_next:<15.5f}")

        print("\nResultados finales:")
        self.mostrar_tabla(x_vals, y_vals)

    def mostrar_tabla(self, x_vals, y_vals):
        print(f"{'Iter':<10}{'x_i':<10}{'y_i':<15}{'k1':<15}{'k2':<15}{'k3':<15}{'k4':<15}{'y_(i+1)':<15}")
        print("="*100)

        for i in range(self.n):
            x_prev = x_vals[i]
            y_prev = y_vals[i]

            k1 = self.h * self.eval_func(x_prev, y_prev)
            k2 = self.h * self.eval_func(x_prev + self.h / 2, y_prev + k1 / 2)
            k3 = self.h * self.eval_func(x_prev + self.h / 2, y_prev + k2 / 2)
            k4 = self.h * self.eval_func(x_prev + self.h, y_prev + k3)

            y_next = y_vals[i + 1]

            print(f"{i:<10}{x_prev:<10.5f}{y_prev:<15.5f}{k1:<15.5f}{k2:<15.5f}{k3:<15.5f}{k4:<15.5f}{y_next:<15.5f}")

# Ejemplo de uso
funcion = "y*exp(x)"  # Función a trabajar
x0 = 1
  # Valor inicial de x
y0 = 2  # Valor inicial de y
xf = 2  # Valor final de x
h = 0.1  # Paso

rk4 = RungeKutta4(funcion, x0, y0, xf, h)
rk4.run()  # Ejecuta el método RK4 y muestra la tabla de resultados
