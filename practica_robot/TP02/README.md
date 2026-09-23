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
1. Instalar dependencias según `UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/INSTALACION.md`.
2. Abrir el simulador:
   ```
   cd UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I
   ./INICIAR_SIMULADOR.sh
   ```
   Elegir `2 - Go2` y esperar a que abra la ventana de MuJoCo.

   **Nota (macOS):** el script usa `python3` internamente, pero el visor de
   MuJoCo (`mujoco.viewer.launch_passive`) en macOS necesita correr en el
   hilo principal a través del ejecutable `mjpython` (incluido con el
   paquete `mujoco`). Si el proceso arranca pero no aparece ninguna ventana,
   lanzarlo manualmente así en su lugar (ver `PROBLEMAS.md` #2):
   ```
   cd UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/entorno
   mjpython -m sim --robot go2 --materia tp02
   ```
3. En otra terminal, ejecutar el controlador (ya copiado en `mi_desarrollo/mi_tp02.py`):
   ```
   python3 mi_desarrollo/mi_tp02.py
   ```
   O el equivalente `EJECUTAR_MI_CODIGO.sh`.

El código fuente entregado también está en `codigo/tp02_quilmore.py` (copia
idéntica a la que se ejecuta desde `mi_desarrollo/`).

## Estructura de la entrega
```
TP02_Quilmore/
├── README.md
├── BITACORA.md
├── PROBLEMAS.md
├── CONCLUSIONES.md
├── codigo/
│   └── tp02_quilmore.py
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
