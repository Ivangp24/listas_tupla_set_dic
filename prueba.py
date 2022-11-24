print('listas y colecciones')

# colecciones es la clase padre de todas
# existen distindas colecciones: []Lists (ordenado individaulmente) -  )Tuples (ordenado por bolsas) -
# {}Set (se puede meter numeros y texto sin ningun orden) - {' ':' '}Dictionaries ()

# Crear listas, tublas, set y diccionarios
lista=[10,'madrid',True,15.95,'valencia',10] # soporta repetición.
print(lista)

tupla=(10,'madrid',False) #es un conjunto fijo (inmutable)

set={10,'madrid',True,15.95,'valencia',10} # Es un conjunto.no soporta repetición, no ordena. El set es muy rapido
print(set)

diccionario={'lunes':15,'martes':18.5}
print(diccionario)

#Mutable vs Inmutable

# LISTA es MUTABLE
lista[0]=14 #setter -> cambia un elemento por otro
print(lista[0]) #getter -> vemos que elemento hay en essa posición. Es una consulta
print(lista[5])
# para añadir un elemento a la lista
lista.append('elemento añadido') #add ok

lista[6]='novedad' # solo si el elemento 6 ya existe
for item in lista:
    print(item)

# TUPLA es INMUTABLE

# SET es MUTABLE
#no soporta duplicado
set.add('item añadido al conjunto')
for i in set:
    print(i)

# DICCIONARIO es MUTABLE

#ORDENAR

lista1=[2,8,9,6,5,4,74]
lista1.sort()# Los elementos de la lista deben tener el mismo tipo de dato


# 1ºcomo se crean
# 2º mutables o inmotables
# 3º ordenar
# 4º Si soporta: sort() y  count(