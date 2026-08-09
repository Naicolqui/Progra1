def cargar_sucursal(numero_sucursal):
    print(f"\n--- Carga de datos para la Sucursal {numero_sucursal} ---")
    sucursal = []
    
    #registrar los 7 días de la semana
    while len(sucursal) < 7:
        dia_actual = len(sucursal) + 1
        entrada = input(f"Ingrese la recaudación del día {dia_actual} (>= 0): ")
        
        if entrada.isdigit():
            valor = int(entrada)
            if valor >= 0:
                sucursal.append(valor)
            else:
                print("Error: El valor debe ser mayor o igual a cero.")
        else:
            print("Error: Debe ingresar un número entero válido (no vacío ni texto).")
            
    return sucursal

#________________________________________________________________________________________________
matrizSucursales = []
for i in range(4):
    fila_sucursal = cargar_sucursal(i + 1)
    matrizSucursales.append(fila_sucursal)

print("\nMatriz final de sucursales:", matrizSucursales)

# b) Recaudación total de cada sucursal
recaudacion_sucursales = [sum(sucursal) for sucursal in matrizSucursales]
print(f"b) Recaudación total de cada sucursal: {recaudacion_sucursales}")

# c) Recaudación total de cada día (sumando por columnas)
recaudacion_dias = []
for col in range(7):
    suma_dia = 0
    for fila in range(4):
        suma_dia += matrizSucursales[fila][col]
    recaudacion_dias.append(suma_dia)
print(f"c) Recaudación total de cada día: {recaudacion_dias}")

# d) Recaudación general
recaudacion_general = sum(recaudacion_sucursales)
print(f"d) Recaudación general: {recaudacion_general}")

# e) Número de día con mayor recaudación total
max_recaudacion_dia = max(recaudacion_dias)
dia_mayor = recaudacion_dias.index(max_recaudacion_dia) + 1 
print(f"e) El día con mayor recaudación fue el día {dia_mayor} con un total de {max_recaudacion_dia}")
