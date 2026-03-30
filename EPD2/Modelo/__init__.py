# Importamos las clases de los archivos individuales. El punto (.) indica que buscamos en el directorio actual
from .Electrodomestico import Electrodomestico
from .Lavadora import Lavadora
from .Televisor import Televisor
from .StockProducto import StockProducto

# Definimos qué se exporta si alguien hace "from Modelo import *"
__all__ = ["Electrodomestico", "Lavadora", "Televisor", "StockProducto"]