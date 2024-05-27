#ejercicio2
#Crear y acceder a los elementos de una tupla:
#al tupla tiene que contener los numeros del 1
#al 5, imprimer el primer valor y el ultimo
'''
t=[1,2,3,4,5]
print(t[0],t[-1])
'''
#ejercici3
#Desenpaquetar una tupla
#crear una tupla con tres elementos(dif datos)
#desenpaquetar la tupla en 3 variables e imprimir
'''
t1=('anto','Rio grande',33)
nombre,apellido,edad =t1
print(nombre)
print(apellido)
print(edad)
'''

#Ejercicio4:
#Crear dos tuplas con los elementos que quieras, concátenalas en
#una nueva tupla repite la nueva tupla dos veces y almacenalas
#en una nueva tupla
'''
tupla1=('a','b','c')
tupla2=('d','e','f')
tupla3=tupla1+tupla2
tupla4=tupla3*2
print(tupla4)
'''

#ejercicio5
#crea una tupla con los numero del 1 al 10
#e imprimi una sub-tupla que contenga del tercer al
#sexto elemento
'''
tupla6=1,2,3,4,5,6,7,8,9,10
tupla7= tupla6[2:6]
print(tupla7)
'''
#ejercicio6
#crea una tupla con los numero del 1 al 15
#e imprimi una sub-tupla que contenga los numeros pares
'''
tupla8=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

tupla9=(tupla8[1:15:2])
print(tupla9)

'''
#ejercicio7
#hacer que la tuplaque se creo antes comience desde el 15 y termine en 1
'''
tupla8=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
tupla9=tupla8[::-1]
print(tupla9)
'''

#Ejercicio8
'''
#crea una variable con tu nombre y darlo vuelta
nombre='antonela'
nomR=nombre[::-1]
print(nomR)
'''
