# Registro y análisis de problemas — TP02

## Problema Nº 1

**Qué se estaba intentando hacer:** Verificar que MuJoCo esté disponible antes
de abrir el simulador.

**Comando ejecutado:**
```
python3 -c "import mujoco; print(mujoco.__version__)"
```

**Resultado esperado:** Que imprima el número de versión instalado.

**Resultado obtenido:**
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'mujoco'
```

**Mensaje de error:** `ModuleNotFoundError: No module named 'mujoco'`

**Interpretación del grupo:** El paquete `mujoco` nunca fue instalado en este
entorno de Python (entorno gestionado con pyenv, versión 3.12.13).

**Hipótesis sobre la causa:** Instalación limpia de la máquina; `INSTALACION.md`
indica que hay que instalarlo manualmente con pip, no viene con Python base.

**Solución 1 intentada y resultado:**
```
python3 -m pip install mujoco
```
Instaló correctamente `mujoco 3.14.0`. Verificado con:
```
python3 -c "import mujoco; print(mujoco.__version__)"
→ 3.14.0
```

**Solución 2 intentada y resultado:** No fue necesaria.

**Estado final:** RESUELTO.

**Evidencia:** Ver `evidencias/02_instalacion/`.

---

## Problema Nº 2

**Qué se estaba intentando hacer:** Abrir el simulador con
`INICIAR_SIMULADOR.sh` (Go2) para dejarlo corriendo mientras se ejecuta el
controlador de misiones.

**Comando ejecutado:**
```
cd entorno
python3 -m sim --robot go2 --materia tp02
```

**Resultado esperado:** Que se abra una ventana de MuJoCo mostrando al robot
Go2 en la escena 3D.

**Resultado obtenido:** El proceso arrancaba y quedaba corriendo (visible con
`ps aux`, usando CPU), se generaba correctamente
`entorno/sim/.simulador_activo.json` con `robot: "go2"`, `materia: "tp02"`,
`puerto: 8765`, pero **no aparecía ninguna ventana 3D** en pantalla. Tampoco
había mensajes de error en la salida estándar ni en el log.

**Mensaje de error:** Ninguno explícito — el proceso no fallaba ni imprimía
nada, simplemente no mostraba ventana.

**Interpretación del grupo:** El visor de MuJoCo
(`mujoco.viewer.launch_passive`, usado en `entorno/sim/visor.py`) necesita
correr en el **hilo principal** del proceso. En macOS, el intérprete estándar
de Python (`python3`) no le cede a MuJoCo el control del hilo principal de la
forma que el visor 3D requiere (a diferencia de Linux/Windows), por lo que la
librería `mujoco` distribuye un ejecutable especial llamado `mjpython`
pensado exactamente para esto.

**Hipótesis sobre la causa:** El script `INICIAR_SIMULADOR.sh` ejecuta
siempre `"$PYTHON" -m sim ...` con el primer intérprete de Python que
encuentra (`python3`), sin distinguir sistema operativo. En Linux/Windows eso
alcanza; en macOS falta invocar `mjpython` en su lugar, así que el visor se
inicializa "en silencio" sin poder abrir la ventana del sistema.

**Solución 1 intentada y resultado:** Matar el proceso lanzado con `python3`
y relanzar manualmente el mismo módulo con `mjpython`:
```
mjpython -m sim --robot go2 --materia tp02
```
**Resultado: FUNCIONÓ.** La ventana de MuJoCo con el Go2 apareció
correctamente en pantalla.

**Solución 2 intentada y resultado:** No fue necesaria.

**Estado final:** RESUELTO.

**Evidencia:** Captura de la ventana "MuJoCo : go2 - escena limpia UADE" con
el robot Go2 visible sobre la grilla, guardada en
`evidencias/05_gemelo_digital/ventana_mujoco_go2.png`.

> **Nota para próximos grupos que usen macOS:** conviene reemplazar
> directamente `python3 mi_desarrollo/mi_tp02.py` por el intérprete normal
> (el controlador en sí no abre ventana, solo se conecta por socket, así que
> no necesita `mjpython`); lo que sí requiere `mjpython` es exclusivamente el
> **simulador** (`INICIAR_SIMULADOR.sh` / `python -m sim`), porque es el que
> abre la ventana 3D.

---

## Problema Nº 3

**Qué se estaba intentando hacer:** Verificar visualmente que
`robot.saludar()` (llamado desde `ejecutar_comando`) produce una animación
en el Go2 dentro del simulador.

**Comando ejecutado:**
```python
from robot import Robot
from mi_tp02 import ejecutar_comando

