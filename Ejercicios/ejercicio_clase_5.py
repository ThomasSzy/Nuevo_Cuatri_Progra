# Desarrolar una funcion quue se llama calcular_IVA que reciba
# un valor y retorne el 21% del valor ingresado


# def calcular_IVA(a: float) -> float:
#     """IVA
#     Args:
#         valor_IVA (float): realiza la cuenta del iva

#     Returns:
#         valor_IVA: Retorna el resultado del iva
#     """
#     valor_IVA = a * 0.21
#     return valor_IVA


# a = float(input("Ingrese un valor para calcular el IVA:  "))
# print(calcular_IVA(a))


# # --------------Primer Ejemplo realizado por profe-------------#


# def calcular_IVA(monto: float) -> float:


#     return monto * .21  # ->La maquina sabe que tiene un 0 delante( podemos colocar solo .21)


# print(calcular_IVA("Pepe"))

# # --------------Segundo Ejemplo realizado por profe-------------#
# CON TRY Y EXCEPT
# def calcular_IVA(monto: float) -> float:
#     try:
#         iva = monto * 0.21
#     except:
#         iva = None

#     return iva


# print(calcular_IVA("Pepe"))

# # --------------Segundo Ejemplo realizado por profe-------------#


# def calcular_porcentaje(monto: float, porcentaje: float) -> float:
#     try:
#         porcentaje = monto * porcentaje / 100

#     except:
#         porcentaje = None

#     return porcentaje

# print(calcular_porcentaje(100,22))

