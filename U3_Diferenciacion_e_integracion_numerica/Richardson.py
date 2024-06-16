from pedir_funcion import pedir_funcion
import math
from tabulate import tabulate
import cmath
from numpy import *
from sympy import *


e, x=symbols('e x')
#evaluar la funcion solictada al usuario
def Evaluar(funcion_str, valor):
		funcion_str = parse_expr(funcion_str)
		f = float(funcion_str.subs([(x, valor), (e, cmath.e)]))
		return f

#derivar la funcion solicitada al usuario
def derivar(funcion_str,orden):
    funcioon = parse_expr(funcion_str)
    fx = diff(funcioon, x,orden)
    return str(fx)

def valorVerdadero(f, x,orden):
    return Evaluar(derivar(f,orden), x)

def Er(Vv, Va):
    return ((Vv - Va)/(Vv))*100




def diferencias_finitas(f, x, h, metodo, orden):
    if metodo == "Atras":
        if orden == "orden2":
            f_xi = f(x)
            f_xi_mens_1 = f(x - h)
            return (f_xi - f_xi_mens_1) / h
        elif orden == "Orden4":
            f_xi = f(x)
            f_xi_mens_1 = f(x - h)
            f_xi_mens_2 = f(x - 2 * h)
            return (3 * f_xi - 4 * f_xi_mens_1 + f_xi_mens_2) / (2 * h)
    elif metodo == "Adelante":
        if orden == "orden2":
            f_xi = f(x)
            f_xi_mas_1 = f(x + h)
            return (f_xi_mas_1 - f_xi) / h
        elif orden == "Orden4":
            f_xi = f(x)
            f_xi_mas_1 = f(x + h)
            f_xi_mas_2 = f(x + 2 * h)
            return (-f_xi_mas_2 - 4 * f_xi_mas_1 - 3 * f_xi) / (2 * h)
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
            return (-(f_xi_mas_2) + 8 * f_xi_mas_1 - 8 * f_xi_mens_1 + f_xi_mens_2) / (12 * h)
    print("Error: Método o fórmula no válidos.")
    return None  # Add this line

def extrapolacion_richardson(f, x, h, metodo, orden, nivel):
    data = [[0.0 for _ in range(nivel + 1)] for _ in range(nivel)]
    for i in range(nivel):
        data[i][1] = diferencias_finitas(f, x, h, metodo, orden)
        data[i][0] = h
        h = 0.5 * h
        pd4 = 1
        for k in range(1, i + 1):
            pd4 = 4 * pd4
            if k >= 2:  # Aplicar la fórmula específica a partir del segundo nivel
                data[i][k + 1] = (pd4 * data[i][k] - data[i - 1][k]) / (pd4 - 1)
            else:
                data[i][k + 1] = data[i][k] + (data[i][k] - data[i - 1][k]) / (pd4 - 1)
    return data


print("-"*120)
print("                        Extrapolacion de Richardson")
print("-"*120)
funcion_str=pedir_funcion()
# Convertir la cadena de la función en una función de Python real
f = eval("lambda x: " + funcion_str)
print("-"*120)
h = None
x = None

while h is None or x is None:
    try:
        if h is None:
            h = float(input("Ingrese el tamaño del paso h: "))
        if x is None:
            x = float(input("Ingrese el valor de x en el que desea evaluar la derivada: "))
        if h <= 0:
            print("El tamaño del paso h debe ser mayor que cero.")
            h = None
        else:
            break
    except ValueError:
        print("Ingrese un valor numérico válido para h y x.")

print("-" * 120)
metodo=input("¿Que diferencia finita desea utilizar.\nAtras\nAdelante\nCentrada\nDeseo:")
if metodo=="Atras":
    orden=input("¿Que formula desea utilizar?\norden2\norden4\nDeseo:")
    resultado=diferencias_finitas(f,x,h,metodo,orden)
elif metodo=="Adelante":
    orden=input("¿Que formula desea utilizar?\norden2\norden4\nDeseo:")
    resultado=diferencias_finitas(f,x,h,metodo,orden)
elif metodo=="Centrada":
    orden=input("¿Que formula desea utilizar?\norden2\norden4\nDeseo:")
    resultado=diferencias_finitas(f,x,h,metodo,orden)
else:
    print("Metodo invalido")
print("-"*120)
#Pidiendo al usuario el nivel de extrapolacion
nivel = int(input("¿Que nivel de Richardson desea calcular: "))
header = [f"Nivel {x} " for x in range(int(nivel) + 1)]
header[0] = "H1"

#Llamando al metodo
respuesta=extrapolacion_richardson(f,x,h,metodo,orden,nivel)
#Imprimiendo resultados
print(tabulate(respuesta,headers=header, tablefmt="fancy_grid", floatfmt=".8f", numalign="center"))

print("-"*120)
valorVerdadero=valorVerdadero(f,x,1)
errorPorcentual=Er(valorVerdadero,respuesta[-1][-1])
print("El valor verdadero es =>",valorVerdadero)
print("El Error porcentual es=>",errorPorcentual)




