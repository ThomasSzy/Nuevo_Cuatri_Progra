
# def saludar(nombre):
#     print("Hola " + nombre)

# saludar("Juan")
# saludar("Thomas")
# saludar("Luz")


# def decime_hola():
#     return "Hola"


# def mi_funcion():

#     a = 5 + 4
#     return a
# # x = decime_hola()
# print(mi_funcion())

# def sumar(a, b):

#     suma =  a + b

#     return suma

# x = sumar(5,8)

# print(x / 2)


#Desarrollar una funcion que reciba dos nuemeros enteros y 
# devuelva el promedio. calcular_promedio






# # --------------Primer Ejemplo PROMEDIO-------------#
# num1 = int(input("Ingrese un numero "))
# num2 = int(input("Ingrese un numero "))
# # --------------Segundo Ejemplo PROMEDIO-------------#
# num1 = 5
# num2 = 14

# suma = num1 + num2

# promedio = suma / 2

# print(f"Promedio es {promedio}")

num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese un numero "))

def calcular_promedio(a:int , b:int) ->float:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        float: _description_
    """    
    suma = a + b
    promedio = suma / 2
    return promedio

print(calcular_promedio(num1, num2))
# # --------------PROMEDIO-------------#
# def calcular_promedio(a, b):
#     promedio = (a + b)/ 2

#     return promedio

# print(calcular_promedio(18,3))