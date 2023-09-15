#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#Elimine los elementos repetidos, por ultimo mostar la lista

#Creamos una lista
lista=[1,2,3,'Ariel',7,7,3,'Alberto',1,'Ariel',2,'Alberto']
#conjunto=set(lista)#Convertimos la lista a un conjunto de tipo set
#lista=list(conjunto)#Convertimos el conjunto a una lista
lista=list(set(lista))#La conversion hecha en una sola linea de codigo(eficiente)
print(lista)

#Ejercicio 2:Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 lista y que a continuacion
#Cree las siguientes listas(en las que no deben haber repeticion)
#1 Lista de palabras que aparecen en las lista
#2 Lista de palabras que aparecen en la primera lista,pero no en la segunda
#3 Lista de palabras que aparecen en la segunda listampero no en la primera
#4 Lista de palabras que aparecen en ambas listas

lista1=[1,2,3,4,5,4,3,2,2,1,5]
lista2=[4,5,6,7,8,4,5,6,7,7,8]

#Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union=list(conjunto1|conjunto2)#Unimos los elementos
solo1=list(conjunto1-conjunto2)#Muestra el conjunto 1
solo2= list(conjunto2-conjunto1)#Muestra el conjunto 2
interseccion=list(conjunto1 & conjunto2)#Mostramos las dos listas

print(f'Lista de palabras que aparecen en las listas:{union}')
print(f'Lista de palabras que aparecen en la primera lista,pero no en la segunda: {solo1}')
print(f'Lista de palabras que aparecen en la segunda lista pero no en la primera: {solo2}')
print(f'#4 Lista de palabras que aparecen en ambas listas: {interseccion}')

#Ejercicio 3 :Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

#Nombre: Aragon
#Clase: Guerrero
#Raza:Dunadan del norte

#Nombre : Gandalf
#Clase: Mago
#Raza: Istar

#Nombre:Legolas
#Clase:Arquero
#Raza:Elfo Sindar

personajes=[]#Creamos una lista vacia
#Creamos un diccionario
P= {'Nombre':'Aragon','Clase':'Guerrero','Raza':'Dunadan del Norte'}
personajes.append(P)#Agregamos a la lista un personaje
P= {'Nombre':'Gandalf','Clase':'Mago','Raza':'Istar'}
personajes.append(P)
P= {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo Sindar'}
personajes.append(P)
print(personajes)#Tarea:Agregar por lo menos otros tres personajes,que sean a tu eleccion
#Personajes Agregados a la lista
P= {'Nombre':'Sauron','Clase':'Guerrero','Raza':'Ainur'}
personajes.append(P)
P= {'Nombre':'Gollum','Clase':'4° Dueño del Anillo','Raza':'Hobbit corrompido'}
personajes.append(P)
P= {'Nombre':'Elrond','Clase':'Señor de Rivendel','Raza':'Peredhil'}
personajes.append(P)
print(personajes)

