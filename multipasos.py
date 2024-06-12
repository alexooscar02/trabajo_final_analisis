import sympy as sp
import numpy as np

class AdamsBashforth4:
    def __init__(self, func, x0, y0, h, xf):
        self.func = sp.sympify(func.replace("^", "**"))
        self.x0 = float(x0)
        self.y0 = float(y0)
        self.h = float(h)
        self.xf = float(xf)
        self.n = int((self.xf - self.x0) / self.h)  # Número total de pasos

    def eval_func(self, x_val, y_val):
        x, y = sp.symbols('x y')
        return float(self.func.subs({x: x_val, y: y_val}).evalf())

    def runge_kutta4_step(self, x, y):
        k1 = self.h * self.eval_func(x, y)
        k2 = self.h * self.eval_func(x + self.h / 2, y + k1 / 2)
        k3 = self.h * self.eval_func(x + self.h / 2, y + k2 / 2)
        k4 = self.h * self.eval_func(x + self.h, y + k3)
        return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    def run(self):
        x_vals = [self.x0 + i * self.h for i in range(self.n + 1)]
        y_vals = [self.y0]

        # Calculamos los primeros tres valores con Runge-Kutta de cuarto orden
        for i in range(3):
            y_next = self.runge_kutta4_step(x_vals[i], y_vals[-1])
            y_vals.append(y_next)

        # Aplicamos Adam-Bashforth de cuatro pasos
        for i in range(3, self.n):
            f1 = self.eval_func(x_vals[i], y_vals[i])
            f2 = self.eval_func(x_vals[i-1], y_vals[i-1])
            f3 = self.eval_func(x_vals[i-2], y_vals[i-2])
            f4 = self.eval_func(x_vals[i-3], y_vals[i-3])

            y_next = y_vals[i] + self.h / 24 * (55 * f1 - 59 * f2 + 37 * f3 - 9 * f4)
            y_vals.append(y_next)

        self.imprimir_tabla(x_vals, y_vals)

    def imprimir_tabla(self, x_vals, y_vals):
        print(f"{'Iter':<10}{'x_i':<10}{'y_i':<15}")
        print("="*35)

        for i, (x, y) in enumerate(zip(x_vals, y_vals)):
            print(f"{i:<10}{x:<10.5f}{y:<15.5f}")

# Ejemplo de uso
funcion = "y*ln(x)"  # Función a trabajar y' = y ln(x)
x0 = 1  # Valor inicial de x
y0 = 1  # Valor inicial de y
xf = 6  # Valor final de x
h = 0.2  # Paso

# Nota: Modificamos x0 a 1 porque ln(x) no está definido en x=0. Utilizamos un x0 cercano a 0, como x=1
ab4 = AdamsBashforth4(funcion, x0, y0, h, xf)
ab4.run()  # Ejecuta el método Adams-Bashforth y muestra la tabla de resultados
