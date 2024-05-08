#Ejercicio 1 de practica
#Escribir un programa que pregunte al usuario su edad
#y muestre por pantalla si es mayor de edad o no
'''
edad = int(input('Ingrese su edad: '))
if edad >= 18:
    print('Usted es mayor de edad')
else:
    print ('Usted es menor de edad ')
'''
#Escribir un programa que almacene la cadena de caracteres
#'contraseña' es una variable, pregunte al usurio por la contraseña
#e imprima por pantalla si la contraseña introducida por el usuario
#coincide con la guardada en la variable sin tener en cuenta mayusculas
#y minusculas
'''
contra = 'contraseña'
contra2 = input('ingrese la contraseña: ').lower()
if contra2 == contra:
    print('Contraseña valida')
else:
    print('Contraseña invalida')
  '''  '''
#Escribir un programa que pida al usuario dos numeros y muestre por
#pantalla su división. si el divisor es cero el programa debe mostrar
#un error
n1= int(input('Ingrese el dividendo: '))
n2= int(input('Ingrese el divisor: '))

if n2 == 0:
    print('El divisor no puede ser cero')
else:
    print(n1/n2)
    
'''
'''

#Escrubir un programa que pida al usuario un numero entero y muestre
#por pantalla su es par o impar

num = int(input('Ingrese un numero: '))
if num%2 == 0:
          print(num, 'es un numero par')
else:
          print(num, 'es un numero impar')
          
'''
'''
#Los alumnos del curso se han dividido en dos grupos A y B
#de acuerdo al sexo y el nombre.
#El grupo A esta formado por las mujeres con un nombre anterior a la M
#y los hombres con un nombre posterior a la N
#y el grupo B por el resto.
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que pertence

nom= input('Ingrese su nombre: ')
sex= input('Ingrese su sexo (M o F): ')
if sex == 'f' and nom < 'm':
    print('tu grupo es el A')
elif sex == 'm' and nom > 'n':
    print('tu grupo es el A')
else:
    print('tu grupo es el B')

'''
'''
#tramos impositivos para la declaracion de la renta
#en un determinado pais son los siguientes:

renta=int(input('ingrese su renta anual: '))
if renta < 10000:
    print ('tipo impositivo: 5%')
elif renta >10000 and renta < 20000:
    print('tipo impositivo: 15%')
elif renta >20000 and renta < 35000:
    print('tipo impositivo: 20%')
elif renta >35000 and renta < 60000:
    print('tipo impositivo: 30%')
else:
    print('tipo impositivo: 45%')
    '''
#pizzeria


tipopizza=int(input('1-vege y 2- no-veg: '))
if tipopizza == 1:
    print('*'*50)
    print('Menu veg:')
    print('*'*50)
    print('ingredientes:')
    print('pimiento')
    print('tofu')
    print('*'*50)
    ingrediente = input('Ingrese un Ingrediente: ').lower()
    if ingrediente == 'pimiento' or ingrediente =='tofu':
        print('Los ingredientes de su Pizza Veg son Muzzarella, tomate y',ingrediente)
        print('*'*50)
else:
    print('*'*50)
    print('Menu no-veg')
    print('*'*50)
    print('ingredientes:')
    print('Peperoni')
    print('Jamon')
    print('Salmón')
    print('*'*50)
    ingrediente = input('Ingrese un Ingrediente: ').lower()
    if ingrediente == 'peperoni' or ingrediente =='jamon'or ingrediente =='salmon':
        print('Los ingredientes de su Pizza No Veg son Muzzarella, tomate y',ingrediente)
        print('*'*50)

