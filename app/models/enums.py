from enum import Enum


class Country(str, Enum):
    CO = "CO"
    PE = "PE"


class RegistrationStatus(str, Enum):
    ACTIVE = "ACTIVA"
    INACTIVE = "INACTIVA"
    CANCELLED = "CANCELADA"
    UNKNOWN = "DESCONOCIDO"
