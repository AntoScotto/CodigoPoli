#Leer números enteros del teclado, hasta que el usuario ingrese 0. Finalmente,
#mostrar la sumatoria de todos los números ingresados.


while True:
    numero=int(input('ingrese un numero por favor: '))
    if numero !=0:
        print('ingrese otro numero')
        continue
    else:
        print('Ingresó el numero correcto!')
        break
suma=0
numero=int(input('ingrese un numero por favor(0 para finalizar): '))

while numero !=0:
    suma+=numero
    numero=int(input('ingrese otro numero por favor: '))

print('la suma de los numeros que ingreso es:',suma)