# Conclusiones — TP02 Robot Unitree Go2

## Nivel máximo alcanzado
- [x] Nivel 1 — Python reconocido
- [x] Nivel 2 — MuJoCo importado correctamente (`mujoco 3.14.0`)
- [x] Nivel 3 — Modelos Go2 disponibles
- [x] Nivel 4 — Verificación del entorno correcta
- [x] Nivel 5 — Ventana MuJoCo abierta (con `mjpython`, ver PROBLEMAS.md #2)
- [x] Nivel 6 — Go2 visible
- [x] Nivel 7 — Programa conectado al simulador
- [x] Nivel 8 — MISION_BASICA ejecutada (4/4 comandos OK)
- [x] Nivel 9 — MISION_CON_ERRORES procesada sin abortar (4 ejecutados, 7
  omitidos correctamente, cada uno con su motivo)
- [x] Nivel 10 — Reporte final generado (para las tres misiones y la misión
  propia)

**Nivel máximo alcanzado: 10/10.**

## a) ¿Cuál fue la principal dificultad de instalación?
El paquete `mujoco` no estaba instalado en el entorno de Python usado
(gestionado con pyenv). Es un paso previo obligatorio antes de poder abrir el
simulador.

## b) ¿Qué error requirió mayor investigación?
El simulador arrancaba (proceso vivo, archivo de estado generado) pero **no
mostraba ninguna ventana** y no imprimía ningún error, lo cual era más difícil
de diagnosticar que un traceback explícito. También llevó investigación
entender la diferencia entre la consigna del PDF original (`distancia`,
`ángulo`, `sentido`) y la API real vigente en el repositorio (`velocidad`,
`tiempo`).

## c) ¿Qué solución resultó efectiva y por qué?
Para el problema de la ventana: revisar el código de `entorno/sim/visor.py` y
notar que usa `mujoco.viewer.launch_passive`, que en macOS requiere el
ejecutable `mjpython` (distribuido junto con el paquete `mujoco`) en vez del
`python3` estándar, porque el visor necesita controlar el hilo principal de
una forma específica del sistema operativo. Relanzar el simulador con
`mjpython -m sim --robot go2 --materia tp02` resolvió el problema al
instante. Para la API: leer directamente el código fuente
(`safety.py`, `robot.py`, `mi_tp02.py`, `misiones.py`) en vez de guiarse solo
por el PDF, porque el orientador aclara explícitamente que prevalece la
plantilla vigente del repositorio.

## d) ¿Qué intento no funcionó y qué aprendieron de él?
Ejecutar el simulador con `python3 -m sim ...` (el intérprete "normal") no
funcionó en macOS: el proceso corría sin errores pero la ventana 3D nunca
aparecía. Aprendizaje: un proceso "vivo sin errores" no es sinónimo de
"funcionando correctamente" — hay que verificar también el efecto esperado
(la ventana), no solo la ausencia de excepciones. También: siempre revisar si
una librería gráfica exige un entrypoint especial en macOS antes de asumir
que el launcher genérico del proyecto (`INICIAR_SIMULADOR.sh`) contempla
todos los sistemas operativos.

## e) Diferencia entre una guía antigua y la arquitectura actual
Ver detalle en `BITACORA.md`, punto (e).

## f) ¿Hasta qué nivel lograron avanzar?
Nivel 10/10: se llegó a generar el reporte final de las tres misiones de
prueba (`MISION_BASICA`, `MISION_CON_ERRORES`) y de una misión propia, con el
simulador del Go2 corriendo y el controlador conectado a él.

## g) Próximo paso si se continuara trabajando
`MISION_CUADRADO` ya se probó (9/9 comandos ejecutados: 4 tramos de
avanzar+girar 90° y detenerse), confirmando que el controlador reproduce
correctamente un recorrido cerrado. Como siguiente paso, documentar
`INICIAR_SIMULADOR.sh` para que en macOS invoque `mjpython` automáticamente
en lugar de `python3` (mejora reportable a la cátedra), y evaluar la
demostración supervisada en el robot físico si el equipo docente lo habilita.
