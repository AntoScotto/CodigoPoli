#Leer números enteros de teclado, hasta que el usuario ingrese el 0.
#Finalmente mostrar
#la sumatoria de todos los números positivos ingresados

suma=0
numero=int(input('ingrese un numero por favor(0 para finalizar): '))

while numero !=0:
    if numero >0:
        suma+=1
    numero=int(input('ingrese otro numero por favor: '))

print('la suma de los numeros que ingreso es:',suma)