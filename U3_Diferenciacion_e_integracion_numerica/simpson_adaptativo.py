from sympy import sympify, symbols, lambdify, Poly, parse_expr
from math import isclose
from rich import print
from rich.tree import Tree
import re
from sympy.parsing.sympy_parser import standard_transformations, split_symbols, implicit_multiplication, convert_xor

# Función para pedir la función matemática
def pedir_funcion(mensaje):
    transformations = standard_transformations + (split_symbols, implicit_multiplication, convert_xor)
    while True:
        expr_str = input(mensaje)
        if all(c not in expr_str for c in "#$%&\"'_`~{}[]@¿¡!?°|;:<>"):
            valid_chars_pattern = re.compile(r'^[a-zA-Z0-9\s\+\-\*/\^\(\)\|\.,]*$')
            if valid_chars_pattern.match(expr_str):
                try:
                    expr = parse_expr(expr_str, transformations=transformations)
                    exp_pol = Poly(expr)
                    print(f"➣ Ecuacion: {exp_pol}\n")
                    return expr
                except:
                    print("Error: La función ingresada no es válida. Por favor, inténtalo de nuevo.")
            else:
                print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")
        else:
            print("Error: La función contiene caracteres no permitidos. Por favor, inténtalo de nuevo.")

# Función para pedir cifras (números reales)
def pedir_cifras(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip():
            try:
                numero = sympify(valor)
                if numero.is_real:
                    return float(numero)
                else:
                    print("Error: Ingresa un número real válido.")
            except (ValueError, TypeError):
                print("Error: Ingresa un número válido.")
        else:
            print("Error: No puedes dejar este campo vacío.")

# Función principal del método de Simpson adaptativo
def simpson_adaptativo(funcion, a, b, tolerancia):
    def simpson_13(f, a, b):
        """
        Calcula la aproximación de la integral de f(x) en [a, b] usando la regla de Simpson 1/3.
        """
        c = (a + b) / 2
        return (b - a) * (f(a) + 4 * f(c) + f(b)) / 6
    
    def adaptar_segmento(f, a, b, tolerancia, tree_node):
        """
        Divide el segmento [a, b] en dos y calcula la aproximación de la integral en cada subsegmento.
        """
        c = (a + b) / 2
        integral_ab = simpson_13(f, a, b)
        integral_ac = simpson_13(f, a, c)
        integral_cb = simpson_13(f, c, b)
        
        # Añadir la información del nodo al árbol
        current_node = tree_node.add(f"Calculando S({a}, {b}) = {integral_ab:.16f}")

        if abs(integral_ab - (integral_ac + integral_cb)) < 15 * tolerancia:
            current_node.add(f"resultado: {integral_ac + integral_cb:.16f}")
            return integral_ac + integral_cb
        else:
            left_result = adaptar_segmento(f, a, c, tolerancia / 2, current_node)
            right_result = adaptar_segmento(f, c, b, tolerancia / 2, current_node)
            return left_result + right_result
    
    x = symbols('x')
    f = lambdify(x, funcion)  # Convierte la expresión sympy en una función Python

    # Crear el árbol de recursión
    tree = Tree("Simpson Adaptativo", guide_style="bold bright_blue")

    resultado = adaptar_segmento(f, a, b, tolerancia, tree)
    
    # Mostrar el árbol completo
    print(tree)
    
    return resultado

def main_sp_adaptativo():
    # Solicitar la función al usuario
    funcion = pedir_funcion("Ingrese la función f(x): ")

    # Solicitar otros parámetros al usuario
    a = pedir_cifras("Ingrese el valor inicial del intervalo (a): ")
    b = pedir_cifras("Ingrese el valor final del intervalo (b): ")
    tolerancia = pedir_cifras("Ingrese la tolerancia: ")

    # Calcula la integral usando Simpson adaptativo
    resultado = simpson_adaptativo(funcion, a, b, tolerancia)
    
    # Imprime el resultado
    print(f"\nLa aproximación de la integral de la función en [{a}, {b}] es: {resultado}")

if __name__ == "__main__":
    main_sp_adaptativo()
