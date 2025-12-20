from tuomari import Tuomari
from abc import ABC, abstractmethod


class KPS(ABC):
    def pelaa(self):
        self._tuomari = Tuomari()

        ekan_siirto = self._ekan_siirto()
        tokan_siirto = self._tokan_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            self._paivita_tilanne(ekan_siirto)

            ekan_siirto = self._ekan_siirto()
            tokan_siirto = self._tokan_siirto()

        print("Kiitos!")
        print(self._tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")

    @abstractmethod
    def _ekan_siirto(self):
        pass

    @abstractmethod
    def _tokan_siirto(self):
        pass

    def _paivita_tilanne(self, ekan_siirto):
        # oletuksena ei tehdä mitään
        pass