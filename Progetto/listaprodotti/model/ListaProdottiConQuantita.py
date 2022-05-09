import json
import os
import pickle
import uuid

from Progetto.listaprodotti.model.Prodotto import Prodotto, CategoriaProdotti


class ListaProdottiConQuantita:
    def __init__(self):
        super(ListaProdottiConQuantita, self).__init__()
        self.lista_magazzino = []
        self.lista_tuple_categorie_unita = ListaProdottiConQuantita.get_tuple_categorie_unita()
        self.quantita_per_tupla = [self.get_tuple_categorie_unita().__len__()]

        with open('/Users/davidedegrazia/PycharmProjects/LaGiuseppina/Progetto/listaprodotti/data/ListaProdottiMagazzino.json') as f:
            lista = json.load(f)
            lista_magazzino = lista
            for prodotto in lista_magazzino:
                prodotto['quantita'] = 0
        with open('/Users/davidedegrazia/PycharmProjects/LaGiuseppina/Progetto/listaprodotti/data/ListaProdottiMagazzino.json', 'w') as f:
            json.dump(lista_magazzino, f)

    @staticmethod
    def get_tuple_categorie_unita():
        lista_tuple = []
        for categoria in Prodotto.get_lista_categorie():
            for unita in Prodotto.get_lista_unita():
                lista_tuple.append((categoria, unita))
        return lista_tuple

    def aggiungi_elemento(self, prodotto: Prodotto, quantita = 0):
        new_prodotto = {
            "nome" : prodotto.get_nome(),
            "categoria" : prodotto.get_categoria(),
            "tipo_unita" : prodotto.get_tipo_unita(),
            "prezzo_su_unita" : prodotto.get_prezzo_su_unita(),
            "quantita" : quantita
        }

        self.lista.append(new_prodotto)

    def get_lista(self):
        return self.lista_magazzino

    def get_lista_per_categoria(self, categoria: str):
        lista_categoria = []
        for prodotto in self.lista:
            if prodotto['categoria'] == categoria:
                lista_categoria.append(prodotto)
        return lista_categoria

    def get_elemento_by_index(self, index):
        return self.lista[index]

    def get_lunghezza(self) -> int:
        return len(self.lista)

    def get_valore(self):
        valore = 0
        for prodotto in self.lista:
            valore = valore + (prodotto['prezzo_su_unita']* prodotto['quantita'])
        return valore

    def get_quantita_per_categoria_unita(self, tupla):
        return self.quantita_per_tupla[tupla]

    def get_valore_per_categoria(self, categoria: str):
        valore = 0
        for prodotto in self.lista:
            if prodotto['categoria'] == categoria:
                valore = valore + (prodotto['prezzo_su_unita'] * prodotto['quantita'])
        return valore

