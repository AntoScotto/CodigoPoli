'''
#tuplas
#secuencia inmutable lo que significa que no le podemos cambiar los valores

#tupla vacia
t=()

print(t)

#una tupla con un solo valor

t1=(1,) #t1=1,
print(t1)

#tupla con varios valores

t2=(1,2,3,4) #t2=1,2,3,4
print(t2)

#funcion tuple
saludo='Hola Mundo'
print(tuple(saludo))

#funcion len()
tupla=21,36,87
print(len(tupla))

t4=14,35,23
print(t4[1])
x=t4[2]
print(x)

#error tupla
#t5=13,34,22
#t[2]=18
#print(t[2])
'''
#ejercicio31
nomes=input('nombre del estudiante: ')
nompro=input('nombre del docente: ')
pro=float(input('ingrese promedio del estudiante con decimales: '))

t1='est.','prof.'
#forma 1
print(nomes,t1[0])
print(nompro,t1[1])
print('promedio notas:',round(pro))

#forma 2

datos=(nomes,nompro,pro)
print('est.',datos[0],'prof.',datos[1],'promedio:',round(pro))

