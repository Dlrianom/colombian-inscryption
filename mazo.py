from carta import Carta

class Mazo:
    def __init__(self):
        self.cartas = []

    def tomarCarta (self, card_tipe_dicc, ID):
        carta = Carta(card_tipe_dicc, ID)
        self.cartas.append(carta)
        card_tipe_dicc.pop(ID)

    def printMazo(self):
        print(self.cartas)
        return self.cartas