from sympy import *

class Integracion:
    def __init__(self, a, b, funcion="", x=[], y=[]):
        self.a = sympify(a)
        self.b = sympify(b)
        self.funcion = sympify(funcion.replace("^", "**")) if funcion != "" else ""
        self.x = x
        self.y = y
        self.h = 0
        self.respuesta = {}

    def evaluar(self, valor):
        x, y, z = symbols('x y z')
        if 'x' in str(self.funcion):
            return self.funcion.subs(x, float(valor))
        elif 'y' in str(self.funcion):
            return self.funcion.subs(y, float(valor))
        elif 'z' in str(self.funcion):
            return self.funcion.subs(z, float(valor))

    def validar(self, sub):
        if self.funcion != "":
            self.x = []
            self.y = []
            self.h = (float(self.b) - float(self.a)) / sub
            self.x.append(float(self.a))
            for i in range(1, sub):
                self.x.append(float(self.x[i - 1] + self.h))
            self.x.append(float(self.b))
            for valor in self.x:
                self.y.append(float(self.evaluar(valor)))
        elif self.funcion == "" and len(self.x) > 0 and len(self.y) > 0:
            igual_espaciado = True
            h_inicial = float(self.x[1]) - float(self.x[0])
            for i in range(2, len(self.x)):
                h_actual = float(self.x[i]) - float(self.x[i - 1])
                if h_actual != h_inicial:
                    igual_espaciado = False
                    break
            if igual_espaciado:
                self.h = h_inicial
            else:
                self.h = []
                for i in range(1, len(self.x)):
                    self.h.append(float(self.x[i]) - float(self.x[i - 1]))
        else:
            return "666"

    def calcular_error(self, Va):
        if self.funcion != "":
            x = symbols('x')
            Vv = integrate(self.funcion, (x, self.a, self.b))
            self.respuesta['Valor Verdadero'] = [float(Vv)]
            Error = abs((Vv - Va) / Vv) * 100
            self.respuesta['Error'] = [float(Error)]

    def trapecio_multiple(self, sub):
        self.validar(sub)
        respuesta = 0
        if type(self.h) == float:
            for k in range(len(self.x) - 1):
                respuesta += (self.h) * ((self.y[k] + self.y[k + 1]) / 2)
        else:
            for k in range(len(self.x) - 1):
                respuesta += (float(self.h[k]) * ((float(self.y[k]) + float(self.y[k + 1])) / 2))
        try:
            self.respuesta['Aproximación'] = float(respuesta)
            self.calcular_error(self.respuesta['Aproximación'])
            self.respuesta['Aproximación'] = [self.respuesta['Aproximación']]
            return self.respuesta
        except TypeError:
            self.respuesta['Aproximación'] = [str(respuesta.expand()).replace("**", "^")]
            return self.respuesta

    def simpson1_3(self, sub):
        self.validar(sub)
        if len(self.x) % 2 == 0:
            return "N131ER"
        if type(self.h) != float:
            return "N132ER"
        suma_i = 0
        for i in range(1, len(self.y) - 1, 2):
            suma_i += self.y[i]
        suma_j = 0
        for j in range(2, len(self.y) - 2, 2):
            suma_j += self.y[j]
        respuesta = (self.h) * ((self.y[0] + (4 * suma_i) + (2 * suma_j) + self.y[-1]) / 3)
        try:
            self.respuesta['Aproximación'] = float(respuesta)
            self.calcular_error(self.respuesta['Aproximación'])
            self.respuesta['Aproximación'] = [self.respuesta['Aproximación']]
            return self.respuesta
        except TypeError:
            self.respuesta['Aproximación'] = [str(respuesta.expand()).replace("**", "^")]
            return self.respuesta

    def simpson3_8(self, sub):
        self.validar(sub)
        if (len(self.x) - 1) % 3 == 0 and self.funcion == "" and type(self.h) == float:
            respuesta = 0
            for i in range(3, len(self.x), 3):
                respuesta += (self.h) * ((self.y[i - 3] + 3 * self.y[i - 2] + 3 * self.y[i - 1] + self.y[i]) / 8)
            try:
                return float(respuesta)
            except TypeError:
                return str(respuesta.expand()).replace("**", "^")
        elif type(self.h) == float and self.funcion != "":
            respuesta = 0
            for i in range(len(self.x) - 1):
                sub = [self.y[i]]
                for j in range(3):
                    sub.append(self.evaluar(self.x[i] + ((self.h / 3) * (j + 1))))
                sub.append(self.y[i + 1])
                respuesta += (self.h) * ((sub[0] + 3 * sub[1] + 3 * sub[2] + sub[3]) / 8)
            try:
                self.respuesta['Aproximación'] = float(respuesta)
                self.calcular_error(self.respuesta['Aproximación'])
                self.respuesta['Aproximación'] = [self.respuesta['Aproximación']]
                return self.respuesta
            except TypeError:
                self.respuesta['Aproximación'] = [str(respuesta.expand()).replace("**", "^")]
                return self.respuesta
        else:
            return "500"


