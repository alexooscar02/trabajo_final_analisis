from U1_Soluciones_de_ecuaciones_de_una_variable import bairstow
from U1_Soluciones_de_ecuaciones_de_una_variable import biseccion
from U1_Soluciones_de_ecuaciones_de_una_variable import falsa_posicion
from U1_Soluciones_de_ecuaciones_de_una_variable import punto_fijo
from U1_Soluciones_de_ecuaciones_de_una_variable import secante
from U1_Soluciones_de_ecuaciones_de_una_variable import newton_raphson
from U1_Soluciones_de_ecuaciones_de_una_variable import newton_raphson_mejorado
from U1_Soluciones_de_ecuaciones_de_una_variable import Ec_cuadraticas
from U1_Soluciones_de_ecuaciones_de_una_variable import tartaglia
from U1_Soluciones_de_ecuaciones_de_una_variable import ferrari
from U1_Soluciones_de_ecuaciones_de_una_variable import horner
from U1_Soluciones_de_ecuaciones_de_una_variable import muller
from U1_Soluciones_de_ecuaciones_de_una_variable import metodo_grafico

from U2_Interpolacion_y_aproximacion_lineal import interpolacion_Lineal
from U2_Interpolacion_y_aproximacion_lineal import interpolacion_cuadratica
from U2_Interpolacion_y_aproximacion_lineal import interpolacion_lagrange
from U2_Interpolacion_y_aproximacion_lineal import interpolacion_newton
from U2_Interpolacion_y_aproximacion_lineal import hermite
from U2_Interpolacion_y_aproximacion_lineal import Trazadores_Cubicos

from U3_Diferenciacion_e_integracion_numerica import Diferencias_finitas
from U3_Diferenciacion_e_integracion_numerica import Richardson
from U3_Diferenciacion_e_integracion_numerica import integracion_numerica
from U3_Diferenciacion_e_integracion_numerica import integracion_por_tabla
from U3_Diferenciacion_e_integracion_numerica import rosemberg
from U3_Diferenciacion_e_integracion_numerica import simpson_adaptativo
from U3_Diferenciacion_e_integracion_numerica import cuadratica_gaussiana
from U3_Diferenciacion_e_integracion_numerica import metodo_boyle

from U4_Problemas_de_valor_inicial_para_ecuaciones_diferenciales import euler
from U4_Problemas_de_valor_inicial_para_ecuaciones_diferenciales import multipasos
from U4_Problemas_de_valor_inicial_para_ecuaciones_diferenciales import runge_kutta
from U4_Problemas_de_valor_inicial_para_ecuaciones_diferenciales import taylor


def menu_metodos(unidad):
    metodos = {
        '1': ["Bairstow", "Biseccion", "Falsa Posicion", "Punto Fijo", "Secante", "Newton-Raphson", "Newton-Raphson Mejorado", "Ecuaciones Cuadraticas", "Tartaglia", "Ferrari", "Horner", "Muller", "Metodo Grafico"],
        '2': ["Interpolacion Lineal", "Interpolacion Cuadratica", "Interpolacion de LaGrange", "Interpolacion de Newton", "Hermite", "Trazadores Cubicos"],
        '3':["Diferencias Finitas", "Extrapolacion Richardson", "Integracion Numerica", "Integracion Numerica Por Tabla", "Rosemberg", "Simpson Adaptativo", "Cuadratura Gaussiana", "Boyle"],
        '4': ["Metodo de Euler", "Metodo de Taylor", "Metodo de Runge Kutta", "Metodos Multipasos"],
        '5': []  
    }

    while True:
        print(f"\nUnidad {unidad}")
        print("Selecciona un método:")
        
        for i, metodo in enumerate(metodos[unidad], 1):
            print(f"{i}. {metodo}")
        print(f"{len(metodos[unidad]) + 1}. Volver al menú principal")
        
        choice = input("Selecciona una opción: ")

        if choice.isdigit() and 1 <= int(choice) <= len(metodos[unidad]):
            metodo_seleccionado = metodos[unidad][int(choice) - 1]
            print(f"Has seleccionado el {metodo_seleccionado}")

            # Llamada al método correspondiente
            if unidad == '1':
                if choice == '1':
                    bairstow.calcular_bairstow()
                elif choice == '2':
                    biseccion.calcular_biseccion()
                elif choice == '3':
                    falsa_posicion.calcular_falsa_posicion()
                elif choice == '4':
                    punto_fijo.calcular_punto_fijo()
                elif choice == '5':
                    secante.calcular_secante()
                elif choice == '6':
                    newton_raphson.calcular_newton_raphson()
                elif choice == '7':
                    newton_raphson_mejorado.calcular_newton_raphson_mejorado()
                elif choice == '8':
                    Ec_cuadraticas.calcular_ec_cuadratica()
                elif choice == '9':
                    tartaglia.calcular_tartaglia()
                elif choice == '10':
                    ferrari.ferrari()  
                elif choice == '11':
                    horner.calcular_horner()    
                elif choice == '12':
                    muller.calcular_muller() 
                elif choice == '13':
                    metodo_grafico.calcular_metodo_grafico()
            if unidad =='2':
                if choice == '1':
                    interpolacion_Lineal.ejecutar_interpolacion_lineal() 
                elif choice == '2':
                    interpolacion_cuadratica.Interpolacion_Cuadratica()
                elif choice == '3':
                    interpolacion_lagrange.calcular_lagrange()        
                elif choice == '4':
                    interpolacion_newton.calcular_interpolacion_newton() 
                elif choice == '5':
                    hermite.main_hermite() 
                elif choice == '6':
                    Trazadores_Cubicos.main_trazadores() 
            if unidad =='3':
                if choice == '1':
                    Diferencias_finitas.main_diferencias_finitas() 
                elif choice == '2':
                    Richardson.main_richardson()
                elif choice == '3':
                    integracion_numerica.main_integracion_numerica()
                elif choice == '4':
                    integracion_por_tabla.main_por_tabla()
                elif choice == '5':
                    rosemberg.integrar_con_rosemberg()
                elif choice == '6':
                    simpson_adaptativo.main_sp_adaptativo()
                elif choice == '7':
                    cuadratica_gaussiana.main_gauss()
                elif choice == '8':
                    metodo_boyle.main_boyle()
            if unidad =='4':
                if choice == '1':
                    euler.main_euler() 
                elif choice == '2':
                    taylor.main_taylor()
                elif choice == '3':
                    runge_kutta.main_runge_kutta()
                elif choice == '4':
                    multipasos.main_multipasos()
        elif choice == str(len(metodos[unidad]) + 1):
            print(f"Volviendo al menú principal de la Unidad {unidad}")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Unidad 1")
        print("2. Unidad 2")
        print("3. Unidad 3")
        print("4. Unidad 5")
        print("14. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == '1':
            menu_metodos('1')
        elif choice == '2':
            menu_metodos('2')
        elif choice == '3':
            menu_metodos('3')
        elif choice == '4':
            menu_metodos('4')
        elif choice == '5':
            menu_metodos('5')
        elif choice == '6':
            menu_metodos('6')
        elif choice == '7':
            menu_metodos('7')
        elif choice == '8':
            menu_metodos('8')
        elif choice == '9':
            menu_metodos('9')
        elif choice == '10':
            menu_metodos('10')
        elif choice == '11':
            menu_metodos('11')
        elif choice == '12':
            menu_metodos('12')
        elif choice == '13':
            menu_metodos('13')
        elif choice == '14':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

main_menu()
