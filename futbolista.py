from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, _nombre, _edad, _altura, _sexo, _añosPracticando,_golesMarcados, _tarjetasRojas, _piernaHabil):
        Persona.__init__(self, _nombre, _edad, _altura, _sexo)
        Deportista.__init__(self, _añosPracticando)
        self._golesMarcados = _golesMarcados
        self._tarjetasRojas = _tarjetasRojas
        self._piernaHabil = _piernaHabil
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self, _golesMarcados):
        self._golesMarcados = _golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTajetasRojas(self, _tarjetasRojas):
        self._tarjetasRojas = _tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self, _piernaHabil):
        self._piernaHabil = _piernaHabil
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
    @classmethod
    def setListaFutbolistas(cls, _listaFutbolistas):
        cls._listaFutbolistas = _listaFutbolistas
    
    def __str__(self):
        return ("Mi nombre es " + str(super().getNombre()) + " soy profesional en el deporte " + str(super().getDeporte()) + " Tengo " + str(super().getEdad()) + " años de edad y llevo " + str(super().getAñosPracticando()) + " años en el deporte")