class Rosemberg(Integracion):
    def __init__(self, a, b, funcion, nivel=2, metodo=1):
        """
        Métodos disponibles:
            1. Trapecio Compuesto
            2. Simpson 1/3
            3. Simpson 3/8
        """
        Integracion.__init__(self, a, b, funcion)
        self.nivel = nivel
        self.metodo = metodo
        self.resultado = {}

    def calcular_error(self, Va):
        x = symbols('x')
        Vv = integrate(self.funcion, (x, self.a, self.b))
        self.resultado["Valor Verdadero"] = [float(Vv)]
        Error = abs((Vv - Va) / Vv) * 100
        self.resultado['Error'] = [float(Error)]
        print(f"Valor Verdadero: {float(Vv)}")
        print(f"Valor Aproximado: {Va}")
        print(f"Error: {float(Error)}%")

    def calcular_diferencias(self, integrales, n=2):
        bloque = []
        for i in range(len(integrales) - 1):
            I = (((4 ** (n - 1)) * integrales[i + 1]) - integrales[i]) / ((4 ** (n - 1)) - 1)
            bloque.append(I)
            print(f"Diferencia de nivel {n}: {I}")

        if len(bloque) == 1:
            self.resultado['Aproximación'] = bloque[0]
        else:
            n += 1
            self.calcular_diferencias(bloque, n)

    @property
    def rosemberg(self):
        integrales = []
        for i in range(self.nivel):
            if self.metodo == 1:
                resultado_trapecio = self.trapecio_multiple(2 ** i)
                integrales.append(float(resultado_trapecio['Aproximación'][0]))
                print(f"Nivel {i + 1} - Trapecio Compuesto: {resultado_trapecio['Aproximación'][0]}")
            elif self.metodo == 2:
                resultado_simpson1_3 = self.simpson1_3(2 ** (i + 1))
                integrales.append(float(resultado_simpson1_3['Aproximación'][0]))
                print(f"Nivel {i + 1} - Simpson 1/3: {resultado_simpson1_3['Aproximación'][0]}")
            else:
                resultado_simpson3_8 = self.simpson3_8(2 ** i)
                integrales.append(float(resultado_simpson3_8['Aproximación'][0]))
                print(f"Nivel {i + 1} - Simpson 3/8: {resultado_simpson3_8['Aproximación'][0]}")

        self.calcular_diferencias(integrales)
        self.calcular_error(self.resultado['Aproximación'])
        self.resultado['Aproximación'] = [self.resultado['Aproximación']]

        return self.resultado

# Ejemplo de uso
if __name__ == "__main__":
    a = 0  # Límite inferior
    b = 1  # Límite superior
    funcion = "exp(x**2)"  # Función a integrar
    nivel = 3  # Nivel de Rosemberg
    metodo = 1  # Método a utilizar: 1 - Trapecio Compuesto, 2 - Simpson 1/3, 3 - Simpson 3/8

    rosemberg = Rosemberg(a, b, funcion, nivel, metodo)
    resultado = rosemberg.rosemberg
    print(f"\nResultado de la Integración por el Método de Rosemberg:")
    for key, value in resultado.items():
        print(f"{key}: {value}")
