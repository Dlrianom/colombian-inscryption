from carta import Carta

class Mazo:
    def __init__(self):
        self.cartas = {}

    def recibirCarta (self, mazo_origen, id):
        carta = mazo_origen.get(id)
        self.cartas[id] = carta
        mazo_origen.pop(id)

    def printCarta(self, id): #para arreglar = imprimir los objetos
        print("==========================")#26 =
        print('|        [ {} ]        |'.format(self.cartas.get(id).id))
        print('| {:23}{}'.format(self.cartas.get(id).nombre, "|"))
        print('|    {:12} {:3d}    {}'.format("ATAQUE:", self.cartas.get(id).ataque, "|"))
        print('|    {:12} {:3d}    {}'.format("DEFENSA:", self.cartas.get(id).defensa, "|"))
        print('|    {:12} {:3d}    {}'.format("SACRIFICIO:", self.cartas.get(id).sacrificio, "|"))
        print('|    {:12} {:3d}    {}'.format("CONVOCAR:", self.cartas.get(id).convocar, "|"))
        print("==========================")#2& =

    def printCartas (self):
        for key in self.cartas:
            self.printCarta(key)
            print ("")

    def getCardsType (self, tipo_carta): #(cartas_DISP, 'super')
        out_cards_for_type = {}
        # extraer cartas disponibles del tipo de carta 
        for carta_key in self.cartas:
            tipo = self.cartas.get(carta_key).tipo
            if tipo == tipo_carta:
                out_cards_for_type[carta_key] = self.cartas.get(carta_key)
            else:
                continue
        return out_cards_for_type
    
    def dictToCarta (self, carta_dicc, id):
        carta = Carta(carta_dicc, id)
        self.cartas[id] = carta

    def diccToCartas (self, cartas_dicc):
        for key in cartas_dicc:
            self.dictToCarta(cartas_dicc, key)