# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)

# Acceder a un elemteno, para esto utilizamos corchetes no parentsis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') # usamos end= para eleminar los saltos de lineas

cocinaLista= list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple (cocinaLista)
print('\n', cocina)

#Elimar la tupla
del cocina
print(cocina)
