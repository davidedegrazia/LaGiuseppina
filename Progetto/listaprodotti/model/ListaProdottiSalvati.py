import json
import os
import pickle
from pathlib import Path

from Progetto.listaprodotti.model.Prodotto import Prodotto
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità

PATH_PRODOTTI_PICKLE = Path('listaprodotti/data/ListaProdottiSalvati.pickle')
PATH_PRODOTTI_JSON = Path(r"C:\Users\Utente\Desktop\progettogiuseppina\Progetto\listaprodotti\data\ListaProdottiSalvati.json")


# Classe che modella la lista_prodotti_salvati dei prodotti presenti nel programma
class ListaProdottiSalvati:
    def __init__(self):
        super(ListaProdottiSalvati, self).__init__()
        self.lista_prodotti_salvati = []
        self.valore = 0
        self.numero_elementi = 0
        self.__len__ = self.lista_prodotti_salvati.__len__()
        self.count_prodotti_frutta = 0
        self.count_prodotti_verdura = 0
        self.count_prodotti_erbe_aromatiche = 0
        self.count_prodotti_altro = 0

        if os.path.isfile(PATH_PRODOTTI_PICKLE):
            with open(
                    PATH_PRODOTTI_PICKLE,
                    'rb') as f:
                self.lista_prodotti_salvati = pickle.load(f)
        else:
            with open(PATH_PRODOTTI_JSON) as f:
                lista_prodotti_salvati_iniziale = json.load(f)
            for prodotto in lista_prodotti_salvati_iniziale:
                self.aggiungi_elemento(Prodotto(prodotto['nome'], prodotto['categoria'], prodotto['tipo_unita'],
                                                prodotto['prezzo_su_unita']))

    def aggiungi_elemento(self, prodotto: Prodotto):
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == prodotto.get_nome().lower():
                raise ValueError('L\'elemento è già presente all\'interno della lista_prodotti_salvati')

        self.lista_prodotti_salvati.append(prodotto)

    def get_num_frutta(self):
        for elemento in self.lista_prodotti_salvati:
            if elemento.categoria == "frutta":
                    self.count_prodotti_frutta = self.count_prodotti_frutta + 1
        return self.count_prodotti_frutta

    def save_data(self):
        with open(PATH_PRODOTTI_JSON, 'wb') as handle:
            pickle.dump(self.lista_prodotti_salvati, handle, pickle.HIGHEST_PROTOCOL)

    def get_elemento_by_name(self, nome: str) -> Prodotto:
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == nome.lower():
                return elemento
        raise ValueError('Prodotto non trovato!')

    def get_index_by_name(self, nome: str) -> int:
        with open(PATH_PRODOTTI_JSON, "r") as file:
            data = json.load(file)
            i = 0
            for elemento in data:
                if elemento['nome'] == nome:
                    return i
                i += 1

    def is_present(self, nome: str):
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == nome.lower():
                return True
        return False

    def get_elemento_by_index(self, index: int) -> ProdottoConQuantità:
        return self.lista_prodotti_salvati[index]

    def get_index_by_name(self, name: str) -> int:
        with open(PATH_PRODOTTI_JSON, "r") as file:
            data = json.load(file)
            index = 0
            for prodotto in data:
                if prodotto['nome'] == name:
                    return index
                index += 1

    def get_quantita_by_name(self, nome: str) -> int:
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == nome.lower():
                return elemento.get_quantita()

    def get_prezzo_by_name(self, nome: str) -> int:
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == nome.lower():
                return elemento.get_prezzo_su_unita()

    def valore_totale(self):
        with open(PATH_PRODOTTI_JSON, "r") as file:
            data = json.load(file)
        valore = 0
        for elemento in data:
            valore = valore + (elemento['quantita'] * elemento['prezzo_su_unita'])
        return round(valore, 2)

    def get_prezzo_by_index(self, index: int):
        with open(PATH_PRODOTTI_JSON, "r") as file:
            data = json.load(file)
        return data[index]['prezzo_su_unita']

    def set_quantita_by_name(self, nome: str, quantita: str):
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == nome.lower():
                elemento['quantita'] = quantita
        self.save_data()

    def modifica_quantita_by_index(self, index: int, quantita: int):
        with open(PATH_PRODOTTI_JSON, "r") as file:
            data = json.load(file)
            data[index]['quantita'] = int(quantita)
        with open(PATH_PRODOTTI_JSON, "w") as file:
            json.dump(data, file, indent=4)

    def rimuovi_elemento_by_name(self, nome: str):
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == nome.lower():
                self.lista_prodotti_salvati.remove(elemento)

    def modifica_elemento_by_name(self, nome: str, nuovo_prodotto: Prodotto):
        with open(PATH_PRODOTTI_JSON, "r") as file:
            data = json.load(file)
        i = 0
        for elemento in data:
            if elemento["nome"].lower() == nome.lower():

                prodotto_modificato = {
                    "nome": nuovo_prodotto.get_nome(),
                    "categoria": nuovo_prodotto.get_categoria(),
                    "tipo_unita": nuovo_prodotto.get_tipo_unita(),
                    "prezzo_su_unita": nuovo_prodotto.get_prezzo_su_unita()
                }
                with open(PATH_PRODOTTI_JSON, "w") as file:
                    data = json.load(file)
                data[i] = prodotto_modificato
                json.dump(data, file, indent=4)
            else:
                i = i + 1

    def getLista(self):
        return self.lista_prodotti_salvati

    def get_lista_frutta(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
        lista_frutta = []
        for elemento in lista:
            if elemento["categoria"].lower() == "frutta":
                lista_frutta.append(elemento)
        return lista_frutta

    def get_lista_verdura(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
        lista_verdura = []
        for elemento in lista:
            if elemento["categoria"].lower() == "verdura":
                lista_verdura.append(elemento)
        return lista_verdura

    def get_lista_erbe_aromatiche(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
        lista_erbearomatiche = []
        for elemento in lista:
            if elemento["categoria"].lower() == "erbe aromatiche":
                lista_erbearomatiche.append(elemento)
        return lista_erbearomatiche

    def get_lista_altro(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
        lista_altro = []
        for elemento in lista:
            if elemento["categoria"].lower() == "altro":
                lista_altro.append(elemento)
        return lista_altro

    def get_count_lista_frutta(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
            for elemento in lista:
                if elemento["categoria"].lower() == "frutta":
                    self.count_prodotti_frutta = self.count_prodotti_frutta + 1
        return self.count_prodotti_frutta

    def get_count_lista_verdura(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
            for elemento in lista:
                if elemento["categoria"].lower() == "verdura":
                    self.count_prodotti_verdura = self.count_prodotti_verdura + 1
        return self.count_prodotti_verdura

    def get_count_lista_erbe_aromatiche(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
            for elemento in lista:
                if elemento["categoria"].lower() == "erbe aromatiche":
                    self.count_prodotti_erbe_aromatiche = self.count_prodotti_erbe_aromatiche + 1
        return self.count_prodotti_erbe_aromatiche

    def get_count_lista_altro(self):
        with open(PATH_PRODOTTI_JSON) as f:
            lista = json.load(f)
            for elemento in lista:
                if elemento["categoria"].lower() == "altro":
                    self.count_prodotti_altro = self.count_prodotti_altro + 1
        return self.count_prodotti_altro


def testprova():
    lista = ListaProdottiSalvati()
    print(lista.getLista())
    print(lista.get_count_lista_frutta())
    print(lista.get_count_lista_verdura())
    print(lista.get_count_lista_erbe_aromatiche())
    print(lista.get_count_lista_altro())
    prodotto0 = lista.get_elemento_by_index(0)
    print(prodotto0.nome)
    print(prodotto0.categoria)
    print(prodotto0.quantita)

if __name__ == "__main__":
    testprova()