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
        key (str): el id de lo que buscamso, en este caso "altura"
        funcion (float): busca el dato que sea igual al de valor y
                        toma el nombre y el valor pedido y lo printea
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


def determinar_cuantos_superheroes_tipo(lista: list, key: str) -> str:
    # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    # L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
    # no tener, Inicializarlo con ‘No Tiene’).
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


def nombres_personajes(lista, key):
    nombres_heroes = determinar_cuantos_superheroes_tipo(lista, key)
    for nombre in nombres_heroes:
        print(f"asdasdas {nombre}")


# print(determinar_cuantos_superheroes_tipo(lista_personajes, "color_ojos"))
print(nombres_personajes(lista_personajes, "color_ojos"))
