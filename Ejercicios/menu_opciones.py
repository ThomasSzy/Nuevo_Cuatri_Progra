
#Importamos funciones o documentacion de otro lado
#Import es una libreria
import os





seguir = True



while seguir:
    os.system("cls")
    print(" *** Menu de Opciones ***")
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")

    opcion = input("Ingrese Opcion: ")

    match opcion:
        case "1":
            print("Hola")

        case "2":
            print("Chin Chin")

        case "3":
            print("Chau nos vemos")
        
        case "4":
            seguir = False

    os.system("Pause")