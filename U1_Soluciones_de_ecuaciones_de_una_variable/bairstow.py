import pandas as pd
import tabulate
import math
import cmath

def calcular_valores_b(a, r, s):
    n = len(a) - 1  
    b = [0] * (n + 1)  
    b[n] = a[n]  
    b[n - 1] = a[n - 1] + r * b[n]  

    for i in range(n - 2, -1, -1):
        b[i] = a[i] + r * b[i + 1] + s * b[i + 2]  

    return b

def calcular_valores_c(b, r, s):
    n = len(b) - 1  
    c = [0] * (n + 1)  
    c[n] = b[n]  
    c[n - 1] = b[n - 1] + r * c[n]  

    for i in range(n - 2, 0, -1):
        c[i] = b[i] + r * c[i + 1] + s * c[i + 2]  

    return c

def calcular_deltas(coeficientes_b, coeficientes_c):
    c1, c2, c3 = coeficientes_c[1:4]  
    b0, b1 = coeficientes_b[:2]  

    delta_r = (c3 * b0 - c2 * b1) / (c2 ** 2 - c1 * c3)
    delta_s = (c1 * b1 - c2 * b0) / (c2 ** 2 - c1 * c3)

    return delta_r, delta_s

def calcular_valores_iniciales(r,s,delta_r,delta_s):
    r=r+delta_r
    s=s+delta_s
    return r,s

def analizar_error(r,s,delta_r,delta_s):
    EDr=(abs(delta_r/r))*100
    EDs=(abs(delta_s/s))*100
    return EDr, EDs

def division_sintetica(coeficientes, a):
    n = len(coeficientes)
    n_coeficientes = [coeficientes[0]]
    b = coeficientes[0]
    
    for i in range(1, n):
        b = b * a + coeficientes[i]
        n_coeficientes.append(b)
    
    return n_coeficientes[:-1]

def cuadratica2(a,b,c):#para hallar las ultimas 2 raices
    discri=math.pow(b,2)-(4*a*c)
    raices=[]
    if discri > 0:#para raiz real
        raices.append((-b+math.sqrt(discri))/(2*a))
        raices.append((-b-math.sqrt(discri))/(2*a))
    else:# para raices complejas
        raices.append((-b-cmath.sqrt(discri))/(2*a))
        raices.append((-b+cmath.sqrt(discri))/(2*a))
    return raices

def calcular_bairstow_interna(a, r0, s0):
    Es = 0.05
    EDr = 100
    EDs = 100
    iteracion = 1

    raices_encontradas = []  # Lista para almacenar todas las raíces encontradas

    df = pd.DataFrame(columns=["Iteracion", "r", "s", "Ear", "Eas"])

    while EDr > Es and EDs > Es:

        b = calcular_valores_b(a, r0, s0)
        c = calcular_valores_c(b, r0, s0)
        delta_r, delta_s = calcular_deltas(b, c)

        r, s = calcular_valores_iniciales(r0, s0, delta_r, delta_s)
        EDr, EDs = analizar_error(r0, s0, delta_r, delta_s)

        r0 = r
        s0 = s

        df.loc[iteracion - 1] = [iteracion, r0, s0, EDr, EDs]
        iteracion += 1

    raiz_1 = ((r0 + (r0 ** 2 + 4 * s0) ** (1/2)) / 2)
    raiz_2 = ((r0 - (r0 ** 2 + 4 * s0) ** (1/2)) / 2)

    coe_nuevo = division_sintetica(list(reversed(a)), raiz_1)
    coe_nuevo2 = division_sintetica(coe_nuevo, raiz_2)

    print(f"{df}\n")
    print(f"→ Coeficientes originales (Segunda pasada): {a}")
    print(f"→ Raíces (Segunda pasada): {raiz_1}, {raiz_2}") 
    print(f"→ Coeficientes resultantes (Segunda pasada): {coe_nuevo2}\n")

    # Agregar las raíces encontradas a la lista
    if len(coe_nuevo2) >= 4:
        print("El polinomio resultante es de grado 3 o más.")
        print("Aplicando el método Bairstow nuevamente...\n")
        raices_encontradas.extend(calcular_bairstow(coe_nuevo2, r, s))
    elif len(coe_nuevo2) == 3:
        print("→ El polinomio resultante es de grado 2.")
        raices = cuadratica2(coe_nuevo2[0], coe_nuevo2[1], coe_nuevo2[2])
        raices_encontradas.extend(raices)
    elif len(coe_nuevo2) == 2:
        print("→ El polinomio resultante es de grado 1.")
        raiz = -(r / s)
        raices_encontradas.append(raiz)

    return raices_encontradas


def calcular_bairstow():
    Es = 0.05
    EDr = 100
    EDs = 100
    iteracion = 1

    r0 = 1
    s0 = 1
    a = [-78, 23, 13, -7, 1]

    df = pd.DataFrame(columns=["Iteracion", "r", "s", "Ear", "Eas"])
    raices_encontradas = []  # Lista para almacenar todas las raíces encontradas

    while EDr > Es and EDs > Es:

        b = calcular_valores_b(a, r0, s0)
        c = calcular_valores_c(b, r0, s0)
        delta_r, delta_s = calcular_deltas(b, c)

        r, s = calcular_valores_iniciales(r0, s0, delta_r, delta_s)
        EDr, EDs = analizar_error(r0, s0, delta_r, delta_s)

        r0 = r
        s0 = s

        df.loc[iteracion - 1] = [iteracion, r0, s0, EDr, EDs]
        iteracion += 1

    raiz_1 = ((r0 + (r0 ** 2 + 4 * s0) ** (1/2)) / 2)
    raiz_2 = ((r0 - (r0 ** 2 + 4 * s0) ** (1/2)) / 2)

    raices_encontradas.append(raiz_1)
    raices_encontradas.append(raiz_2)
    coe_nuevo = division_sintetica(list(reversed(a)), raiz_1)
    coe_nuevo2 = division_sintetica(coe_nuevo, raiz_2)

    print(f"{df}\n")
    print(f"→ Coeficientes originales: {a}")
    print(f"→ Raices: {raiz_1}, {raiz_2}") 
    print(f"→ Coeficientes resultantes: {coe_nuevo2}\n")

    # Agregar las raíces encontradas a la lista
    if len(coe_nuevo2) >= 4:
        print("El polinomio resultante es de grado 3 o más.")
        print("Aplicando el método Bairstow nuevamente...\n")
        raices_encontradas.extend(calcular_bairstow_interna(list(reversed(coe_nuevo2)), r0, s0))
    elif len(coe_nuevo2) == 3:
        print("→ El polinomio resultante es de grado 2.")
        raices = cuadratica2(coe_nuevo2[0], coe_nuevo2[1], coe_nuevo2[2])
        raices_encontradas.extend(raices)
        print(f"{raices}\n")
    elif len(coe_nuevo2) == 2:
        print("→ El polinomio resultante es de grado 1.")
        raiz = -r0 / s0
        raices_encontradas.append(raiz)
        print(f"{raiz}\n")

    # Mostrar todas las raíces encontradas al final
    print(f"Todas las raíces encontradas: {raices_encontradas}")

calcular_bairstow()  