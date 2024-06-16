import math
from pedir_funcion import pedir_funcion

def trapecio_compuesto(a,b,n):
    h=(b-a)/n
    
    suma = 0
    for k in range(1, n):
        x_k = a + k * h
        suma += f(x_k)
    
    integral = (b - a) * ((f(a) + 2 * suma + f(b)) / (2 * n))
    return integral

print("-" * 90)
print("Trapecio compuesto".center(90))
print("-" * 90)
funcion_str=pedir_funcion()
# Convertir la cadena de la función en una función de Python real
f = eval("lambda x: " + funcion_str)
print("-"*90)
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
        
n=int(input("Ingrese el numero de intervalos que desea:"))
# Calculando los puntos de división
puntos_division = [a + i * (b - a) / n for i in range(n + 1)]

# Calculando los valores de la función en los puntos de división
valores_función = [f(x) for x in puntos_division]

print("Integral a evaluar: ∫ ",funcion_str)
print("Intervolo a=",a," Intervalo b=",b)
print("-"*65)
print("|" + " Intervalo ".center(20) + "|" + " Subintervalo ".center(20) + "|" + " Valor de la función".center(20)+"|")
print("-" * 65)
for i in range(n):
    
    intervalo = f"{puntos_division[i]:.2f}, {puntos_division[i + 1]:.2f}"
    subintervalo = f"{puntos_division[i]:.2f}, {puntos_division[i + 1]:.2f}"
    valor_funcion = f"{valores_función[i]:.15f}"
    print(f"|{intervalo.center(20)}|{subintervalo.center(20)}|{valor_funcion.center(20)}|")

resultado = trapecio_compuesto(a, b, n)
print("-"*65)
print("Resultado de la integración =", resultado)
