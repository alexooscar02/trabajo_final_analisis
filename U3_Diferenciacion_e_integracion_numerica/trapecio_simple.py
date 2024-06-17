import math

import re

def pedir_funcion():
    allowed_chars = r"[a-zA-Z\s\+\-\*/\^0-9\(\)\.,]"
    while True:
        funcion = input("Ingrese la función (solo se permiten letras y caracteres matemáticos): ")
        if re.match(allowed_chars, funcion):
            return funcion
        else:
            print("Función inválida. Por favor, inténtelo de nuevo.")


def trapecio_simple(a,b):
    integral=(b-a)*((f(a)+f(b))/2)
    return integral

print("-"*70)
print("                    Trapecio Simple")
print("-"*70)

funcion_str=pedir_funcion()
# Convertir la cadena de la función en una función de Python real
f = eval("lambda x: " + funcion_str)

#Intervalos para la integral 
a=None
b=None
while a is None or b is None:
    try:
        if a is None:
            a = float(input("Ingrese el valor del inrervalo a: "))
        if b is None:
            b = float(input("Ingrese el valor del intervalo b: "))
        else:
            break
    except ValueError:
        print("Ingrese un valor numérico válido para a y b.")

resultado=trapecio_simple(a,b)
 #Imprimiendo resultados
print("-"*70)
print("Integral a evaluar: ∫",funcion_str)
print("Intervalos de la integarl a=",a," b=",b)
print("El resultado de la inetragción es: ",resultado)
    