robot = Robot()
robot.conectar()
resultado = ejecutar_comando(robot, ('saludar',))
print(resultado)
```

**Resultado esperado:** El robot levanta la pata delantera izquierda (pose
`saludo` definida en `entorno/sim/robots.py` para el Go2) durante unos
segundos.

**Resultado obtenido:** El programa imprime `saludar() ejecutado` (sin
ningún error ni excepción), pero el robot en la ventana de MuJoCo **no se
mueve**.

**Mensaje de error:** Ninguno — la llamada se completa exitosamente desde el
punto de vista del código del alumno.

**Interpretación del grupo:** El problema no está en `comando_es_valido` ni
en `ejecutar_comando`: ambos funcionan como se espera (el comando es válido,
se llama a `robot.saludar()`, no se lanza `ErrorDeSeguridad`). El problema
está más adentro, en el propio simulador.

**Hipótesis sobre la causa:** Se rastreó el camino completo de la orden:

1. `robot.saludar()` (en `entorno/sim/robot.py:346`) llama a
   `self._cliente.WaveHand()`.
2. `WaveHand()` (en `entorno/sim/local.py:258`) manda por socket
   `{"orden": "gesto", "nombre": "saludo"}` — con el nombre **`"saludo"`**.
3. El servidor recibe eso y ejecuta `self.mundo.gesto("saludo", 2.0)`
   (`local.py:162`), que guarda `self.accion = "saludo"` durante 2 segundos.
4. Pero quien dibuja la pose del saludo revisa
   `if e["accion"] in ("saludando", "besando")` (en `arrancar.py:293` y
   `visor.py:59`) — es decir, espera el string **`"saludando"`**, no
   `"saludo"`.

Como `"saludo" != "saludando"`, la condición nunca se cumple y la pose
jamás se aplica, aunque el pedido se procesó "OK" en todos los pasos
intermedios. Como evidencia adicional de que es un bug de nombres y no de
lógica: en `entorno/sim/servicio_sport_go2.py:89` (el camino que se usa por
DDS con el robot físico) el mismo gesto se dispara con
`self.mundo.gesto("saludando")` — ahí sí con el nombre correcto. Es una
inconsistencia entre los dos transportes (`local.py` vs.
`servicio_sport_go2.py`) del propio simulador de la cátedra.

**Solución 1 intentada y resultado:** No se modificó el simulador (fuera del
alcance del TP; el enunciado pide no tocar `robot.py`, y `local.py` es
código interno del laboratorio, no del alumno). Se documenta como hallazgo
de diagnóstico: el comando `saludar` funciona correctamente del lado del
controlador (se valida, se ejecuta, no lanza excepciones); la falta de
animación visible es un bug de nomenclatura interno del simulador
(`"saludo"` vs. `"saludando"`), ajeno al código entregado.

**Solución 2 intentada y resultado:** No se aplicó ninguna, por lo indicado
arriba.

**Estado final:** NO RESUELTO (a nivel simulador) — pero identificado,
explicado y no atribuible al controlador de misiones. `ejecutar_comando`
se considera correcto: reporta `"saludar() ejecutado"` porque el pedido al
robot no lanzó ningún error, que es exactamente el contrato esperado.

**Evidencia:** Salida de consola confirmando `saludar() ejecutado` sin
excepciones, y lectura de código fuente citada arriba (`robot.py`,
`local.py`, `arrancar.py`, `visor.py`, `servicio_sport_go2.py`).
