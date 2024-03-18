from zona import Zona

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def cantidadTotalAnimales(self):
        cantAnimales = 0
        for i in range (len(self._zonas)):
            cantAnimales += self._zonas[i].cantidadAnimales()
        return cantAnimales
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubi):
        self._ubicacion = ubi

    def getZona(self):
        return self._zonas
    
    def setZona(self, zona):
        self._zonas = zona