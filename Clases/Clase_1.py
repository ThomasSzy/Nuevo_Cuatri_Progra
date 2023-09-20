""" x = "Juan"
e = [] """

""" x = 30

x = 20 """
#------------------------------------#

""" 
x = 10
print(id(x))
x = 20
print(id(x))
x = 40
print(id(x)) """

#------------------------------------#

""" x = 30
print(id(x))

y = 30
print(id(y))

y = 50
print(id(y)) """

#------------------------------------#

""" 
print()

int()
input()
float()
id()
type()


x = [2,5,6]

print(id(x))

x.append(8) # --->[2,5,6,8]
print(id(x)) """

#------------------------------------#
#Explicado en la Tablet
x = 4
""" 
lista = []

lista.append(4) 
"""
lista = [4, 3, 70]

print(id(x))

print(id(lista[0])) # ---> Busco en posicion 0 de lista || --> print(id(lista)) busca el id de la lista entera.||

""" 
x = 5

print(id(x))
print(id(lista[0]))
"""
print(id(lista))
print(lista)

lista[1] = 20 # ---> [4, 3, 70] --> reemplaza el 1 [0, 1, 2] quedaria [4, 20, 70]
print(id(lista))
print(lista)





