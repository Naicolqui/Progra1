


def mostrar_alumnos():
    try:
       
        arch = open("alumnos.txt", "rt", encoding="utf-8")
    except OSError as error:
        print("No se pudo abrir el archivo:", error)
    else:
        nro_linea = 0
        validos = 0
        invalidos = 0
        legajos_mayores = []   
        por_comision = {}       

        print("\n Alumnos válidos:")
        for linea in arch:                      
            nro_linea += 1
            linea = linea.rstrip("\n")         
            campos = linea.split(";")

           
            if len(campos) != 3:
                invalidos += 1
                print("  [Línea", nro_linea, "inválida: se esperaban 3 campos] ->", linea)
            else:
                legajo, nombre, comision = campos
                try:
                    legajo = int(legajo)
                    comision = int(comision)
                except ValueError:
                    invalidos += 1
                    print("  [Línea", nro_linea, "inválida: legajo o comisión no numéricos] ->", linea)
                else:
                    if legajo <= 0 or nombre.strip() == "" or comision < 1 or comision > 10:
                        invalidos += 1
                        print("  [Línea", nro_linea, "inválida: datos fuera de rango o vacíos] ->", linea)
                    else:
                        
                        validos += 1
                        print("Legajo:", legajo, "| Nombre:", nombre, "| Comisión:", comision)

                        
                        if legajo > 10000:
                            legajos_mayores.append((legajo, nombre))

                        
                        if comision in por_comision:
                            por_comision[comision] += 1
                        else:
                            por_comision[comision] = 1

        
        arch.close()

        print("\n Registros válidos:", validos, "\n  Registros inválidos:", invalidos)

        print("\n Alumnos con legajo mayor a 10000:")
        if len(legajos_mayores) == 0:
            print("No hay alumnos con legajo mayor a 10000")
        for legajo, nombre in legajos_mayores:
            print("Legajo:", legajo, "| Nombre:", nombre)

        print("\n Alumnos por comisión: ")
        if len(por_comision) == 0:
            print("No hay registros válidos.")
        for comision in sorted(por_comision):
            print("Comisión", comision, ":", por_comision[comision] )


mostrar_alumnos()