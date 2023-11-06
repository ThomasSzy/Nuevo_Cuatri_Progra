#               #Burbujeo           #
from data import lista

# lista = [4, 9, 2, 8, 5]
# tam = len(lista)

# print(lista)
# for i in range(tam - 1):  # Nunca llega al final el "i"
#     for j in range(i + 1, tam):  # Donde empieza i +1 ------ El final de la
#         if lista[i] > lista[j]:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
# print(lista)

# Alfabeticamente codigo asky todas las letras son numeros, las letras estan ordenadas con numeros


# lista = ["Juan", "Lucia", "Analia", "Jorge", "Thomas","agustin"]
# tam = len(lista)

# print(lista)
# for i in range(tam - 1):  # Nunca llega al final el "i"
#     for j in range(i + 1, tam):  # Donde empieza i +1 ------ El final de la
#         if lista[i].upper() > lista[j].upper():
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
# # print(lista)


##### MENOR A MAYOR EDAD ########
# tam = len(lista)
# for persona in lista:
#     print(persona)
# for i in range(tam - 1):  # Nunca llega al final el "i"
#     for j in range(i + 1, tam):  # Donde empieza i +1 ------ El final de la
#         if lista[i]["edad"] > lista[j]["edad"]:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print("-------------")
# for persona in lista:
#     print(persona)


####### MAYOR TAMA;O DE NOMBRES ###########
# tam = len(lista)
# for persona in lista:
#     print(persona)
# for i in range(tam - 1):  # Nunca llega al final el "i"
#     for j in range(i + 1, tam):  # Donde empieza i +1 ------ El final de la
#         if len(lista[i]["nombre"]) < len(lista[j]["nombre"]):
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print("-------------")
# for persona in lista:
#     print(persona)


# def ordenar_lista_entero(list, key):
#     tam = len(list)
#     for i in range(tam - 1):  # Nunca llega al final el "i"
#         for j in range(i + 1, tam):  # Donde empieza i +1 ------ El final de la
#             if lista[i]["edad"] > lista[j]["edad"]:
#                 aux = lista[i]
#                 lista[i] = lista[j]
#                 lista[j] = aux


###### TAREA #########
# HACER UNA FUNCION QUE RECIBA UNA LISTA DE NUMEROS Y QUE SE PUEDA  ORDENAR
# DE MANERA CRECIENTE O DE MANERA DECRECIENTE


lista = [4, 9, 2, 8, 5]

# def ordenar_lista_menor_a_mayor(list: list, creciente: bool = False):
#     tam = len(list)
#     for i in range(tam - 1):
#         for j in range(i + 1, tam):
#             if creciente:
#                 if lista[i] > lista[j]:
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux
#             else:
#                 if lista[i] < lista[j]:
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux


# print(lista)
# ordenar_lista_menor_a_mayor(lista, True)
# print(lista)


def ordenar_lista(list: list, creciente: bool = False):
    tam = len(list)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (creciente and lista[i] > lista[j]) or (not creciente and lista[i] < lista[j]) :
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


print(lista)
ordenar_lista(lista, False)
print(lista)
