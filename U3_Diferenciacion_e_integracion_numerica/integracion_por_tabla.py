from pedir_tabla import pedir_tabla
import numpy as np

def simpson_untercio(h, y0, y1, y2):
    return h * (y0 + 4*y1 + y2) / 3

def trapecio_simple(h, y0, y1):
    return h * (y0 + y1) / 2

def integracion_numerica(x, y):
    n = len(x)
    
    if n < 2:
        raise ValueError("Se necesitan al menos 2 puntos para realizar la integración numérica.")
    
    elif n == 2:
        # Caso base: Trapecio simple
        return [(x[0], x[1], 'Trapecio simple', trapecio_simple(x[1] - x[0], y[0], y[1]))]
    
    else:
        integracion_detalle = []
        
        for i in range(n - 1):
            h = x[i+1] - x[i]
            if i % 2 == 0:  # índice par
                if i + 2 < n:
                    resultado = simpson_untercio(h, y[i], y[i+1], y[i+2])
                    integracion_detalle.append((x[i], x[i+2], 'Simpson 1/3', resultado))
                else:
                    resultado = trapecio_simple(h, y[i], y[i+1])
                    integracion_detalle.append((x[i], x[i+1], 'Trapecio simple', resultado))
        
        return integracion_detalle

# Función principal para ejecutar el programa
def main():
    print("-"*120)
    print("Integración Numérica".center(120))
    print("-"*120)
    x_vals, y_vals = pedir_tabla()
    print("-"*120)
    detalle_integracion = integracion_numerica(x_vals, y_vals)
    suma_resultados = 0.0  # Variable para almacenar la suma de los resultados
    
    for intervalo in detalle_integracion:
        inicio, fin, metodo, resultado = intervalo
        suma_resultados += resultado
        print(f"Intervalo [{inicio}, {fin}] - Método: {metodo} - Resultado: {resultado}")
    
    print("-"*120)
    print(f"Resultado de la integración: {suma_resultados}")
    print("-"*120)

# Ejecutar la función principal
if __name__ == "__main__":
    main()

