# TP02 — Programación I · Controlador de misiones (Robot Unitree Go2)

## Integrante
- Nicole Quilmore

## Descripción
Programa modular en Python que ejecuta una misión (lista de comandos) sobre el
robot simulado Unitree Go2, validando cada comando, registrando el resultado
en un historial y generando un reporte final. Sigue el diseño Top-Down pedido
en la consigna: `comando_es_valido`, `ejecutar_comando`, `ejecutar_mision`,
`generar_reporte`.

## Fuente utilizada
Repositorio de la cátedra: https://github.com/tsamaan/UadeRobotLab.git
(carpeta `05LaboratoriosTPs/TP02_Programacion_I`), clonado dentro de esta
misma carpeta `practica_robot/UadeRobotLab`.

Se usó exclusivamente la modalidad **simulada con MuJoCo** (sin CycloneDDS ni
SDK oficial de Unitree, tal como indica el orientador).

## Cómo ejecutar
1. Instalar dependencias según `UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/INSTALACION.md`
   (resumen: `python3 -m pip install mujoco`).

2. Abrir el simulador (macOS — requiere `mjpython`, ver nota abajo):
   ```
   cd UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/entorno
   mjpython -m sim --robot go2 --materia tp02
   ```
   Esperar a que aparezca la ventana "MuJoCo : go2 - escena limpia UADE" con
   el robot Go2 visible. Dejarla abierta.

   **Nota:** `INICIAR_SIMULADOR.sh` lanza el simulador con `python3` a
   secas, que funciona en Linux/Windows pero **no en macOS**: el visor de
   MuJoCo (`mujoco.viewer.launch_passive`) necesita correr en el hilo
   principal, y en Mac eso solo lo logra el ejecutable `mjpython`
   (incluido con el paquete `mujoco`). Con `python3` el proceso queda vivo
   pero nunca aparece ninguna ventana — usar siempre `mjpython -m sim ...`
   directamente, como arriba (ver `PROBLEMAS.md` #2).

3. En otra terminal, con el simulador ya abierto, ejecutar el controlador
   (ya copiado en `mi_desarrollo/mi_tp02.py`):
   ```
   cd UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I
   python3 mi_desarrollo/mi_tp02.py
   ```

4. Para cerrar el simulador: `Ctrl+C` en su terminal, o cerrar la ventana.

El código fuente entregado también está en `codigo/tp02.py` (copia
idéntica a la que se ejecuta desde `mi_desarrollo/mi_tp02.py`).

## Estructura de la entrega
```
TP02/
├── README.md
├── BITACORA.md
├── PROBLEMAS.md
├── CONCLUSIONES.md
├── codigo/
│   └── tp02.py
└── evidencias/
    ├── 01_entorno/
    ├── 02_instalacion/
    ├── 03_errores/
    ├── 04_soluciones/
    ├── 05_gemelo_digital/
    └── 06_misiones/
```

## Límites de seguridad aplicados (perfil `tp02`)
- Velocidad máxima: 0.20 m/s
- Velocidad angular máxima: 0.50 rad/s
- Duración máxima por comando: 10 s
- Batería mínima: 25 %

## Nivel de avance alcanzado
Ver `CONCLUSIONES.md`.
