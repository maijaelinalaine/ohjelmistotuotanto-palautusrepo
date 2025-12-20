from viikko7.src.kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_siirto(self):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

    def _paivita_tilanne(self, ekan_siirto):
        self._tekoaly.aseta_siirto(ekan_siirto)
