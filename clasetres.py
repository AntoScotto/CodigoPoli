'''
#Act11

#Entrada
votosc1 = int(input('ingrese votos candidato 1: '))
votosc2 = int(input('ingrese votos candidato 2: '))

#Proceso
totalv = votosc1+votosc2
pc1 = (votosc1*100)/totalv
pc2 = (votosc2*100)/totalv
#Salida

print('porcentaje candidato 1: ',pc1)
print('porcentaje candidato 2: ',pc2)
'''

#Act12
#sumarNum-pendiente

#Act13
# a-porc b-area c-vmin d-dens e-cnum f-naOper 6-emailemp

#Act14
# a-float b-int c-int d-string e-bool


#Act17

'''
num 1 m 50 n10 p5

a-10/5+3
b-50/5+10*1
c-50-3*10+4*1
d-1/5
e-18/5
f--5*10
g--50/20
h-(50-10)/(5+1)
i-50+10/5+1
'''
#Act18
'''
print('Respuesta1 es el entero',9/4)
print('Respuesta1 es el entero',17/3)


print('El residuo de 9 dividido entre 4 es:',9%4)
print('El residuo de 17 dividido entre 3 es:',17%3)
'''
'''
#Act22
apellido = str(input('ingrese apellido del alumno:'))
nombre = str(input('ingrese nombre del alumno:'))
dominio = '@tdf.edu.ar'

nyamin = apellido.lower()+'_'+nombre.lower()
email = nyamin+dominio

print('El email del alumno es:',email)
'''
'''
#Act23
cordros= 400
kmh=122

crt= cordros/kmh

print('el tiempo estimado de viaje es de:',round(crt,2))
#Act24

'''


               #CLASE 3
'''
a=2
b=3

#suma
suma = a+b
#resta
resta = a-b
#producto
prod = a*b
#division decimal
divDecimal = a/b
#division entera
divEntera = a//b
#resto
resto =a%b
#Potencia
potencia = a**b

'''
'''
nom = input('ingrese nombre: ')
apellido= input('ingrese apellido: ')
datos = 'Tus datos son:'
dni= int(input('Ingrese DNI: '))
edad= int(input('Ingrese edad: '))
tel= int(input('Ingrese Telefono: '))
ciudad= input('Ingrese Ciudad: ')

saludo = 'Bienvenido '+ apellido.upper() + ' '+ nom.capitalize() + ' al Curso de Diseño Web!'
print('^'*50)
print(saludo)
print('^'*50)
print(datos)
print('DNI:',dni)
print('Telefono:',tel)
print('Ciudad: ',ciudad.capitalize())
print('^'*50)

'''
                    




