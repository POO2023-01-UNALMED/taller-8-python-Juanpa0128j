class Persona():
    def __init__(self, _nombre, _edad, _altura, _sexo):
        self._nombre = _nombre
        self._edad = _edad
        self._altura = _altura
        self._sexo = _sexo
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, _nombre):
        self._nombre = _nombre
    def getEdad(self):
        return self._edad
    def setEdad(self, _edad):
        self._edad = _edad
    def getAltura(self):
        return self._altura
    def setAltura(self, _altura):
        self._altura = _altura
    def getSexo(self):
        return self._sexo
    def setNombre(self, _sexo):
        self._sexo = _sexo

    