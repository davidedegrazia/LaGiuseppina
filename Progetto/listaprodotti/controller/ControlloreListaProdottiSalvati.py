import json
import os
import pickle
import sys

from Progetto.listaprodotti.model.ListaProdottiSalvati import ListaProdottiSalvati, PATH_PRODOTTI_PICKLE, \
    PATH_PRODOTTI_JSON
from Progetto.listaprodotti.model.Prodotto import Prodotto, CategoriaProdotti
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità

''' def prova_init():
    cntr = ControlloreListaProdottiSalvati()
    p = Prodotto('uva', CategoriaProdotti.FRUTTA, 'kg', 150)
    ControlloreListaProdottiSalvati.aggiungi_elemento(cntr, p)
    print(ControlloreListaProdottiSalvati.is_present(cntr, 'banana'))
    cntr.save_data() '''


class ControlloreListaProdottiSalvati:
    def __init__(self):
        super(ControlloreListaProdottiSalvati, self).__init__()
        self.model = ListaProdottiSalvati()

    def aggiungi_elemento(self, prodotto: Prodotto):
        self.model.aggiungi_elemento(prodotto)
        self.model.save_data()

    def rimuovi_elemento_by_name(self, nome: str):
        self.model.rimuovi_elemento_by_name(nome)
        self.model.save_data()

    def get_elemento_by_name(self, nome: str) -> ProdottoConQuantità:
        return self.model.get_elemento_by_name(nome)

    def modifica_elemento_by_name(self, nome: str, nuovo_prodotto: Prodotto):
        self.model.modifica_elemento_by_name(nome, nuovo_prodotto)
        self.model.save_data()

    def get_index_by_name(self, nome: str):
        return self.model.get_index_by_name(nome)

    def is_present(self, nome: str):
        self.model.is_present(nome)

    def get_elemento_by_index(self, index):
        return self.model.getLista()[index]

    def get_quantita_by_name(self, nome: str) -> int:
        return self.model.get_quantita_by_name(nome)

    def set_quantita_by_name(self, nome: str, quantita: int):
        self.model.set_quantita_by_name(nome, quantita)

    def modifica_quantita_by_index(self, index: int, quantita: int):
        self.model.modifica_quantita_by_index(index, quantita)

    def get_prezzo_by_name(self, nome: str) -> int:
        return self.model.get_prezzo_by_name(nome)

    def get_prezzo_by_index(self, index: int):
        return self.model.get_prezzo_by_index(index)

    def valore_totale(self):
        return self.model.valore_totale()

    def get_lista(self):
        return self.model.getLista()

    def get_elemento_by_name(self, nome: str):
        return self.model.rimuovi_elemento_by_name(nome)

    def get_index_by_name(self, name: str) -> int:
        return self.model.get_index_by_name(name)

    def get_lista_frutta(self):
        return self.model.get_lista_frutta()

    def get_lista_verdura(self):
        return self.model.get_lista_verdura()

    def get_lista_erbe_aromatiche(self):
        return self.model.get_lista_erbe_aromatiche()

    def get_lista_altro(self):
        return self.model.get_lista_altro()

    def get_count_lista_frutta(self):
        return self.model.get_count_lista_frutta()

    def get_count_lista_verdura(self):
        return self.model.get_count_lista_verdura()

    def get_count_lista_erbe_aromatiche(self):
        return self.model.get_count_lista_erbe_aromatiche()

    def get_count_lista_altro(self):
        return self.model.get_count_lista_altro()



