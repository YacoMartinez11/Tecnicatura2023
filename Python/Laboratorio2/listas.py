#lista = Ariel, Liliana, Natalia, Osvaldo
nombres=['Naty','Osvaldo','Lyli','Ariel']
print(nombres)
print(nombres[0:2]) # Solo muestra el indece 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#moficamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
      print(nombre)
else:
      print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()

#Eliminar un indice especifico
del nombres[2] # del significa delete
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres)