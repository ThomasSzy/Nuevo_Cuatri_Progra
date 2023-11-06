from data_3 import lista


def ordenar_personas(lista, atributo="id", asc=True):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][atributo] > lista[j][atributo]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def mostrar_persona(persona):
    print(
        f" {persona['id']:2d}    {persona['nombre']:>20s}           {persona['edad']:2d}  {persona['gender']:>4s}   {persona['sector']:>30s}"
    )


def mostrar_personas(lista: list):
    print(" Lista de personas")
    print(" Id                  nombre          edad        genero        sector ")
    for persona in lista:
        mostrar_persona(persona)



tam = len(lista)
for i in range(tam - 1):
    for j in range(i + 1, tam):
        if lista[i]["sector"] > lista[j]["sector"]:#Desordenado  por Genero
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
        elif lista[i]["sector"] == lista[j]["sector"]:
            if lista[i]["gender"] == lista[j]["gender"]: #Desordenado por Nombre o edad lo que queramos
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


mostrar_personas(lista)


