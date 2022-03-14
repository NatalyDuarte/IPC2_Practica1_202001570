from ListaCola import ListaCola
import re

def Inicio():
    global cola 
    cola= ListaCola()
    opcion = 0
    while True:
        print("================= PIZZAS ==================")
        print("|1. Ingresar datos del cliente            |")
        print("|2. Cantidad de pizza y su ingrediente    |")
        print("|3. Ingresar orden                        |")
        print("|4. Mostrar cola de ordenes               |")
        print("|5. Entregar orden                        |")
        print("|6. Salir                                 |")
        print("===========================================")
        print("Ingrese Opcion:")
        opcion = int(input(">. "))
        Menu(opcion)
        print("\n")
        if (opcion >= 1 and opcion <= 6):
            break

def Menu(opcion):
    if opcion == 1:
        global nombre
        global nit 
        global dire
        print("Ingrese el nombre del cliente")
        nombre = input(">. ")
        print("Ingrese el NIT del cliente")
        nit = input(">. ")
        print("Ingrese la dirección del cliente")
        dire = input(">. ")
        Inicio()
    elif opcion == 2:
        global ingredientes 
        global cantidad 
        print("=============== INGREDIENTES DE PIZZAS ==============")
        print("|1. Pepperoni                                       |")
        print("|2. Salchica                                        |")
        print("|3. Carne                                           |")
        print("|4. Queso                                           |")
        print("|5. Piña                                            |")
        print("=====================================================")
        print("Ingrese los ingredientes que desea, utilice comas para separar cada ingrediente")
        ingredientes= input(">. ")
        print("Ingrese la cantidad de pizzas que desea (con números)")
        cantidad=int(input(">. "))
        Inicio()
    elif opcion == 3:
        global tiempo
        tiempo = 0
        ingredientes = ingredientes.replace('"','' )
        ingre= ingredientes.split(",")
        for m in range(0, len(ingre)):
            if ingre[m]=="Pepperoni" or ingre[m]=="pepperoni":
                tiempo= tiempo +3
            elif ingre[m]=="Salchica" or ingre[m]=="salchica":
                tiempo= tiempo +4
            elif ingre[m]=="Carne" or ingre[m]=="carne":
                tiempo= tiempo +10
            elif ingre[m]=="Queso" or ingre[m]=="queso":
                tiempo= tiempo +5
            elif ingre[m]=="Piña" or ingre[m]=="piña":
                tiempo= tiempo +2
            else: 
                print("Ese ingrediente no existe en nuestro menu")
        tiempo= tiempo * int(cantidad)
        cola.insertar(nombre, nit, dire, ingredientes, tiempo)
        Inicio()
    elif opcion == 4:
        cola.imprimir()
        Inicio()
    elif opcion == 5:
        cola.eliminar()
        Inicio()
    elif opcion == 6:
        opcion = 7
        print("\n=== ¡HASTA PRONTO! ====")
    else:
        print("\n====¡OPCION NO EXISTENTE!====")

# Inicio de ejecucion
if __name__ == '__main__':
    Inicio()