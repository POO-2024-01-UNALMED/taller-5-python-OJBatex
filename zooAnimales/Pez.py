from animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, \
                 colorEscamas, aletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = aletas
        Pez._listado.append(self)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, \
                      "rojo", 6)
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, \
                      "gris", 6)
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cant):
        self._cantidadAletas = cant
