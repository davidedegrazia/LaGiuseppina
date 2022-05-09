import os
import pickle

from Progetto.listaprodotti.model.ListaProdottiConQuantita import ListaProdottiConQuantita


class ControlloreListaMagazzino():
    def __init__(self):
        super(ControlloreListaMagazzino, self).__init__()
        self.model = ListaProdottiConQuantita()

    def aggiungi_elemento(self, prodotto):
        self.model.aggiungi_prodotto(prodotto)

    def get_lista(self):
        return self.model.get_lista()

    def get_lista_per_categoria(self, categoria: str):
        return self.model.get_lista_per_categoria(categoria)

    def get_prodotto_by_index(self, index):
        return self.model.get_elemento_by_index(index)

    def get_lunghezza_lista(self) -> int:
        return self.model.get_lunghezza()

    def get_valore_magazzino(self) -> int:
        return self.model.get_valore()

    def get_valore_per_categoria(self, categoria: str) -> int:
        return self.model.get_valore_per_categoria(categoria)

    def prodotti(self):
        self.prodotti()









    



