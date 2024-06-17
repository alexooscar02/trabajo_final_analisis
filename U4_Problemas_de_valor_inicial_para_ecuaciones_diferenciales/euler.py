from sympy import symbols, sympify
import numpy as np

class Euler:
    def __init__(self, funct, xi, yi, xf, h="", n=""):
        self.funct = sympify(funct.replace("^", "**"))
        self.xi = sympify(xi)
        self.yi = sympify(yi)
        self.xf = sympify(xf)
        self.h = h
        self.n = n

    def eval(self, valorX, valorY=""):
        x, y = symbols('x y')
        if "y" not in str(self.funct):
            return self.funct.subs(x, float(valorX))
        else:
            return self.funct.subs([(x, float(valorX)), (y, float(valorY))])

    @property
    def euler(self):
        if self.h == "" and self.n == "":
            print("Error: Se necesita proporcionar ya sea el paso h o el número de pasos n.")
            return

        if self.h == "":
            self.h = (self.xf - self.xi) / self.n

        if self.n == "":
            self.n = (self.xf - self.xi) / self.h

        x = list(np.linspace(float(self.xi), float(self.xf), int(self.n + 1)))
        yf = [self.yi]

        print("Tabla de valores:")
        print(f"{'x':<15}{'y (Euler)':<15}")
        print(f"{x[0]:<15}{float(yf[0]):<15}")

        for i in range(1, len(x)):
            if "y" not in str(self.funct):
                new_y = yf[i - 1] + (self.eval(x[i - 1]) * self.h)
            else:
                new_y = yf[i - 1] + (self.eval(x[i - 1], yf[i - 1]) * self.h)
            yf.append(new_y)
            print(f"{x[i]:<15}{float(new_y):<15}")

        print("\nResultado final:")
        print(f"x final: {x[-1]}, y final (Euler): {float(yf[-1])}")

# Ejemplo de uso
if __name__ == "__main__":
    funcion = "x + y"  # Ejemplo de función, puedes cambiarla
    xi = 0  # Valor inicial de x
    yi = 1  # Valor inicial de y
    xf = 2  # Valor final de x
    h = 0.1  # Paso (opcional)
    n = ""  # Número de pasos (opcional)

    # Crear instancia de la clase Euler
    euler = Euler(funct=funcion, xi=xi, yi=yi, xf=xf, h=h, n=n)
    euler.euler  # Calcular y mostrar la tabla y el resultado final
