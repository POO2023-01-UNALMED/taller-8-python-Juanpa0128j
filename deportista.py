class Deportista():
    def __init__(self, _añosPracticando, _deporte = "Futbol"):
        self._deporte = _deporte
        self._añospracticando = _añosPracticando

    def getDeporte(self):
        return self._deporte
    def setDeporte(self, _deporte):
         self._deporte = _deporte
    def getAñosPracticando(self):
        return self._añospracticando
    def setAñosPracticando(self, _añospracticando):
         self._añospracticando = _añospracticando