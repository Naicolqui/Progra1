# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  Nombre y apellido:  Nicole Quilmore
#  Comision:           .....................................
#
#  Este archivo es una copia resuelta de:
#  UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/mi_desarrollo/mi_tp02.py
#
#  Para ejecutarlo:
#    1. Abrir INICIAR_SIMULADOR (elegir 2 - Go2) desde
#       UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/
#    2. Esperar a que aparezca la ventana de MuJoCo con el robot
#    3. Copiar/pegar este archivo en mi_desarrollo/mi_tp02.py (o ejecutarlo
#       desde ahi) y correrlo con: python mi_desarrollo/mi_tp02.py
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO

# Nombres de comando validos y cuantos parametros numericos llevan cada uno.
COMANDOS_VALIDOS = {
    "avanzar": 2,
    "girar": 2,
    "detenerse": 0,
    "saludar": 0,
}


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)
    """
    if not isinstance(comando, tuple) or len(comando) == 0:
        return False

    nombre = comando[0]
    if nombre not in COMANDOS_VALIDOS:
        return False

    params = comando[1:]
    cantidad_esperada = COMANDOS_VALIDOS[nombre]
    if len(params) != cantidad_esperada:
        return False

    if nombre in ("avanzar", "girar"):
        velocidad, tiempo = params
        # bool es subclase de int: se descarta explicitamente para no
        # aceptar True/False como si fueran numeros validos.
        if isinstance(velocidad, bool) or not isinstance(velocidad, (int, float)):
            return False
        if isinstance(tiempo, bool) or not isinstance(tiempo, (int, float)):
            return False
        if tiempo < 0:
            return False

    return True


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso."""
    nombre = comando[0]
    params = comando[1:]

    try:
        if nombre == "avanzar":
            velocidad, tiempo = params
            robot.avanzar(velocidad=velocidad, tiempo=tiempo)
            return f"avanzar(velocidad={velocidad}, tiempo={tiempo}) ejecutado"
        elif nombre == "girar":
            velocidad, tiempo = params
            robot.girar(velocidad=velocidad, tiempo=tiempo)
            return f"girar(velocidad={velocidad}, tiempo={tiempo}) ejecutado"
        elif nombre == "detenerse":
            robot.detenerse()
            return "detenerse() ejecutado"
        elif nombre == "saludar":
            robot.saludar()
            return "saludar() ejecutado"
    except ErrorDeSeguridad as error:
        return f"RECHAZADO por seguridad: {error}"


# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Un comando invalido no corta la mision: se registra y se sigue.
    """
    for comando in mision:
        if not comando_es_valido(comando):
            historial.append({
                "comando": comando,
                "ejecutado": False,
                "motivo": "Comando invalido (nombre, cantidad o tipo de parametros)",
            })
            continue

        resultado = ejecutar_comando(robot, comando)
        ejecutado = not resultado.startswith("RECHAZADO")
        historial.append({
            "comando": comando,
            "ejecutado": ejecutado,
            "motivo": "" if ejecutado else resultado,
        })


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision."""
    total = len(historial)
    ejecutados = sum(1 for r in historial if r["ejecutado"])
    omitidos = total - ejecutados

    print("=" * 40)
    print(" REPORTE DE MISION")
    print("=" * 40)
    print(f" Comandos recibidos:  {total}")
    print(f" Comandos ejecutados: {ejecutados}")
    print(f" Comandos omitidos:   {omitidos}")
    print("-" * 40)
    for registro in historial:
        estado = "OK" if registro["ejecutado"] else "OMITIDO"
        linea = f" [{estado}] {registro['comando']}"
        if registro["motivo"]:
            linea += f" -> {registro['motivo']}"
        print(linea)
    print("=" * 40)


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        ejecutar_mision(robot, MISION_BASICA, historial)
        generar_reporte(historial)

        historial_errores = []
        ejecutar_mision(robot, MISION_CON_ERRORES, historial_errores)
        generar_reporte(historial_errores)

        # Misión propia: al menos 5 comandos, con un error intencional.
        mision_propia = [
            ("avanzar", 0.15, 2.0),
            ("girar", 0.5, 1.57),       # 90 grados a la izquierda
            ("avanzar", 0.15, 2.0),
            ("girar", 5.0, 1.0),        # MAL: supera velocidad angular max
            ("saludar",),
            ("detenerse",),
        ]
        historial_propia = []
        ejecutar_mision(robot, mision_propia, historial_propia)
        generar_reporte(historial_propia)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
