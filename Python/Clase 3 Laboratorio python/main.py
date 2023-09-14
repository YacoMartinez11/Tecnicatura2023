# Para definir un conjunto
conjunto2 = set()
conjunto1= {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

# Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 # Une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto 2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos uqe no comparten o son diferentes
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Preguntamos si un comjunto es un subconjunto dentro de oto
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del cojunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconunto
print(conjunto1.issuperset(conjunto3))

# Como saber si ambos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente inmutable
conjunto1 = frozenset
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como Eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel':{'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

# Ejercicios con diccionario

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre':'Franco Armani','Edad':35,'Altura':1.89,'Precio':'3.5 Millones','Posicion':'Portero'}

}
for llave, valor  in seleccionArgentina.items():
    print(llave,valor)

#Como tarea agregar por lo menos 4 jugadores mas al diccionario : seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ',end=' ')
print(len(seleccionArgentina))

seleccionArgentina[6] = {'Nombre': 'Leandro Paredes', 'Edad': 29, 'Altura': 1.82, 'Precio': '12 Millones', 'Posicion': 'Centrocampista'}
seleccionArgentina[21] = {'Nombre': 'Alexis McAllister', 'Edad': 24, 'Altura': 1.76, 'Precio': '40 Millones', 'Posicion': 'Centrocampista'}
seleccionArgentina[25] = {'Nombre': 'Enzo Fernandez', 'Edad': 22, 'Altura': 1.78, 'Precio': '121 Millones', 'Posicion': 'Centrocampista'}
seleccionArgentina[8] = {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.80, 'Precio': '37 Millones', 'Posicion': 'Centrocampista'}
print(seleccionArgentina)

#Pilas usando listas
pila = [1, 2, 3]

# Agregar elemntos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# sacamos elementos desde el final
elementoBorrado = pila.pop()
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con Listas
#estructura de datos de tipo fifo(first input/ first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agragamos elementos al final de la cola

cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacar elemntos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

