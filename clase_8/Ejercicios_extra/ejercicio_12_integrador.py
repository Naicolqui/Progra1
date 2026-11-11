
import re

cliente = "MEV-458 | maria@gmail.com | 21/09/2026 | $1250"

print("Dato a analizar:")
print(cliente)


# ------------------------------------------------------------
# 1. CÓDIGO
# ------------------------------------------------------------

patron_codigo = r"[A-Z]{3}-\d{3}"

resultado_codigo = re.search(patron_codigo, cliente)


# ------------------------------------------------------------
# 2. CORREO
# ------------------------------------------------------------

patron_correo = r"[\w.]+@[\w.]+"

resultado_correo = re.search(patron_correo, cliente)


# ------------------------------------------------------------
# 3. FECHA
# ------------------------------------------------------------

patron_fecha = r"\d{2}/\d{2}/\d{4}"

resultado_fecha = re.search(patron_fecha, cliente)


# ------------------------------------------------------------
# 4. MONTO
# ------------------------------------------------------------

patron_monto = r"\$\d+"

resultado_monto = re.search(patron_monto, cliente)


# ------------------------------------------------------------
# 5. VALIDACIÓN COMPLETA DEL CÓDIGO
# ------------------------------------------------------------

codigo = "MEV-458"
patron_validacion = r"[A-Z]{3}-\d{3}"

resultado_validacion = re.fullmatch(patron_validacion, codigo)


# ------------------------------------------------------------
# MOSTRAR RESULTADOS
# ------------------------------------------------------------

print("\nDATOS ENCONTRADOS:")

print("Código:", resultado_codigo.group())
print("Correo:", resultado_correo.group())
print("Fecha:", resultado_fecha.group())
print("Monto:", resultado_monto.group())

print("\nVALIDACIÓN:")

if resultado_validacion:
    print("El código cumple con el formato solicitado.")
else:
    print("El código no cumple con el formato solicitado.")
