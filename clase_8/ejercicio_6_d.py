import re


patron_anio = re.compile(r"[0-9]{4}")
fechas = "07/08/2017|03/02/1984|17/03/2001"
print( patron_anio.findall(fechas))
