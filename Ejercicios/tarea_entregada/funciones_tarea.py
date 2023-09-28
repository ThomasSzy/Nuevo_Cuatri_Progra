#Thoma szymuda 
#Funciones!!

import os


# --------Menu--------#
def menu_tarea():
    seguir = True

    while seguir:
        os.system("cls")
        print(" *** Menu de Opciones ***")
        print("1- Perimetro del circulo")
        print("2- Numero Par o impar")
        print("3- suma de numeros")
        print("4- numero maximo de los 3")
        print("5- invertir frase/palabras")
        print("6- Orden alfabetico")
        print("7- Potencia de numero")
        print("8- invertir frase/palabras")
        print("9- invertir frase/palabras")
        print("10- invertir frase/palabras")
        print("0 si desea salir ")

        opcion = input("Ingrese Opcion: ")

        opciones_menu(opcion)


def opciones_menu(opcion) -> float:
    """Opciones_menu

    Args:
        opcion (int): El usuario ingresa un numero entero y
            printea la opcion que eligio el usuario.
    """
    match opcion:
        case "1":
            radio = float(input("Ingrese el radio del circulo:  "))
            print(calcular_perimetros_circulo(radio))
        case "2":
            numero = int(input("Ingrese un numero para saber si es par o impar"))
            print(numero_par_impar(numero))
        case "3":
            lista = [1, 2, 3, 4, 5]
            print(suma_numeros_listas(lista))
        case "4":
            numero1 = float(input("Ingrese el primero numero "))
            numero2 = float(input("Ingrese el segundo numero "))
            numero3 = float(input("Ingrese el tercer numero "))
            numero_maximo(numero1, numero2, numero3)
        case "5":
            cadena = input("Coloque la cadena que quiera invertir: ")
            cadena_invertida(cadena)
        case "6":
            palabras = ["rico", "ayudante", "hambriento", "buenas", "calle"]
            orden_alfabetico(palabras)
        case "7":
            numero_base = float(input("Ingrese el numero que desea de base  "))
            numero_exponente = int(input("Ingrese el numero que elevar  "))
            potencia_numero(numero_base, numero_exponente)
        case "8":
            lista = [1, 2, 3, 5, 6]
            numeros_pares(lista)
        case "9":
            lista_num = [1, 2, 3, 4, 5]
            suma_nuumeros(lista_num)
        case "10":
            palabra = input("Ingrese una palabra y te dira si es palindromo:    ")
            palabra_palindromo(palabra)
        case "11":
            seguir = False  # --> No me funciona porque no esta dentro de la funcion menu por eso no lo toma
            # consultar como poder realizarlo de manera correcta
    os.system("Pause")


# 1--------Calcular perimetro Circulo--------#


def calcular_perimetros_circulo(radio) -> float:
    """Calcular perimetro ciruclo

    Args:
        radio (float): con el radio colocado por el usuario
                        calculamos el perimetro del circulo.

    Returns:
        perimetro: devuelve el perimetro del circulo
    """
    perimetro = 3.14 * radio * 2

    return perimetro


# 2--------Calcular numero par o impar--------#
def numero_par_impar(numero) -> int:
    """numero_par_impar

    Args:
        numero (int): El usuario ingresa un numero entero y el programa
                    dice si el numero es % 2 es par de lo contrario
                    es impar

    Returns:
        int: printea si el numero es par o impar
    """
    if numero % 2 == 0:
        print(f"El {numero} es Par")
    else:
        print(f"El {numero} es Impar")


# 3--------Suma de numeros ingresados--------#
def suma_numeros_listas(lista):
    suma = 0

    for numero in lista:
        suma += numero

    return suma


# 4--------Maximo de 3 numeros--------#
def numero_maximo(numero1: float, numero2: float, numero3: float) -> float:
    """numero_maximo

    Args:
        numero1 (float): verifica si el numero 1 es mayor o igual que todos
        numero2 (float): verifica si el numero 2 es mayor o igual que todos
        numero3 (float): verifica si el numero 3 es mayor o igual que todos
    """
    if numero1 >= numero2 and numero1 >= numero3:
        num_maximo = numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        num_maximo = numero2
    else:
        num_maximo = numero3

    print(f"El numero maximo es {num_maximo}")
    return num_maximo


# 5--------Cadena Invertida--------#
def cadena_invertida(cadena: str) -> str:
    """cadena_invertida

    Args:
        cadena (str): recibe una cadena por el usuario y la invierte

    Returns:
        str: devuelve la cadena invertida
    """
    # Para invertir una cadena utilizamos [::-1]
    cadena_inv = cadena[::-1]
    print("cadena", cadena_inv)

    return cadena_inv


# 6--------Orden de palabras Alfabeticamente--------#
def orden_alfabetico(palabras: str) -> str:
    """orden_alfabetico

    Args:
        palabras (str): Las palabras vienen de una lista

    Returns:
        str: retorna una variable con las palabras de la lista ordenadas alfabeticamente
    """
    ordenada = list(
        sorted(palabras)
    )  # -->Sorted ordena la lista de palabras de manera alfabetica.
    print(ordenada)

    return ordenada


# 7--------Potencia numerica--------#


def potencia_numero(numero_base: float, numero_exponente: int) -> int:
    """potencia_numero

    Args:
        numero_base (float): el usuario ingresa el numero que se base
        numero_exponente (int): el usuario ingresa el numero que va a ser de exponente
        potencia(float):Realiza la cuenta y la guarda en una variable

    Returns:
        int: devuelve el valor de la cuenta
    """
    potencia = numero_base**numero_exponente
    print(potencia)

    return potencia


# 8--------Numeros pares--------#
def numeros_pares(lista: float) -> float:
    """numeros_pares

    Args:
        lista (float):una lista ya creada con numeros

    Returns:
        float: devuelve la lista modificada solo con los numeros pares
    """
    lista_pares = []
    for numeros in lista:
        if numeros % 2 == 0:
            lista_pares.append(numeros)
    print(lista_pares)

    return lista_pares


# 9--------Suma Numeros--------#


def suma_nuumeros(lista_num: float) -> float:
    """numeros_pares

    Args:
        lista_num (float): Una lista con numeros

    Returns:
        float: devuelve la suma total de todos los numeros de la lista
    """
    suma_total = 0
    for numero in lista_num:
        suma_total += numero

    print(suma_total)
    return suma_total


# 10--------Palindromo--------#
def palabra_palindromo(palabra: str) -> str:
    """palabra_palindromo

    Args:
        palabra (str): palabra colocada por el usuario
        [::-1] verifica si es igual del revez que de origen.

    Returns:
        str: returna la palabra
    """
    if palabra == palabra[::-1]:
        print(f"La palabra es palindromo {palabra}")
    else:
        print(f"La palabra {palabra} no es palindromo")
    return palabra
