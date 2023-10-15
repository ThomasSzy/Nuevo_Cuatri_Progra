from data_stark import *

# Punto A y B


def super_heroe_generos(lista: list, key: str) -> str:
    """super_heroe_generos lo que realiza esta funcion es la busqueda
        de un genero y manda los nombres a la lista para poder ser printeada

    Args:
        lista (list): recibe los datos de todos los personajes
        key (str): el genero buscado

    Returns:
        str: devuelve la lista de los nombres de los personajes del genero buscado
    """
    nombres_generos = []
    for personajes in lista:
        genero = personajes["genero"]
        if genero == key:
            nombre = personajes["nombre"]
            nombres_generos.append(nombre)
    return nombres_generos


# Punto C,D,E,F,I
def valor_max(lista: list, key: str, key2: str) -> float:
    """altura_max
        Sacamos Valor maximo de la lista de personajes

    Args:
        lista (list): Colocamos una lista con los datos de los personajes
        flag: Colocamos una flag para que ingrese si o si guardando el dato
        de la altura y luego empiece a comparar con las demas alturas
        key (str): el id de lo que buscamso, en este caso "altura"
        key2 (str): el id del personaje, en esta caso "F/M"
    Returns:
        float: returna el numero maximo de la lista de alturas
    """
    numero_max = 0
    flag_valor = True

    for valor in lista:
        genero = valor["genero"]
        valor_lista = float(valor[key])
        if genero == key2:
            if valor_lista >= numero_max or flag_valor == True:
                numero_max = valor_lista
                flag_valor = False

    return numero_max


def valor_min(lista: list, key: str, key2) -> float:
    """altura_min
    Buscamos la altura minima en la lista

    Args:
        lista (list): lista con los valores de los personajes
        for: buscamos el valor altura y lo parseamos.

        if: buscamos el valor minimo y con una flag obligamos a que
        ingrese si o si un dato para ser comparado con cual es mas
        chico

        key (str): el id de lo que buscamso, en este caso "altura"
        key2 (str): el id del personaje, en esta caso "F/M"
    Returns:
        float: devuelve el valor minimo
    """
    minimo = 0
    flag_valor = True

    for valor in lista:
        genero = valor["genero"]
        valor_lista = float(valor[key])
        if genero == key2:
            if valor_lista <= minimo or flag_valor == True:
                minimo = valor_lista
                flag_valor = False
    return minimo


def nombres_valores(lista: list, key: str, funcion, key2) -> None:
    """Tomamos valores de una funcion y lo que deseamos buscar.
        y de ahi le damos el nombre del valor pedido

    Args:
        lista (list): lista de personajes
        key (str): el id de lo que buscamos, en este caso "altura"
        key2 (str): el id del personaje, en esta caso "F/M"
        funcion (float): Colocamos la funcion que queremos que realice
                        valor_min / valor_max, etc
    """
    valores = funcion(lista, key, key2)

    if valores:
        for maximo_minimo in lista:
            if float(maximo_minimo[key]) == valores:
                nombre = maximo_minimo["nombre"]
                altura_max = maximo_minimo[key]

        print(f"El personaje es {nombre} y su valor es {altura_max}")


# Punto G y H
def promedio(lista: list, key, key2) -> float:
    """promedio_altura
        buscamos la cantidad de personajes y sumamos sus estaturas
        y sacamos el promedio

    Args:
        lista (list): lista con los datos de todos los personajes

    Returns:
        float: devuelve el promedio total
        key es altura
    """

    valor_total = 0
    cantidad_unidades = 0
    for alturas in lista:
        genero = alturas["genero"]
        if genero == key2:
            valor_total += float(alturas[key])
            cantidad_unidades += 1
            promedio = valor_total / cantidad_unidades
    return promedio


# Punto J K L
def determinar_cuantos_superheroes_tipo(lista: list, key: str) -> str:
    """deterninar_cuantos_superheroes_tipo
        Esta funcion determina cuantos tipos de key hay y si tiene o no esa key
        buscada de no ser asi lo agrega con un No tiene

    Args:
        lista (list): Agregamos una lista
        key (str): la clave con la que buscamos cuantos super heroes con ese tipo hay

    Returns:
        str: retorna la cantidad y el tipo de superheroes dentro de la lista
    """
    diccionario_tipo = {}
    for superheroe in lista:
        if superheroe[key] in diccionario_tipo:
            diccionario_tipo[superheroe[key]] += 1
        else:
            if superheroe[key] == "":
                superheroe[key] = "No tiene"
            diccionario_tipo[superheroe[key]] = 1
    superheroes_de_cada_tipo = ""
    for tipo in diccionario_tipo:
        cantidad_superheroes = diccionario_tipo[tipo]
        superheroes_de_cada_tipo += (
            f"Hay {cantidad_superheroes} superheroes de tipo {key} = {tipo}\n"
        )

    return superheroes_de_cada_tipo


# Punto M N O
def agrupar_superheroes_por_valor(lista, key):
    """Listar heroes por valor

    Args:
        lista(list) Ingresamos una lista
        clave(str)

    Returns:
        list: superheroes_agrupados
        key: la clave asignada para lo que buscamos
    """
    superheroes_agrupados = {}

    for heroe in lista:
        nombre = heroe["nombre"]
        valor = heroe[key]

        if valor == "":
            valor = "No tiene"

        if valor in superheroes_agrupados:
            superheroes_agrupados[valor].append(nombre)

        else:
            superheroes_agrupados[valor] = [nombre]

    return superheroes_agrupados


# Menu
def menu_stark():
    """menu_stark: creamos la base del menu lo que el usuario ve al momento de elegir
    las opciones
    """
    seguir = True

    while seguir:
        print(" *** Menu de Opciones ***")
        print("1- Nombre de Personajes segun su genero")
        print("2- altura maxima y genero del personaje")
        print("3- altura minima y genero del personaje")
        print("4- Altura promedio segun genero")
        print("5- cantidad de color / inteligencia")
        print("6- nombres segun color / inteligencia")
        print("7 si desea salir ")

        opcion = input("Ingrese Opcion: ")
        if opcion == "7":
            seguir = False
        opciones_menu(opcion)


def opciones_menu(opcion) -> float:
    """Opciones_menu

    Args:
        opcion (int): El usuario ingresa un numero entero y
            printea la opcion que eligio el usuario.
    """
    match opcion:
        case "1":
            nombre = input("Ingrese Genero F/M: ")
            print(super_heroe_generos(lista_personajes, nombre))
        case "2":
            genero = input("Ingrese genero del Heroe F/M : ")
            print(nombres_valores(lista_personajes, "altura", valor_max, genero))
        case "3":
            genero = input("Ingrese genero del Heroe F/M : ")
            print(nombres_valores(lista_personajes, "altura", valor_min, genero))
        case "4":
            genero = input("Ingrese genero del Heroe F/M : ")
            print(promedio(lista_personajes, "altura", genero))
        case "5":
            dato = input(
                "Ingrese el dato que quiere saber, color_ojos / color_pelo / inteligencia: "
            )
            print(determinar_cuantos_superheroes_tipo(lista_personajes, dato))
        case "6":
            dato = input(
                "Ingrese el dato que quiere saber, color_ojos / color_pelo / inteligencia: "
            )
            print(agrupar_superheroes_por_valor(lista_personajes, dato))
