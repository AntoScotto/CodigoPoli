
#ejercicio31
nomes=input('nombre del estudiante: ')
nompro=input('nombre del docente: ')
pro=float(input('ingrese promedio del estudiante: '))
#forma1
t1='est.','prof.'
print(nomes,t1[0])
print(nompro,t1[1])
print('promedio notas:',round(pro))

#forma 2

datos=(nomes,nompro,pro)
print('est.',datos[0],'prof.',datos[1],'promedio:',round(pro))
