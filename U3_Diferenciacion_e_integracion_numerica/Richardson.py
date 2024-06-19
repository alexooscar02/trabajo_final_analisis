import re
from sympy import symbols, parse_expr, Poly, Add
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication, convert_xor
from sympy import lambdify
from tabulate import tabulate

e, x = symbols('e x')

# Función para solicitar y validar la función matemática ingresada
def pedir_funcion(mensaje):
    transformations = standard_transformations + (implicit_multiplication, convert_xor)
    while True:
        expr_str = input(mensaje)
        # Validar caracteres permitidos en la expresión
        if all(c not in expr_str for c in "#$%&\"'_`~{}[]@¿¡!?°|;:<>"):
            valid_chars_pattern = re.compile(r'^[a-zA-Z0-9\s\+\-\*/\^\(\)\|\.,]*$')
            if valid_chars_pattern.match(expr_str):
                try:
                    expr = parse_expr(expr_str, transformations=transformations)
                    exp_pol = Poly(expr)
                    print(f"➣ Ecuacion: {exp_pol}")
                    return expr
                except Exception as e:
                    print(f"Error: La función ingresada no es válida. Detalles: {e}")
            else:
                print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

# Función para evaluar una función simbólica en un punto dado
def Evaluar(funcion_str, valor):
    try:
        funcion_sym = parse_expr(funcion_str)
        if funcion_sym is None:
            raise ValueError("La función simbólica no pudo ser parseada correctamente.")
        f = float(funcion_sym.subs([(x, valor), (e, 2.71828182846)]))  # Se asume e como constante
        return f
    except Exception as e:
        print(f"Error evaluando la función: {e}")
        return None

# Función para derivar una función simbólica
def derivar(funcion_str, orden):
    try:
        funcion_sym = parse_expr(funcion_str)
        if funcion_sym is None:
            raise ValueError("La función simbólica no pudo ser parseada correctamente.")
        fx = funcion_sym.diff(x, orden)
        return fx
    except Exception as e:
        print(f"")
        return None

# Función para calcular el valor verdadero de la derivada
def valorVerdadero(f, x, orden):
    derivada = derivar(f, orden)
    if derivada is not None:
        return Evaluar(derivada, x)
    else:
        return None

# Función para calcular el error relativo porcentual
def Er(Vv, Va):
    if Vv == 0:
        return float('inf') if Va != 0 else 0.0
    return ((Vv - Va) / Vv) * 100

# Función para calcular diferencias finitas
def diferencias_finitas(funcion_sym, x, h, metodo, orden):
    x_sym = symbols('x')
    f = lambdify(x_sym, funcion_sym, 'numpy')  # Convertir la función simbólica a una función numérica

    if metodo == "Atras":
        if orden == "orden2":
            f_xi = f(x)
            f_xi_mens_1 = f(x - h)
            return (f_xi - f_xi_mens_1) / h
        elif orden == "orden4":
            f_xi = f(x)
            f_xi_mens_1 = f(x - h)
            f_xi_mens_2 = f(x - 2 * h)
            return (3 * f_xi - 4 * f_xi_mens_1 + f_xi_mens_2) / (2 * h)
    elif metodo == "Adelante":
        if orden == "orden2":
            f_xi = f(x)
            f_xi_mas_1 = f(x + h)
            return (f_xi_mas_1 - f_xi) / h
        elif orden == "orden4":
            f_xi = f(x)
            f_xi_mas_1 = f(x + h)
            f_xi_mas_2 = f(x + 2 * h)
            return (-f_xi_mas_2 + 4 * f_xi_mas_1 - 3 * f_xi) / (2 * h)
    elif metodo == "Centrada":
        if orden == "orden2":
            f_xi_mas_1 = f(x + h)
            f_xi_mens_1 = f(x - h)
            return (f_xi_mas_1 - f_xi_mens_1) / (2 * h)
        elif orden == "orden4":
            f_xi_mas_1 = f(x + h)
            f_xi_mas_2 = f(x + 2 * h)
            f_xi_mens_1 = f(x - h)
            f_xi_mens_2 = f(x - 2 * h)
            return (-f_xi_mas_2 + 8 * f_xi_mas_1 - 8 * f_xi_mens_1 + f_xi_mens_2) / (12 * h)
    else:
        print("Error: Método o fórmula no válidos.")
        return None

# Función para realizar la extrapolación de Richardson
def extrapolacion_richardson(f, x, h, metodo, orden, nivel):
    data = [[0.0 for _ in range(nivel + 1)] for _ in range(nivel)]
    for i in range(nivel):
        data[i][1] = diferencias_finitas(f, x, h, metodo, orden)
        data[i][0] = h
        h = 0.5 * h
        pd4 = 1
        for k in range(1, i + 1):
            pd4 = 4 * pd4
            if k >= 2:
                data[i][k + 1] = (pd4 * data[i][k] - data[i - 1][k]) / (pd4 - 1)
            else:
                data[i][k + 1] = data[i][k] + (data[i][k] - data[i - 1][k]) / (pd4 - 1)
    return data

# Función principal encapsulando el código anterior
def main_richardson():
    print("-" * 120)
    print("                        Extrapolación de Richardson")
    print("-" * 120)

    # Pedir y validar la función
    funcion_str = pedir_funcion("Ingrese la función (solo se permiten letras y caracteres matemáticos): ")

    print("-" * 120)
    h = None
    x_value = None

    # Pedir y validar el tamaño del paso h y el valor de x
    while h is None or x_value is None:
        try:
            if h is None:
                h = float(input("Ingrese el tamaño del paso h: "))
                if h <= 0:
                    print("El tamaño del paso h debe ser mayor que cero.")
                    h = None
            if x_value is None:
                x_value = float(input("Ingrese el valor de x en el que desea evaluar la derivada: "))
        except ValueError:
            print("Ingrese un valor numérico válido para h y x.")

    print("-" * 120)
    metodo = input("¿Qué diferencia finita desea utilizar?\nAtras\nAdelante\nCentrada\nDeseo: ").capitalize()

    if metodo in ["Atras", "Adelante", "Centrada"]:
        orden = input("¿Qué fórmula desea utilizar?\norden2\norden4\nDeseo: ").lower()
        if orden not in ["orden2", "orden4"]:
            print("Fórmula no válida.")
            exit(1)
    else:
        print("Método inválido.")
        exit(1)

    print("-" * 120)
    nivel = int(input("¿Qué nivel de Richardson desea calcular: "))

    # Calcular y mostrar la tabla de extrapolación de Richardson
    header = [f"Nivel {i}" for i in range(nivel + 1)]
    header[0] = "h"

    try:
        respuesta = extrapolacion_richardson(funcion_str, x_value, h, metodo, orden, nivel)
        print(tabulate(respuesta, headers=header, tablefmt="fancy_grid", floatfmt=".8f", numalign="center"))

        print("-" * 120)
        # Calcular el valor verdadero y el error porcentual si es posible
        valor_verdadero = valorVerdadero(funcion_str, x_value, 1)
        if valor_verdadero is not None:
            error_porcentual = Er(valor_verdadero, respuesta[-1][-1])
            print(f"El valor verdadero es => {valor_verdadero}")
            print(f"El Error porcentual es => {error_porcentual}")
    except Exception as e:
        print(f"Ocurrió un error durante el cálculo: {e}")

# Ejecutar la función principal si este script es ejecutado directamente
if __name__ == "__main__":
    main_richardson()
