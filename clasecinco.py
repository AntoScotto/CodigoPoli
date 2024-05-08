#estructura condicional
#estructura
#if expresión logica:
#..
#else:
#...

#ejercicio 26
#entrada
#n1/n2
#proceso, if n1>n2 mayor=n1 menor=n2 else:mayor=n2 menor=n1
#salida
#menor/mayor

#Pseudo codigo
#Inicio:
#1- ingresar n1 yn2
#2-ordenarlos
#3-mostrarlos de menor a mayor
'''
n1=int(input('ingrese n1 :'))
n2=int(input('ingrese n2 :'))
if n1 > n2:
    mayor=n1
    menor=n2
else:
    mayor=n2
    menor=n1
    
print(menor,mayor)
'''
'''
#Actividad27
n1=int(input('ingrese n1:'))
n2=int(input('ingrese n2:'))
n3=int(input('ingrese n3:'))
suma=n1+n2+n3
if suma>10:
    print(suma/2)
else:
    print(suma**2)
'''
'''
#Actividad28

turno = int(input('ingrese turno: '))
horas= float(input('ingrese cantidad de horas trabajadas :'))
t1= 1
t2= 2
htd=5234
htn=8075.75
if turno == t1:
    print('El pago por las horas trabajadas son: ', horas*htd)
elif turno == t2:
     print('El pago por las horas trabajadas son: ',horas*htn)
else:
    print('Opción de turno NO valida')
    
'''