from carta import Carta

class Mazo:
    def __init__(self):
        self.cartas = {}

    def recibirCarta (self, mazo_origen, id):
        carta = mazo_origen.get(id)
        self.cartas[id] = carta
        mazo_origen.pop(id)

    def printMazo(self): #para arreglar = imprimir los objetos
        print(self.cartas)
        return self.cartas

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