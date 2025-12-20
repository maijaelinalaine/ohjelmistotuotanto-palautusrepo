from viikko7.src.kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_siirto(self):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
