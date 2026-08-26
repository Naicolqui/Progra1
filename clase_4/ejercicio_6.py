
def recorrer_alumnos(alumnos):
    for alumno in alumnos:
        print(f"{alumno[0]} nació el día: {alumno[1][0]}-{alumno[1][1]}-{alumno[1][2]}")

def main ():
    alumnos = (
        ("Ana", (12, "Marzo", 2005)),
        ("Bruno", (8, "Julio", 2004)),
        )

    print(f"Ana cumple años en: , {alumnos[0][1][1]}")
    recorrer_alumnos(alumnos)

if __name__ == "__main__":
    main()
