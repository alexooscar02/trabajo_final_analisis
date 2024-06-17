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

# Diferencias Divididas Hacia Atrás

# Primera Derivada
def primeraderi_formula1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        return (f_xi - f_xi_mens_1) / h
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (3 * f_xi - 4 * f_xi_mens_1 + f_xi_mens_2) / (2 * h)
    else:
        return "Fórmula no válida"

# Segunda Derivada
def segundaderi_formula1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (f_xi - 2 * f_xi_mens_1 + f_xi_mens_2) / h ** 2
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        return (2 * f_xi - 5 * f_xi_mens_1 + 4 * f_xi_mens_2 - f_xi_mens_3) / h ** 2
    else:
        return "Fórmula no válida"

# Tercera Derivada
def treceraderi_formula1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        return (f_xi - 3 * f_xi_mens_1 + 3 * f_xi_mens_2 - f_xi_mens_3) / h ** 3
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        f_xi_mens_4 = f(x - 4 * h)
        return (5 * f_xi - 18 * f_xi_mens_1 + 24 * f_xi_mens_2 - 14 * f_xi_mens_3 + 3 * f_xi_mens_4) / h ** 3
    else:
        return "Fórmula no válida"

# Cuarta derivada
def cuartaderi_formula1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        f_xi_mens_4 = f(x - 4 * h)
        return (f_xi - 4 * f_xi_mens_1 + 6 * f_xi_mens_2 - 4 * f_xi_mens_3 + f_xi_mens_4) / (2 * h ** 4)
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        f_xi_mens_4 = f(x - 4 * h)
        f_xi_mens_5 = f(x - 5 * h)
        return (3 * f_xi - 14 * f_xi_mens_1 + 26 * f_xi_mens_2 - 24 * f_xi_mens_3 + 11 * f_xi_mens_4 - 2 * f_xi_mens_5) / h ** 4
    else:
        return "Fórmula no válida"

# Diferencias finitas hacia adelante

# Primera derivada
def prideri_haciaadelante1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        return (f_xi_mas_1 - f_xi) / h
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        return (-f_xi_mas_2 - 4 * f_xi_mas_1 - 3 * f_xi) / (2 * h)
    else:
        return "Fórmula no válida"

# Segunda derivada
def seguderi_hacia_adelante1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        return (f_xi_mas_2 - 2 * f_xi_mas_1 + f_xi) / h ** 2
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        return (-f_xi_mas_3 + 4 * f_xi_mas_2 - 5 * f_xi_mas_1 + 2 * f_xi) / h ** 2
    else:
        return "Fórmula no válida"

# Tercera derivada
def tercderi_hacia_adelante1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        return (f_xi_mas_3 - 3 * f_xi_mas_2 + 3 * f_xi_mas_1 - f_xi) / h ** 3
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mas_4 = f(x + 4 * h)
        return (-3 * f_xi_mas_4 + 14 * f_xi_mas_3 - 24 * f_xi_mas_2 + 18 * f_xi_mas_1 - 5 * f_xi) / (2 * h ** 3)
    else:
        return "Fórmula no válida"

# Cuarta derivada
def cuarderi_hacia_adelante1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mas_4 = f(x + 4 * h)
        return (f_xi_mas_4 - 4 * f_xi_mas_3 + 6 * f_xi_mas_2 - 4 * f_xi_mas_1 + f_xi) / h ** 4
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mas_4 = f(x + 4 * h)
        f_xi_mas_5 = f(x + 5 * h)
        return (-2 * f_xi_mas_5 + 11 * f_xi_mas_4 - 24 * f_xi_mas_3 + 26 * f_xi_mas_2 - 14 * f_xi_mas_1 + 3 * f_xi) / h ** 4
    else:
        return "Fórmula no válida"

# Diferencias finitas centradas

# Primera Derivada
def primedi_centrada1(f, x, h, formula):
    if formula == "formula1":
        f_xi_mas_1 = f(x + h)
        f_xi_mens_1 = f(x - h)
        return (f_xi_mas_1 - f_xi_mens_1) / (2 * h)
    elif formula == "formula2":
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (-f_xi_mas_2 + 8 * f_xi_mas_1 - 8 * f_xi_mens_1 + f_xi_mens_2) / (12 * h)
    else:
        return "Fórmula no válida"

# Segunda derivada
def seguderi_centrada1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mens_1 = f(x - h)
        return (f_xi_mas_1 - 2 * f_xi + f_xi_mens_1) / h ** 2
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (-f_xi_mas_2 + 16 * f_xi_mas_1 - 30 * f_xi + 16 * f_xi_mens_1 - f_xi_mens_2) / (12 * h ** 2)
    else:
        return "Fórmula no válida"

# Tercera derivada
def terderi_centrada1(f, x, h, formula):
    if formula == "formula1":
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (f_xi_mas_2 - 2 * f_xi_mas_1 + 2 * f_xi_mens_1 - f_xi_mens_2) / (2 * h ** 3)
    elif formula == "formula2":
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        return (-f_xi_mas_3 + 8 * f_xi_mas_2 - 13 * f_xi_mas_1 + 3 * f_xi_mens_1 - 8 * f_xi_mens_2 + f_xi_mens_3) / (8 * h ** 3)
    else:
        return "Fórmula no válida"

