from data_stark import lista_personajes


# Punto B
def imprimir_datos_str(lista: list, key) -> None:
    """imprimir_datos_str

    Args:
        lista (list): proporciona una lista con datos de los personajes
        key (_type_): el usuario da una key de lo que quiere buscar
        en este caso va a buscar nombres. pero puede ser todo tipo de str.
    """
    for personajes in lista:
        datos_personajes = personajes[key]
        print(datos_personajes)


# Punto C
def altura_personajes(lista: list) -> None:
    """altura_personajes
    tomamos la altura y el nombre de los personajes
    Args:
        lista (list): proporciona una lista con datos de los personajes
    """
    for altura_nombre in lista:
        nombre_personaje = altura_nombre["nombre"]
        altura_personajes = float(altura_nombre["altura"])
        print(f"El personaje {nombre_personaje} mide {altura_personajes}")


# Punto D y H
def valor_max(lista: list, key: str) -> float:
    """altura_max
        Sacamos Valor maximo de la lista de personajes

    Args:
        lista (list): Colocamos una lista con los datos de los personajes
        flag: Colocamos una flag para que ingrese si o si guardando el dato
        de la altura y luego empiece a comparar con las demas alturas
    Returns:
        float: returna el numero maximo de la lista de alturas
    """
    numero_max = 0
    flag_valor = True

    for valor in lista:
        valor_lista = float(valor[key])

        if valor_lista >= numero_max or flag_valor == True:
            numero_max = valor_lista
            flag_valor = False

    return numero_max


# (Creo que se podria optimizar realizando una sola funcion que haga maximos
# y minimos para no recorrer la lista 2 veces o directamente pasar todos
# los datos del diccionario y darles un Id para poder llamarlos)


# Punto E y H
def valor_min(lista: list, key: str) -> float:
    """altura_min
    Buscamos la altura minima en la lista

    Args:
        lista (list): lista con los valores de los personajes
        for: buscamos el valor altura y lo parseamos.

        if: buscamos el valor minimo y con una flag obligamos a que
        ingrese si o si un dato para ser comparado con cual es mas
        chico

    Returns:
        float: devuelve el valor minimo
    """
    minimo = 0
    flag_valor = True

    for valor in lista:
        valor_lista = float(valor[key])

        if valor_lista <= minimo or flag_valor == True:
            minimo = valor_lista
            flag_valor = False
    return minimo


# Punto F
def promedio(lista: list, key) -> float:
    """promedio_altura
        buscamos la cantidad de personajes y sumamos sus estaturas
        y sacamos el promedio

    Args:
        lista (list): lista con los datos de todos los personajes

    Returns:
        float: devuelve el promedio total
    """

    valor_total = 0
    cantidad_unidades = 0
    for alturas in lista:
        valor_total += float(alturas[key])
        cantidad_unidades += 1
    promedio = valor_total / cantidad_unidades
    return promedio


# Punto G y H
def nombres_valores(lista: list, key: str, funcion) -> None:
    """Tomamos valores de una funcion y lo que deseamos buscar.
        y de ahi le damos el nombre del valor pedido

    Args:
        lista (list): lista de personajes
        key (str): el id de lo que buscamso, en este caso "altura"
        funcion (float): busca el dato que sea igual al de valor y
                        toma el nombre y el valor pedido y lo printea
    """
    valores = funcion(lista, key)

    if valores:
        for maximo_minimo in lista:
            if float(maximo_minimo[key]) == valores:
                nombre = maximo_minimo["nombre"]
                altura_max = maximo_minimo[key]

        print(f"El personaje es {nombre} y su valor es {altura_max}")


# Menu
def menu_stark():
    """menu_stark: creamos la base del menu lo que el usuario ve al momento de elegir 
                    las opciones
    """    
    seguir = True

    while seguir:
        print(" *** Menu de Opciones ***")
        print("1- Nombre de Personajes")
        print("2- Nombre  y la Altura de cada personaje")
        print("3- Super Heroe mas Alto")
        print("4- Super Heroe mas Bajo")
        print("5- Super Heroe mas Pesado")
        print("6- Super Heroe menos Pesado")
        print("7- Promedio pesos")
        print("0 si desea salir ")

        opcion = input("Ingrese Opcion: ")
        if opcion == "0":
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
            print(imprimir_datos_str(lista_personajes, "nombre"))
        case "2":
            altura_personajes(lista_personajes)
        case "3":
            nombres_valores(lista_personajes, "altura", valor_max)
        case "4":
            nombres_valores(lista_personajes, "altura", valor_min)
        case "5":
            nombres_valores(lista_personajes, "peso", valor_max)
        case "6":
            nombres_valores(lista_personajes, "peso", valor_min)
        case "7":
            print(promedio(lista_personajes, "altura"))
