planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # función len = length significa largo

#para revisar si existe un elemento en el set
print('Júpiter' in planetas)

# Agregar elemento
planetas.add('Tierra')
print(planetas)

#Eliminar elemento
planetas.remove('Júpiter') # da error si lo escribimos mal
print(planetas)
planetas.discard('Tierra') # no da error si lo escribimos mal
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas
#print(planetas) # nos da error porque ya no existe

"""
#Diccionario esta compuesto por dos elementos 
# Una llave y un valor 
# dict (key, value)
"""
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
print(diccionario)

# Para verificar la cantidad de elementos
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))

# Modificar elemento en el diccionario
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

# Otra manera de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de elemento
print('IDE' in diccionario)

# Agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) #".extend" es para agragar elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado

# Como saber cuantos valores estan repetidos en una lista
print(lista3.count(1)) #cuanta cunatos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort() # Ordena los elementos de forma ascendente
print(lista3)
lista3.sort(reverse=True) # Ordena los elementos de for descendente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentyes tipos de datos dentro
print(tupla)

print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana
