#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
#Crear una lista que solo incluya los numeros menores a 5 e impima por consola [1, 3, 2]

lista = [] #Aca definimos la tupla

#se filta los numeros menores a 5 con un "for"
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
