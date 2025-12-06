from tkinter import Tk
from src.kayttoliittyma import Kayttoliittyma
from src.sovelluslogiikka import Sovelluslogiikka


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovellus, window)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()