# Cuarta derivada
def cuarderi_centrada(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (f_xi_mas_2 - 4 * f_xi_mas_1 + 6 * f_xi - 4 * f_xi_mens_1 + f_xi_mens_2) / h ** 4
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        return (-f_xi_mas_3 + 12 * f_xi_mas_2 - 39 * f_xi_mas_1 + 56 * f_xi - 39 * f_xi_mens_1 + 12 * f_xi_mens_2 - f_xi_mens_3) / (6 * h ** 4)
    else:
        return "Fórmula no válida"

# Fórmula de 3 puntos
def primtres_puntos_1(f, x, h, formula):
    if formula == "formula1":
        f_xi_mens_1 = f(x - h)
        f_xi_mas_1 = f(x + h)
        return (f_xi_mas_1 - f_xi_mens_1) / (2 * h)
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        return (-3 * f_xi + 4 * f_xi_mas_1 - f_xi_mas_2) / (2 * h)
    else:
        return "Fórmula no válida"

# Fórmula de 5 puntos
def pricinco_puntos1(f, x, h, formula):
    if formula == "formula1":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mas_4 = f(x + 4 * h)
        return (-25 * f_xi + 48 * f_xi_mas_1 + 36 * f_xi_mas_2 + 16 * f_xi_mas_3 - 3 * f_xi_mas_4) / (12 * h)
    elif formula == "formula2":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mas_3 = f(x + 3 * h)
        f_xi_mens_1 = f(x - h)
        return (-3 * f_xi_mens_1 - 10 * f_xi + 18 * f_xi_mas_1 - 6 * f_xi_mas_2 + f_xi_mas_3) / (12 * h)
    elif formula == "formula3":
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        return (f_xi_mens_2 - 8 * f_xi_mens_1 + 8 * f_xi_mas_1 - f_xi_mas_2) / (12 * h)
    elif formula == "formula4":
        f_xi = f(x)
        f_xi_mas_1 = f(x + h)
        f_xi_mas_2 = f(x + 2 * h)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        return (4 * f_xi_mens_3 + 6 * f_xi_mens_2 - 8 * f_xi_mens_1 + 34 * f_xi + 3 * f_xi_mas_1 + 34 * f_xi_mas_2) / (12 * h)
    elif formula == "formula5":
        f_xi = f(x)
        f_xi_mens_1 = f(x - h)
        f_xi_mens_2 = f(x - 2 * h)
        f_xi_mens_3 = f(x - 3 * h)
        f_xi_mens_4 = f(x - 4 * h)
        return (f_xi_mens_4 - 3 * f_xi_mens_3 + 4 * f_xi_mens_2 - 36 * f_xi_mens_1 + 25 * f_xi) / (12 * h)
    else:
        return "Fórmula no válida"
    
    
print("-"*120)
print("                                         Diferencias Finitas")
print("-"*120)
# Solicitar la función al usuario
funcion_str = pedir_funcion()
# Convertir la cadena de la función en una función de Python real
f = eval("lambda x: " + funcion_str)
print("-"*120)
h = float(input("Ingrese el tamaño del paso h: "))
x = float(input("Ingrese el valor de x en el que desea evaluar la derivada: "))
print("-"*120)
#Solicitando al usuario la derivada que desea calcular 
tipo_derivada=input("¿Que derivada desea calcular?(Ingrese el numero de la derivada)\n1-Primera derivada\n2-Segunda derivada\n3-Tercera derivada\n4-Cuarta derivada\nDeseo:")
print("-"*120)
if tipo_derivada =="1":
    metodo=input("¿Que diferencia dinita desea implementar?(Atras,Adelante,Centrada,3 Puntos,5 Puntos):")
    if metodo=="Atras":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=primeraderi_formula1(f,x,h,formula)
    elif metodo=="Adelante":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=prideri_haciaadelante1(f,x,h,formula)
    elif metodo=="Centrada":
      formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
      resultado=primedi_centrada1(f,x,h,formula)
    elif metodo=="3 Puntos":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=primtres_puntos_1(f,x,h,formula)
    elif metodo=="5 Puntos":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\tformula3\tformula4\tformula5\nDeseo:") 
        resultado=pricinco_puntos1(f,x,h,formula)
elif tipo_derivada=="2":
    if metodo=="Atras":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=segundaderi_formula1(f,x,h,formula)
    elif metodo=="Adelante":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=seguderi_hacia_adelante1(f,x,h,formula)
    elif metodo=="Centrada":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=seguderi_centrada1(f,x,h,formula)
elif tipo_derivada=="3":
    if metodo=="Atras":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=treceraderi_formula1(f,x,h,formula)
    elif metodo=="Adelante":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=tercderi_hacia_adelante1(f,x,h,formula)
    elif metodo=="Centrada":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=terderi_centrada1(f,x,h,formula)
elif tipo_derivada=="4":
    if metodo=="Atras":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=cuartaderi_formula1(f,x,h,formula)
    elif metodo=="Adelante":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=cuarderi_hacia_adelante1(f,x,h,formula)
    elif metodo=="Centrada":
        formula=input("¿Que formula desea implementar\nformula1\tformula2\nDeseo:")
        resultado=cuarderi_centrada(f,x,h,formula)
else:
    print("Derivada invalida")
print("-"*120)
print("El resultado de la Diferencia Finita es: ",resultado)