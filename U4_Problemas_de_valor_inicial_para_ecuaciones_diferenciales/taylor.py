from sympy import symbols, sympify, diff
import numpy as np
from math import pow, factorial

class Taylor:
    def __init__(self, funct, xi, yi, xf, grado=2, h=0, n=0, derivadas=[]):
        self.funct = sympify(funct.replace("^", "**"))
        self.xi = sympify(xi)
        self.yi = sympify(yi)
        self.xf = sympify(xf)
        self.grado = grado
        self.h = float(h) if h else 0
        self.n = int(n) if n else 0
        self.derivadas = derivadas

    def parciales(self, funcion):
        x, y = symbols("x y")
        parcial_x = diff(funcion, x)
        parcial_x = parcial_x + y
        derivada = parcial_x.subs(y, self.funct)
        return derivada.expand()

    def eval(self, funcion, valor_x, valor_y):
        x, y = symbols("x y")
        return funcion.subs([(x, float(valor_x)), (y, float(valor_y))])

    @property
    def taylor(self):
        if self.n == 0 and self.h == 0:
            print("Error: Debes proporcionar un tamaño de paso (h) o una cantidad de puntos (n).")
            return

        if self.h == 0:
            try:
                self.h = (float(self.xf) - float(self.xi)) / self.n
            except ZeroDivisionError:
                print("Error: División por cero al calcular h.")
                return
            except TypeError:
                print("Error: Valor no numérico para n.")
                return

        if self.n == 0:
            try:
                self.n = (float(self.xf) - float(self.xi)) / self.h
            except ZeroDivisionError:
                print("Error: División por cero al calcular n.")
                return
            except TypeError:
                print("Error: Valor no numérico para h.")
                return

        try:
            x = list(np.linspace(float(self.xi), float(self.xf), int(self.n + 1)))
        except ValueError as e:
            print(f"Error: {e}")
            return

        yf = [float(self.yi)]

        fi = [self.funct]
        if len(self.derivadas) == 0:
            for i in range(self.grado):
                fi.append(self.parciales(fi[-1]))
        else:
            fi += [sympify(funct) for funct in self.derivadas]

        print("Tabla de valores:")
        print(f"{'x':<15}{'y (Taylor)':<15}")
        print(f"{x[0]:<15}{float(yf[0]):<15}")

        for i in range(1, len(x)):
            T = yf[i - 1]
            for k in range(len(fi)):
                T += (self.eval(fi[k], x[i - 1], yf[i - 1])) * (pow(self.h, k + 1) / factorial(k + 1))
            yf.append(float(T))
            print(f"{x[i]:<15}{float(T):<15}")

        print("\nResultado final:")
        print(f"x final: {x[-1]}, y final (Taylor): {float(yf[-1])}")

# Ejemplo de uso
if __name__ == "__main__":
    funcion = "x + y"  # Ejemplo de función, puedes cambiarla
    xi = 0  # Valor inicial de x
    yi = 1  # Valor inicial de y
    xf = 2  # Valor final de x
    h = 0.1  # Paso (opcional)
    n = ""  # Número de pasos (opcional)

    # Crear instancia de la clase Taylor
    taylor = Taylor(funct=funcion, xi=xi, yi=yi, xf=xf, grado=2, h=h, n=n)
    taylor.taylor  # Calcular y mostrar la tabla y el resultado final
