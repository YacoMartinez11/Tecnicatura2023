# Ejercicio 1: llnar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for,
# los elementos deben mostrarse  de la siguien forma: 1-2-3-4-5...-50

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i, end='-')
