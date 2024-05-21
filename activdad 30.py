#ACT30:Cargar por teclado tres números enteros que se supone representan las
#edades de tres personas. Determinar si alguno de los valores cargados es
#negativo, en cuyo caso informe en pantalla con un mensaje tal como:
#“Alguna es incorrecta: negativo”. Si todos los valores son positivos o cero,
#informe que todos son correctos.
  
edad1=int(input('ingrese edad1:'))
edad2=int(input('ingrese edad2:'))
edad3=int(input('ingrese edad3:'))
if edad1<0 or edad2<0 or edad3<0:
    print('alguna de las edades es negativa')
else:
    print('todos los valores son correctos')