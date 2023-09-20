# desarrollar una funcion que calcule  la superficie de un circulo
# calcular_superficie_circulo



def calcular_superficie_circulo(radio:float) -> float:
    """superficie

    Args:
        PI (float):Valor de PI
        radio (float):Valor del radio ingresado por el usuario

    Returns:
        superficie: retorna la superficie del circulo.
    """
    try:
        superficie = 3.14 * radio ** 2
    except:
        superficie = None

    return superficie

# radio = float(input("Ingrese el radio del circulo:  "))

# print(calcular_superficie_circulo(PI,radio))


def calcular_superficie_rectangulo(largo: float, ancho: float) -> float:
    """superficie

    Args:
        largo (float): colocamos el largo que ingreso el usuario
        ancho (float):colocamos el ancho que ingreso el usuario

    Returns:
        superficie: Retornamos la superficie total.
    """    
    try:
        superficie = largo * ancho

    except:
        superficie = None

    return superficie


# largo = float(input("Ingrese el largo del rectangulo:  "))
# ancho = float(input("Ingrese el ancho del rectangulo:  "))
# print(calcular_superficie_rectangulo(largo, ancho))

def calcular_superfiecie_cuadrado(lado:float)->float:
    """superficie

    Args:
        lado (float): multiplicamos los lados

    Returns:
        superficie: retorna la superficie de un cuadrado
    """    
    superficie = lado * lado

    return  superficie

# lado = float(input("Ingrese el lado: "))
# print(calcular_superfiecie_cuadrado(lado))

# def calcular_superficie_triagulo():
#     superficie = pass

#     return superficie

# print(calcular_superficie_triagulo())