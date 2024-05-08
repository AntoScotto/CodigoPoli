'''print('hola mundo') #sirve para impirmir por consola
#crear mi primera variable
saludo = 'hola mundo desde variable'
#Imprimir la variable
print(saludo)
#Imprimir por consola hola + nombre
nombre = 'antonela'
#para concatenar pueden usar , o +
print('hola', nombre)
'''

#Act4
'''
#Entradas
#input permite ingreso en cadena de txt #int convierte ola cedena de txt en entero
#ingresa en string y convierte a entero (int) y decimal (float)
n1 = int(input('ingrese n1: '))
n2 = float(input('ingrese n2: '))

#procesos

suma= n1 + n2


#Salidas
print('El resultado de la suma es:',suma)
'''
'''
#Ejercicio5

#Entrada

n1 = int(input('ingrese n1: '))
n2 = int(input('ingrese n2: '))

#Proceso

producto = n1*n2

#Salida

print('El resultado del producto es: ', producto)
'''
'''
#Act6
#Entrada

l1 = float(input('ingrese cm : '))


#Proceso

per = l1*4 

#Salida

print('El perimetro es de: ', per)

'''
'''
#Act7

#Entrada
a = 5
b = 3

#Proceso

suma = a+b
dif = a-b
prod = a*b

#Salida

print('la suma es: ',suma, 'la resta es: ',dif ,'la multiplicacion es: ', prod)
'''
'''
#Act8

#Entrada
cant1 = int(input('Productos vendidos Art1: '))
pre1  = float(input('Precio Art1: '))
cant2 = int(input('Productos vendidos Art2: '))
pre2 = float(input('Precio Art2: '))
cant3 = int(input('Productos vendidos Art3: '))
pre3 = float(input('Precio Art3: '))
#Proceso
venta1 = cant1*pre1
venta2 = cant2*pre2
venta3 = cant3*pre3
total= venta1+venta2+venta3

#Salida 

print('El total de ventas del Art1: ', venta1)
print('El total de las ventas del Art2: ', venta2)
print('El total de ventas del Art3: ', venta3)
print('importe total de ventas es de: ', total)

'''
'''
#Act9

#Entrada
km = float(input('Ingrese los km recorridos: '))
pre = float(input('Ingrese precio de combustible:'))
kml = float(input('Ingrese autonomia por litro: '))
#Proceso
lcons = km/kml
gascom = lcons*pre


#Salida

print('Litros consumidos: ', lcons)
print('Importe gastado: ', gascom)
'''
'''
#Act10

#Entrada
t1 = float(input('Ingrese temperatura por la mañana:'))
t2 = float(input('Ingrese temperatura por la tarde:'))
t3 = float(input('Ingrese temperatura por la noche:'))

#Proceso

prot = (t1+t2+t3)/3


#Salida
print('La temperatura promedo del dia fue de: ',prot)
'''

