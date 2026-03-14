"""Validacion de RUC peruano (formato basico).

El RUC (Registro Unico de Contribuyentes) tiene 11 digitos.
Los primeros 2 digitos indican el tipo de contribuyente:
  10 = Persona natural
  15 = Persona natural sin RUC (NRUS)
  17 = Persona natural no domiciliada
  20 = Persona juridica
"""

from __future__ import annotations

import re


def validate_ruc(raw: str) -> tuple:
    """Validate a Peruvian RUC.

    Returns:
        (cleaned_ruc, errors)
        If errors is empty, the RUC is valid.
    """
    errors: list[str] = []

    # Strip whitespace, dots, dashes
    cleaned = re.sub(r"[\s.\-]", "", raw.strip())

    if not cleaned:
        return "", ["RUC vacio"]

    if not cleaned.isdigit():
        return cleaned, ["RUC contiene caracteres no numericos"]

    if len(cleaned) != 11:
        return cleaned, [f"RUC tiene longitud invalida: {len(cleaned)} digitos (esperado 11)"]

    # First 2 digits must be 10, 15, 17 or 20
    prefix = cleaned[:2]
    if prefix not in ("10", "15", "17", "20"):
        errors.append(f"Prefijo de RUC invalido: {prefix} (esperado 10, 15, 17 o 20)")

    return cleaned, errors
