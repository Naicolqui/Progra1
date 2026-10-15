import csv

ARCHIVO = "entregas.csv"



def crear_archivo():
    try:
        open(ARCHIVO).close()
    except FileNotFoundError:
        with open(ARCHIVO, "w", newline="") as arch:
            csv.writer(arch).writerow(["grupo", "proyecto", "responsable", "avance"])


def validar(fila):
    if len(fila) != 4:
        raise ValueError("cantidad de campos incorrecta")
    grupo = int(fila[0])
    avance = float(fila[3])
    if grupo <= 0 or fila[1].strip() == "" or fila[2].strip() == "" or avance < 0 or avance > 100:
        raise ValueError("datos vacíos o fuera de rango")
    return {"grupo": grupo, "proyecto": fila[1], "responsable": fila[2], "avance": avance}



def leer_entregas():
    entregas = []
    with open(ARCHIVO, newline="") as arch:
        filas = list(csv.reader(arch))
    for fila in filas[1:]:  # salteamos el encabezado
        try:
            entregas.append(validar(fila))
        except ValueError as error:
            print("Registro omitido:", fila, "->", error)
    return entregas



def buscar(entregas, grupo):
    for e in entregas:
        if e["grupo"] == grupo:
            return e
    return None



def cargar_entrega(entregas):
    fila = [input("Grupo: "), input("Proyecto: "), input("Responsable: "), input("Avance: ")]
    try:
        entrega = validar(fila)
    except ValueError as error:
        print("Datos inválidos:", error)
        return
    if buscar(entregas, entrega["grupo"]) is not None:
        print("Ese grupo ya tiene una entrega cargada.")
        return
    with open(ARCHIVO, "a", newline="") as arch:
        csv.writer(arch).writerow(fila)
    entregas.append(entrega)
    print("Entrega cargada.")



def mostrar(e):
    print(e["grupo"], "-", e["proyecto"], "-", e["responsable"], "-", e["avance"], "%")



def bajo_avance(entregas):
    resultado = []
    for e in entregas:
        if e["avance"] < 50:
            resultado.append(e)
    return resultado



def promedio(entregas):
    if len(entregas) == 0:
        return None
    total = 0
    for e in entregas:
        total += e["avance"]
    return total / len(entregas)




def main():
    crear_archivo()
    entregas = leer_entregas()

    while input("¿Cargar una entrega? (s/n): ") == "s":
        cargar_entrega(entregas)

    print("\n--- Entregas válidas ---")
    for e in entregas:
        mostrar(e)

    print("\n--- Búsqueda por grupo ---")
    encontrada = buscar(entregas, int(input("Grupo a buscar: ")))
    if encontrada is None:
        print("No se encontró ese grupo.")
    else:
        mostrar(encontrada)

    print("\n--- Avance menor al 50 % ---")
    for e in bajo_avance(entregas):
        mostrar(e)

    print("\n--- Promedio de avance ---")
    prom = promedio(entregas)
    if prom is None:
        print("No hay registros válidos.")
    else:
        print(round(prom, 2), "%")


main()
