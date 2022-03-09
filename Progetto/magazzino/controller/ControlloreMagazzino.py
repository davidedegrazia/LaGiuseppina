from Progetto.magazzino.model.Magazzino import Magazzino


class ControlloreListaMagazzino():
    def __init__(self):
        super(ControlloreListaMagazzino, self).__init__()
        self.model = Magazzino()

    def aggiungi_elemento(self, prodotto):
        self.model.aggiungi_prodotto(prodotto)

    def elimina_elemento_by_index(self, index):
        self.model.rimuovi_prodotto_by_index(index)

    def get_prodotto_by_index(self, index):
        return self.model.get_prodotto_by_index(index)

    def save_data(self):
        self.save_data()

    def load_data(self):
        self.load_data()

    def get_totale(self):
        return self.model.totale()

    def aggiorna_totale(self):
        self.model.totale()

    def get_numero_prodotti(self):
        return self.prodotti()

    def get_totale_categoria_prodotti(self, prodotti):
        return self.model.categoria_prodotti(prodotti)

    def prodotti(self):
        self.prodotti()

    def aggiungi_quantita_by_index(self, index):
        self.model.quantita_by_index(index)

    def modifica_quantita_by_index(self, index):
        self.model.quantita_by_index(index)







    



