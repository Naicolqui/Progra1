# 5. Modificación de listas mediante slicing 
# Las rebanadas también pueden aparecer del lado izquierdo de una asignación. En ese caso permiten reemplazar, 
# eliminar o insertar varios elementos consecutivos. Resuelvan cada inciso partiendo de una copia nueva de la lista 
# original.    numeros = [2, 4, 6, 8, 10, 12, 14]
# a) Reemplazar 6 y 8 por 60 y 80. 
# b) Eliminar 10 y 12. 
# c) Insertar 100 y 200 entre 4 y 6 utilizando una rebanada nula. 
# d) Agregar tres valores al comienzo. 
# e) Vaciar la lista utilizando una rebanada.

numeros = [2, 4, 6, 8, 10, 12, 14]
print(f'lista original {numeros}')
numeros[2:4] = [60, 80]
print(f'Reemplazar 6 y 8 por 60 y 80. {numeros}')
numeros[4:6] = []
print(f'Eliminar 10 y 12{numeros}')
numeros[2:2] = [100,200]
print(f'Insertar 100 y 200 entre 4 y 6 con rebanada nula{numeros}')
numeros[0:0]=[18,12,2022]
print(f'agregamos al inicio de la lista los valores 18,12,2022 {numeros}')
numeros[::] = []
print(f'vaciar lista con rebanada{numeros}')