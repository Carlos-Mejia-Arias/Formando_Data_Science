# Esto es un comentario de 1 linea
""" Esto es un comentario de varias lineas """

"""---------------------------------------------------"""

# Variables

string = 'Hola Mundo' # se usa comillas simple o doble comillas
entero_int = 10
decimal_float = 3.14
booleano_bool = True

""" Esta es una forma como podemos asignar variables en una sola fila, no es recomendable usarlo mucho o poner muchas variables en una sola lista, ademas tenemos que tener cuidado en el orden del ingreso de datos."""
nombre, apellido, edad = 'Luis', 'Perez', 35

"""---------------------------------------------------"""

# Mostrar en pantalla

print(string)
print(entero_int)
print(decimal_float)
print(booleano_bool)
print(nombre, apellido, edad)

"""---------------------------------------------------"""

# Concatenar variables

nombre = 'Juan'
apellido = 'Asturias'

print(nombre + apellido) # no deja espacio
print(nombre + ' ' + apellido) # si deja espacio
print(nombre , apellido) # permite dejar un espacio
print(f'{nombre} {apellido}') # permite dejar un espacio y es mas elegante
print("este es un sting concatenado a una variable:" + " " + nombre)

"""---------------------------------------------------"""

# Identificar tipo de variables

print(type(string))
print(type(entero_int))
print(type(decimal_float))
print(type(booleano_bool))

"""---------------------------------------------------"""

# Forzar el tipo
""" Cuando queremos que una variable asignada tenga otro tipo de dato"""

asignacion = 10 

print(type(asignacion)) # es un int
asignacion2 = str(asignacion) # forzamos a string
print(type(asignacion2))

asignacion3 = 10
print(str(asignacion3)) # forzamos a string
print(type(asignacion3)) # es un string

"""---------------------------------------------------"""

# Operadores Aritméticos

print(5 + 4)
print(6 - 4)
print(7 * 4)
print(5 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

"""---------------------------------------------------"""

# Operación mixta

print("Hola " * 5) # muestra en pantalla 5 veces hola
print("Hola " + str(5)) # muestra el string y fuerza el int a ser string

"""---------------------------------------------------"""

# Operadores relacionales

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python") # también podemos hacer comparaciones con string para obtener True o False

"""---------------------------------------------------"""

# Operadores Lógicos

# AND

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# OR

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

# NOT

print(not True)  # False
print(not False) # True
print(not not not not True) # True

"""---------------------------------------------------"""

# listas  --> usamos corchetes para identificarla

lista1 = [1, 2, 3, 4, 'Si', 1.8] 
print(type(lista1))

# Acceder a las listas

lista2 = [3, "Python", 3.87]

""" Para acceder a las listas primero escribimos el print, luego la variable y entre corchetes la posicion a la que deseamos ingresar"""

print(lista2[0]) 
print(lista2[1]) 
print(lista2[2]) 

""" si tenemos una lista dentro de una lista para ingresar seria de esta forma"""

lista3 = [3, "Python", 3.87, [1, 2, 3, 4]]

print(lista3[3][1]) # ingresamos el nombre de la variable, la posición de la sub lista y por ultimo la posición deseada

""" Ingresar al ultimo elemento"""

print(lista2[-1])

""" Modificar elementos """

lista2[0] = 8
print(lista2)  # nuevo resultado [8, 'Python', 3.87]

""" Eliminar elemento"""

lista4 = [1, 2, 3, 4, 5, 6]
# del lista4[0]  # comentado para que no elimine elementos, retira el # del inicio para que puedas ver como trabaja
print(lista4)  # nuevo resultado [2, 3, 4, 5, 6]

# lista4.remove(3) # de esta forma podemos eliminar el elemento si lo conocemos en este caso el 3, retira el # del inicio para que puedas ver como trabaja

""" Crear sub-listas --> usamos : entre corchetes, esto indica, valor de inicio = izquierda, valor final = derecha (este no esta incluido)"""

lista5 = [1, 2, 3, 4, 5, 6]
print(lista5[0:2]) # resultado [1,2]

""" Añadir un valor a la lista """

lista6 = [1, 2, 3, 4, 5]
lista6.append("Si")
print(lista6) # resultado [1, 2, 3, 4, 5, 'Si'], siempre se añade al final de la lista

lista6.insert(0,"hola") # otra forma de añadir un valor --> la primera posición es el lugar de inserción y luego el valor añadido
print(lista6)

"""---------------------------------------------------"""

# Tuplas 

""" parecidas a las listas pero inmutables (no pueden ser modificadas), se inician con () """

"""---------------------------------------------------"""

# Diccionarios

dic1 = {"Nombre": "Luisa","Edad": 27,"Documento": 62543484, "Altura":1.80, "fumadora": False}
print(dic1)
print(type(dic1))

dic2 = dict([('Nombre', 'Luisa'), ('Edad', 27), ('Documento', 62543484), ('Altura', 1.8), ('Fumadora', False)])
print(dic2)
print(type(dic2))

dic3 = dict(Nombre='Luisa', Edad=27, Documento=62543484, Altura=1.80, Fumadora=False)
print(dic3)
print(type(dic3))

""" Acceder a diccionarios --> es parecido a las listas, pero usamos la clave."""

print(dic1['Nombre'])
print(dic1.get('Nombre')) # también podemos usar la función get()sin corchetes

""" Modificar diccionarios"""

dic1['Nombre'] = "Laura"
print(dic1) # {'Nombre': 'Laura', 'Edad': 27, 'Documento': 62543484, 'Altura': 1.8, 'fumadora': False}

dic1['Direccion'] = "Calle 123"  # Si no existe el elemento que queremos modificar lo añade al diccionario
print(dic1) # {'Nombre': 'Laura', 'Edad': 27, 'Documento': 62543484, 'Altura': 1.8, 'fumadora': False, 'Direccion': 'Calle 123'}

dic2.update({'empresa': 'GG', 'hobby': 'Ajedrez'}) # update --> permite añadir multiples elementos

""" Eliminar de elementos  --> están comentados para que no se elimine, pero puedes probarlo solo quitando el #"""

# del dic2['Altura']
print(dic2)
# dic2.clear() # Elimina todos los elementos del diccionario



""" Podemos ver mas en esta pagina web que dejo como referencia donde " https://docs.python.org/es/3/tutorial/datastructures.html " hay mas información sobre las tupas, listas y diccionarios, asi como otros tipos de estructura de datos.  

Hagan experimentos de combinar acciones, crear diccionarios y sub diccionarios o listas y sub listas para poder entender mejor el tema, la programación no es de memoria, es de practicar."""