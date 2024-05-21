#ejer 1: escribe un programa que solicite al usuario
#dos numeros enteros y que determine si ambos numoers son
# mayores a 10
'''
n1=int(input('ingrese el primer numero: '))
n2=int(input('ingrese el segundo numero: '))
if n1 >=10 and n2 >=10:
    print('los numeros son iguales o mayores a 10')
else:
    print('alguno de los numeros es menor a 10')
'''

#ejer2: escribe un programa que solicite al usuario
#dos numeros enteros y determine si al menos uno de ellos es par
'''
n1=int(input('ingrese el primer numero: '))
n2=int(input('ingrese el segundo numero: '))
if n1%2 == 0 or n2%2 == 0:
    print('alguno de los numeros es par')
else:
    print('ninguno de ellos espar')
<>
'''
#ejer3: escriba un programa que solicite al usuario un numero
#entero y determine si el numero NO esta dentro de 1 y 100 (Inclusive)
'''
n1=int(input('ingrese un numero: '))
if not n1<1 and n1<=100:
    print('el numero esta entre 1 y 100')
else:
    print('El numero NO esta entre 1 y100')

#otra manera
num5= int(input('ingrese un numero: '))
if not 1 <= num5 <=100:
    print('el numero esta entre 1 y 100')
else:
    print('El numero NO esta entre 1 y100')
'''

#escriba un programa que le solicite al usuario
#un numero entero y determine si el numero es multiplo
# de 3 y de 5.
'''
n1=int(input('ingrese un numero: '))
if n1%3 == 0 or n1%5 == 0:
    print('El numero es multiplo de 3 o 5')
else:
    print('El numero NO es multiplo de 3 o 5')
 '''   
#escribe un programa que solicite al usuario
#su nombre y determine si su nombre empeza
#con una vocal (AEIOU)
'''
nom=input('Ingrese su nombre: ')
primeraL = nom[0]
if primeraL.upper() in 'AEIOU':
    print('Su nombre empieza con vocal')
else:
    print('Su nombre NO empieza con vocal')
'''

#Escribe un programa que solicite al usuario tres numeros
#enteros y determine si al menos uno de ellos
#es positivo
'''
n1=int(input('ingrese el primer numero: '))
n2=int(input('ingrese el segundo numero: '))
n3=int(input('ingrese el tercer numero: '))
if n1 >=0 or n2 >=0 or n3 >=0:
    print('Hay un numero positivo')
else:
    print('todos los numeros son negativos')
    
'''

#escribe un programa que solicite al usuario
#dos numeros enteros y determine si la suma de ambos es par
'''
n1=int(input('ingrese el primer numero: '))
n2=int(input('ingrese el segundo numero: '))
suma=n1+n2
if suma%2 == 0:
    print('La suma de los numeros es par')
else:
    print('La suma de los numeros no es par')
'''

#escribe un programa que solicite al usuario
#su edad y determine si tiene al menos 18 años
#y menos de 70 y por lo tanto esta en el rango para poder
#conducir
'''
edad=int(input('Ingrese su edad: '))
if edad >=18 and <=70:
    print('Usted esta en el rango para poder conducir')
else:
    print('Usted NO esta en el rango para poder conducir')
'''
#escribre un programa que solicite al usuario un año y determine
#si es bisiesto.
#dato: un año bisiesto si es divisible por4, pero no por 100
#a menos que tambien sea divisible por 400
'''
año=int(input('Ingrese un año: '))
if año % 4==0 and año%100 !=0 or año%400==0:
    print('Es año bisiesto')
else:
    print('No es bisiesto')
'''
#escibre un programa que solicite al usuario
#una palabra y determine si la palbra comienza y termina
#con la misma letra
'''
palabra=input('ingrese una palabra: ')
iniL=palabra[0]
endL=palabra[-1]
if iniL == endL:
    print('son iguales')
else:
    print('no son iguales')
'''