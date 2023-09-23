from enum import IntEnum, StrEnum


class Environment(StrEnum):
    LOCAL = "LOCAL"
    PROD = "PROD"


class Latitude(IntEnum):
    MIN = -90.00
    MAX = 90.00


class Longitude(IntEnum):
    MIN = -180.00
    MAX = 180.00
