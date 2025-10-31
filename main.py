# -*- coding: utf-8 -*-
"""
Lógica para combinar CSV + API y consultar países (sin clases).
Formato unificado por país:
{ "nombre": str, "poblacion": int, "superficie": int, "continente": str }
"""

def _norm(s):
    if s is None: return ""
    return str(s).strip().lower()

def _to_int(value, campo, fila):
    try:
        return int(value)
    except Exception:
        raise ValueError("Fila {}: el campo '{}' debe ser entero (valor={!r})".format(fila, campo, value))