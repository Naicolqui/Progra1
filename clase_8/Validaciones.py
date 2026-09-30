import re

def validar_nombre(nombre):

    patron = r"[A-Za-z ]+"

    match=re.fullmatch(patron, nombre)
    return match


def validar_legajo(legajo):
    patron=r"[0-9]{6}"
    match=re.fullmatch(patron, legajo)
    return match


def validar_correo(correo):
    patron = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{3,}"
    mail=re.findall(patron, correo)
    return mail

def validar_comision(comision):
    patron = r"[A-Z]{1}-[0-9]{4}"
    comision=re.fullmatch(patron, comision)
    return comision

def validar_telefono(telefono):
    patron = r"[0-9]{2}-[0-9]{4}-[0-9]{4}"
    telefono=re.fullmatch(patron, telefono)
    return telefono


