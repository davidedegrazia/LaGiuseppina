class Magazzino():

    def __init__(self, prodotto, numero_prodotti, categorie, totale, aggiungi_a_bilancio):
        self.prodotto = prodotto
        self.numero_prodotti = numero_prodotti
        self.categorie = categorie
        self.totale = totale
        self.aggiungi_a_bilancio = aggiungi_a_bilancio

    def get_prodotti(self):
        return self.prodotto

    def get_totale(self):
        return self.totale

    def get_categorie(self):
        return self.categorie

    def get_numero_prodotti(self):
        return self.numero_prodotti

    def rimuovi_prodotto_by_index(self, index):
        self.prodotto_by_index(index)

    def aggiungi_prodotto(self, prodotto):
        self.prodotto(prodotto)

    def get_prodotto_by_index(self, index):
        return self.prodotto_by_index(index)

    def categoria_prodotti(self, prodotti):
        self.categoria_prodotti(prodotti)

    def prodotto_by_index(self, index):
        self.prodotto_by_index(index)

    def quantita_by_index(self, index):
        self.quantita_by_index(index)










