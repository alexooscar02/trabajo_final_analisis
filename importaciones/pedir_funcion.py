import re

def pedir_funcion():
    allowed_chars = r"[a-zA-Z\s\+\-\*/\^0-9\(\)\.,]"
    while True:
        funcion = input("Ingrese la función (solo se permiten letras y caracteres matemáticos): ")
        if re.match(allowed_chars, funcion):
            return funcion
        else:
            print("Función inválida. Por favor, inténtelo de nuevo.")
