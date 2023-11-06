file = open("./archivo.txt", "r")  # --> r de Lectura

# x = file.read() # ---> Leemos todo el archivo
# x = file.readline() # --->Leemos una sola linea del archivo
x = file.readlines()
print(x, end="")


file.close
