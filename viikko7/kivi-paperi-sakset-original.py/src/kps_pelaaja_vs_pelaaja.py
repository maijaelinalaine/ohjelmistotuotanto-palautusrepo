from viikko7.src.kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")