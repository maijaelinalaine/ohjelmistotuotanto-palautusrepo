from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class PeliTehdas:
    @staticmethod
    def luo(vastaus):
        if vastaus == "a":
            return KPSPelaajaVsPelaaja()
        elif vastaus == "b":
            return KPSTekoaly()
        elif vastaus == "c":
            return KPSParempiTekoaly()
        else:
            return None