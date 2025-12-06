class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def summa(self, operandi):
        self._arvo = self._arvo + operandi

    def erotus(self, operandi):
        self._arvo = self._arvo - operandi

    def nollaus(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo