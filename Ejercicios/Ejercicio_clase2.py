""" 
# Ejercicio 01
# Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
# en la bolsa de valores:
# A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
# * Nombre
# * Monto en pesos de la operación (no menor a $10000)
# * Cantidad de instrumentos
# * Tipo (CEDEAR, BONOS, MEP)
# B) Luego del ingreso mostrar en pantalla todos los datos.
# C) Realizar los siguientes informes:
# 1. Tipo de instrumento que más se operó.
# 2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
# más de $50000.
# 3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
# que menos dinero invirtió. Puede ser más de uno.
# 4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
# monto promedio
# 5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
# no supere los $50000.
"""

#Bucle infinito (hasta que el usuario quiera)
#Datos: Nombre, monto(Mayor a 10.0000), cantidad, tipo(alguno de los 3).
#imprimir datos
#....


nombres = ["Juan","Pedro","Thomas","Luz"]
montos = [1000,23333,55555,11111]
cantidades = [2,3,5,6]
tipos = ["cedear","tipo","csas","asdasda"]
contador_tipos = [0,0,0]

# while True:
#     #Pedimos datos
#     nombres.append(input("Ingrese Nombre: "))
# #------------MONTO---------------#
# #     while True:
# #         try:
# #             monto = float(input("Ingrese Monto Mayor a 10.000:  "))
# #             if monto >= 10000:
# #                 break
# #             else:
# #                 print("Monto Invalido")
# #         except:
# #             print("Eso no es un Numero")

# #     #Agrego monto a la lista
# #     montos.append(monto)
# # # #-------------EDAD--------------#
# #     while True:
# #         try:
# #             edad = input("Ingrese Edad: ")
# #             if edad.isdigit():
# #                 edad = int(edad)
# #                 if edad >= 18 or edad <=65:
# #                     break
# #             else:
# #                 print("Edad fuera de rango")
# #         except:
# #             print("Eso no es una edad")
# # # #--------------CANTIDAD-------------#
# #     while True:
# #         try:
# #             cantidad = int(input("Ingrese Cantidad Mayor a 1000:  ")) 
# #             if monto >= 0:
# #                 break
# #             else:
# #                 print("Cantidad Invalidoa")
# #         except:
# #             print("Eso no es un Numero")
# #     cantidades.append(cantidad)

# # # #--------------TIPO-------------#
    # while True:
    #         tipo = input("Ingrese el Tipo: CEDEAR, BONOS, MEP:  ") 
    #         if tipo == "cedear" or tipo == "bonos" or tipo == "mep":
    #             break
    #         else:
    #             print("Tipo Invalido")
    
    # tipos.append(tipo)
    # if tipo == "cedear":
    #     contador_tipos[0] += 1
    # elif tipo == "bonos":
    #     contador_tipos[1] += 1
    # else:
        # contador_tipos[2] += 1
# # --------------TIPO-------------#

#     seguir = input("Quiere continuar? [Si/No]: ")
#     if not (seguir == "s" or seguir == "S"):
#         break


# print(nombres)
# print(montos) 
# print(cantidades)
# print(tipos)

# print(" *** Listado de operaciones ***")
# print("     Nombre        Monto    Cantidad    Tipo")
# for i in range(len(nombres)):
#     print(f"{nombres[i]:>10}    {montos[i]:9.2f}    {cantidades[i]:3d}      {tipos[i]:>6}")
