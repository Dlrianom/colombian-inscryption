class Carta:
    def __init__(self, mazo, card_id):
        carta = mazo.get(card_id)
        self.id = card_id
        self.nombre = carta[0]
        self.tipo = carta[1]
        self.ataque = carta[2]
        self.defensa = carta[3]
        self.sacrificio = carta[4]
        self.convocar = carta[5] # o quien haga sus veces