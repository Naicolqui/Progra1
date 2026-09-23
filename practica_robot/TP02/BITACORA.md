# Bitácora técnica — TP02 Robot Unitree Go2

## a) ¿Qué herramientas necesita el TP?
Python 3.10+, el paquete `mujoco`, `pip`, y opcionalmente `git` para clonar el
repositorio de la cátedra. Editor: VS Code.

## b) ¿Qué versión de Python se requiere?
Python 3.10 o superior (usamos 3.12.13).

## c) ¿Qué componentes ya están instalados en la computadora?
Python 3.12.13, pip 25.0.1 y git 2.39.5 ya estaban disponibles. `mujoco` NO
estaba instalado (`ModuleNotFoundError: No module named 'mujoco'`).

## d) ¿Qué componentes del repositorio oficial de Unitree no son necesarios?
No hace falta CycloneDDS ni el SDK oficial de Unitree (`unitree_sdk2py`). El
laboratorio UADE trae su propio simulador (`entorno/sim`) que se comunica por
socket local (127.0.0.1), sin depender del SDK real.

## e) Diferencias entre el TP en PDF y la versión actual del repositorio
- El PDF de consigna (`TP02_Programacion_I.pdf`) describe comandos con
  `distancia/velocidad` y `ángulo/sentido` ("izquierda"/"derecha"), y nombres
  de función `procesar_comando`, `ejecutar_mision`, `generar_reporte`,
  `inicializar_robot`.
- La plantilla real del repositorio (`mi_desarrollo/mi_tp02.py`) usa la API
  vigente basada en **velocidad y tiempo** (`robot.avanzar(velocidad, tiempo)`,
  `robot.girar(velocidad, tiempo)`), con funciones `comando_es_valido`,
  `ejecutar_comando`, `ejecutar_mision`, `generar_reporte` (sin
  `inicializar_robot` separado: `Robot()` + `conectar()` ya están resueltos en
  `main()`), y un comando adicional `saludar` en lugar de `saludo`.
- Se respetó la plantilla actual del repositorio, como indica el orientador
  (punto 15).

## Registro de acciones

| Nº | Acción / comando | Resultado | Problema | Solución intentada | Estado |
|----|-------------------|-----------|----------|---------------------|--------|
| 1 | `python3 --version` | `Python 3.12.13` | — | — | RESUELTO |
| 2 | `git clone https://github.com/tsamaan/UadeRobotLab.git` | Clonado en `practica_robot/UadeRobotLab` | — | — | RESUELTO |
| 3 | `python3 -c "import mujoco; print(mujoco.__version__)"` | `ModuleNotFoundError: No module named 'mujoco'` | MuJoCo no instalado | Ejecutar `python3 -m pip install mujoco` según `INSTALACION.md` | PENDIENTE (ver PROBLEMAS.md) |
| 4 | Lectura de `entorno/sim/safety.py` | Perfil `tp02`: vel_max=0.20 m/s, vel_angular_max=0.50 rad/s, duración_max=10s, batería_min=25% | — | — | RESUELTO |
| 5 | Escritura de `mi_desarrollo/mi_tp02.py` (4 funciones) | Compila sin errores (`py_compile`) | — | — | RESUELTO |
| 6 | `python3 -m pip install mujoco` | Instalado `mujoco 3.14.0` | — | — | RESUELTO |
| 7 | `python3 -m sim --robot go2 --materia tp02` (desde `entorno/`) | Proceso corría, `.simulador_activo.json` generado, pero sin ventana 3D visible | Visor de MuJoCo no abre ventana en macOS con `python3` normal | Relanzar con `mjpython -m sim --robot go2 --materia tp02` | RESUELTO (ver PROBLEMAS.md #2) |
| 8 | `python3 mi_desarrollo/mi_tp02.py` (con simulador ya abierto vía mjpython) | Conectado a Go2, `MISION_BASICA` 4/4 OK | — | — | RESUELTO |
| 9 | Misma ejecución, `MISION_CON_ERRORES` | 4 ejecutados / 7 omitidos, cada uno con motivo correcto | — | — | RESUELTO |
| 10 | Misma ejecución, misión propia (6 comandos, 1 inválido) | 5 ejecutados / 1 omitido por velocidad angular excedida | — | — | RESUELTO |

| 11 | `MISION_CUADRADO` (mismo simulador, mismas funciones) | 9/9 comandos OK: 4 tramos avanzar+girar 90° + detenerse | — | — | RESUELTO |

Salida completa de consola guardada en `evidencias/06_misiones/salida_consola_mi_tp02.txt`
y `evidencias/06_misiones/salida_consola_mision_cuadrado.txt`.
