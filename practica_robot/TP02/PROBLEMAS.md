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
