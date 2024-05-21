#Escribir un programa que pregunte una
#y otra vez si desea continuar con el programa,
#siempre que se conteste exactamente sí
#( en minúscula y contilde).

while True:
    respuesta = input("¿Desea continuar el programa? (sí): ")
    if respuesta != "sí":
        continue
    else:
        print("¡Ahora sí!")
        break