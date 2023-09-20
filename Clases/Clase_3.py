# COMENTAR CON  CONTROL + "/"


# secuencia = list(range(5)) #---> Range devuelve una secuencia de numeros
# print(secuencia)
# nombres = ["Juan","Thomas"]
# for i in range(len(nombres)):
#     print(nombres[i])
#------------------------------------------------#
# nombre = "Juan"

# print("hola " + nombre)
#------------------------------------------------#
# nombre = 30

# print("hola " + str(nombre)) #--->Pasamos el numero a str para poder usarlo en el print de str + str
#------------------------------------------------#
# nombre = "Juan"
# apellido = "Perez"
# edad = 30
# print("hola {} {} {}".format(nombre, apellido, edad)) #--->Modificamos el contenido dentro de hola y metemos el nombre donde esta el {}
#------------------------------------------------#
# nombre = "Juan"
# apellido = "Perez"
# edad = 30
# print(f"Hola {nombre} {apellido} edad {edad}") #---> Manera mas Simple agregando la (F)

#--------------------COMO SACAR UN MAYOR----------------------------#
a = 20
b = 30
c = 25

if a > b and a > c:
    mayor = a
elif b > c and b>=a:
    mayor = b
else:
    mayor = c

print(F"El mayor es: {mayor}")
