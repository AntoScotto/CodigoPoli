#Escriba un programa que solicite una contraseña ( el texto de la contraseña
#no es importante) y la vuelva solicitar hasta que las dos contraseñas
#coinciden.

contraseña1='anto'

while True:
    contraseña2=input('ingrese la contraseña:')
    if contraseña2 != contraseña1:
        print('Las contraseñas no coinciden')
        continue
    else:
        print('las contraseñas coinciden')
        break
    
    
intento 2
contraseña1 = input("Ingrese su contraseña: ")
contraseña2 = input("Confirme su contraseña: ")

while contraseña1 != contraseña2:
    print("Las contraseñas no coinciden ingrese de nuevo la contraseña: ")
    contraseña2 = input("Confirme su contraseña: ")

print("Las contraseñas coinciden")