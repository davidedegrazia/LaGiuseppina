import json
import os
import pickle
import sys

from Progetto.listaprodotti.model.ListaProdottiSalvati import ListaProdottiSalvati, PATH_PRODOTTI_PICKLE, \
    PATH_PRODOTTI_JSON
from Progetto.listaprodotti.model.Prodotto import Prodotto, CategoriaProdotti
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità


def prova_init():
    cntr = ControlloreListaProdottiSalvati()
    p = Prodotto('banana', CategoriaProdotti.FRUTTA, 'kg', 150)
    ControlloreListaProdottiSalvati.aggiungi_elemento(cntr, p)
    print(ControlloreListaProdottiSalvati.is_present(cntr, 'banana'))
    cntr.save_data()


class ControlloreListaProdottiSalvati:
    def __init__(self):
        super(ControlloreListaProdottiSalvati, self).__init__()
        self.model = ListaProdottiSalvati()
        if os.path.isfile('D:\Python\LaGiuseppina_aggiornato\Progetto/listaprodotti/data/ListaProdottiSalvati.pickle'):
            try:
                with open('D:\Python\LaGiuseppina_aggiornato\Progetto/listaprodotti/data/ListaProdottiSalvati.pickle',
                          'rb') as f:
                    self.model.lista = pickle.load(f)
            except EOFError:
                self.model.lista = []
        else:
            with open('D:\Python\LaGiuseppina_aggiornato\Progetto/listaprodotti/data/ListaProdottiSalvati.json') as f:
                self.model.lista = json.load(f)
            for prodotto in self.model.lista:
                self.aggiungi_elemento(Prodotto(prodotto['nome'], prodotto['categoria'], prodotto['tipo_unita'],
                                                prodotto['prezzo_su_unita']))

    def aggiungi_elemento(self, prodotto: Prodotto):
        lista = self.model.getLista()
        for elemento in self.model.lista:
            if elemento.get_nome().lower() == prodotto.get_nome().lower():
                raise ValueError('L \'elemento è già presente all\'interno della lista')
        lista.append(prodotto)
        lista.sort(key=Prodotto.get_nome)

    def get_elemento_by_name(self, nome: str) -> ProdottoConQuantità:
        for elemento in self.model.lista:
            if elemento.get_nome().lower() == nome.lower():
                return elemento
        raise ValueError('Prodotto non trovato!')

    def is_present(self, nome: str):
        for elemento in self.model.lista:
            if elemento.get_nome().lower() == nome.lower():
                return True
        return False

    def get_elemento_by_id(self, id):
        lista = self.model.getLista()
        for elemento in lista:
            if elemento.get_id() == id:
                return elemento
        raise ValueError('ID not found')

    def get_elemento_by_index(self, index):
        return self.model.getLista()[index]

    def get_lista(self):
        return self.model.getLista()

    def save_data(self):
        with open('..\data\ListaProdottiSalvati.pickle',
                  'wb') as handle:
            pickle.dump(self.model.getLista(), handle, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    prova_init()
