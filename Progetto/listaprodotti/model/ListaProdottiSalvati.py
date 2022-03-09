from Progetto.magazzino.model.Magazzino import Magazzino


class ListaProdottiSalvati():
    def __init__(self):
        super(ListaProdottiSalvati, self).__init__()
        self.model = Magazzino()

    def crea_prodotto(self):
        var = self.model.prodotto