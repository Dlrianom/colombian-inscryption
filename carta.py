class Carta:
    def __init__(self, mazo, card_ID):
        carta = mazo.get(card_ID)
        self.ID = card_ID
        self.nombre = carta[0]
        self.ataque = carta[2]
        self.defensa = carta[3]
        self.sacrificio = carta[4]
        self.convocar = carta[5] # o quien haga sus veces