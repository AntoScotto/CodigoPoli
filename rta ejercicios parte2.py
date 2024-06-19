# Ejercicios Bucle
# 1. Imprimir los números del 1 al 10
'''
numero=0
for i in range(1,11):
    numero+=1
    print(numero)
'''
# 2. Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
'''
palabra=input('Ingrese una palabra: ')
for i in range(1,11):
    print(palabra)
'''    

# 3. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
#los años que ha cumplido (desde 1 hasta su edad)
'''
edad=int(input('ingrese su edad: '))
for i in range(edad):
    print(f'Su edad es {i+1}')
'''

# 4. Escribir un programa que pida al usuario un numero entero positivo
#y muestre por pantalla la cuenta atras desde ese numero hasta cero
'''
entero=int(input('ingrese un numero entero positivo: '))
for i in range(entero, -1,-1):
    print(i)
'''
# 5. Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interes anual y el numero de años, y muestre por pantalla el capital obtenido en la inversion cada año que dura la inversion
'''
dinero=int(input('Ingrese la cantidad de dinero que quiere invertir: '))
interes=float(input('Ingrese el interes anual: '))
anios=int(input('Ingrese a cuantos años: '))
for i in range(anios):
    dinero*= 1 + interes/100
    print(f'El capital despues de {i+1} años: {round(dinero,2)}')
'''

# 6. Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
'''
for i in range(1,11):
    print('~'*10)
    for y in range(1,11):
        print(f'{i} * {y} = {i*y}')
 '''   

# 7. Escribir un programa en el que se pregunte al usuario por una frase y una letra,
#y muestre por pantalla el numero de veces que aparece la letra en la fase
'''
frase=input('Ingrese una frase: ')
letra=input('Que letra desea saber la cantidad que contiene la frase?: ')
contador=0
for i in frase:
    if i == letra:
        contador+=1
print(f'La letra {letra} esta {contador} veces en la frase')

'''    

# 8. Escribe un programa para calcular la suma de todos los numeros pares del 1 al 100
'''
suma=0
for i in range(1,100):
    if i %2==0:
        suma =suma+i
        print(suma)
'''        
# Ahora vamos a aprender algo nuevooo .

'''
import random  se utiliza para importar el modulo "random"
que contiene una variedad de funciones para generar numeros aleatorios y realizar operaciones relacionadas con la aleatoriedad. 
Este modulo es parte de la biblioteca estandar de Py , por lo que no necesitas instalar nada adicional.


random.randint(a,b) se utiliza para generar un numero entero aleatorio entre a y b ( ambos inclusive)'''

# 9. Escribe un programa que genere un numero aleatorio entre 1 y 100
#y le pida al usuario que lo adivine. El programa debe seguir pidiendo al usuario
#que advine hasta que acierte. Debe indicar si el numero ingresado es demasiado alto
#o demasiado bajo en cada intento
'''
import random

num= random.randint(1,100)

while True:
    numero=int(input('Adivine el numero (entre 1 y 100): '))
    if numero > num:
        print(f'{numero} es alto')     
    elif numero < num:
        print(f' {numero} es bajo')
    else:
        print('Usted adivino el numero!')
        break

'''
'''
import random


num = random.randint(1, 100)


intentos = 0
while True:
    intentos += 1
    numero = int(input('Adivina el número (entre 1 y 100): '))
    
    if numero > num:
        print(f'El número {numero} es demasiado alto.')
    elif numero < num:
        print(f'El número {numero} es demasiado bajo.')
    else:
        print(f'¡Felicidades! ¡Adivinaste el número {num} en {intentos} intentos!')
        break
'''
# 10. Escribe un programa que tome una tupla de numeros.
#Calcule e imprima la suma de todos los numeros.
'''
numeros=2,3,4,5,6,7,8,9,10
suma=0
for i in numeros:
    suma+=i
print(suma)
'''
    
