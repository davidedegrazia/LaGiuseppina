import json
import os
import pickle
from os.path import exists

from Progetto.listaprodotti.controller.ControlloreListaProdottiSalvati import ControlloreListaProdottiSalvati
from Progetto.listaprodotti.model.ListaProdottiConQuantita import ListaProdottiConQuantita
from Progetto.listaprodotti.model.Prodotto import Prodotto, CategoriaProdotti, UnitaDiMisura
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità


def prova_init():
    pth = '../data/ProvaListaProdotti.json'
    c_p_salvati = ControlloreListaProdottiSalvati()
    cntr = ControlloreListaProdotti(c_p_salvati, pth)
    pepe = Prodotto('pepe', CategoriaProdotti.ALTRO, UnitaDiMisura.KILOGRAMMO, 150000)
    print(pepe)
    c_p_salvati.aggiungi_elemento(pepe)
    print(c_p_salvati.get_elemento_by_name('pepe'))
    cntr.aggiungi_elemento_by_name('pepe', 600)
    pepe600 = cntr.get_elemento_by_name('pepe')
    print(pepe600)
    return cntr


def get_nome(prodotto: Prodotto):
    return prodotto.get_nome()


class ControlloreListaProdotti(ControlloreListaProdottiSalvati):

    # Il path è il path del file in cui sono salvati i dati del Controllore, funziona sia con .pickle che con .json
    # Se il file al path specificato non esiste lo crea ed in tal caso ritorna FIleNotFoundError con un messaggio che riporta l'avvenuta creazione
    def __init__(self, c_lista_prodotti_salvati: ControlloreListaProdottiSalvati, path):
        self.clps = c_lista_prodotti_salvati
        if path.endswith('.pickle'):
            self.path_pickle = path
            self.path_json = path.replace('.pickle', '.json')
        elif path.endswith('.json'):
            self.path_json = path
            self.path_pickle = path.replace('.json', '.pickle')
        else:
            raise ValueError
        self.model = ListaProdottiConQuantita(self.path_json)
        if os.path.isfile(self.path_pickle):
            with open(self.path_pickle, 'rb') as f:
                self.model.lista = pickle.load(f)
        else:
            file_is_present = exists(self.path_json)
            if not file_is_present:
                with open(self.path_json, 'w') as f:
                    f.write('[]')
            with open(self.path_json) as f:
                self.model.lista = json.load(f)
            for prodotto in self.model.lista:
                self.aggiungi_elemento(Prodotto(prodotto['nome'], prodotto['categoria'], prodotto['tipo_unita'],
                                                prodotto['prezzo_su_unita']))
            if not file_is_present:
                error_string = 'Non è stato creato nesssun file al path: ' + path
                if exists(self.path_json):
                    error_string + '\n File ' + self.path_json + ' crato con successo!'
                elif exists(self.path_pickle):
                    error_string + '\n File ' + self.path_pickle + ' crato con successo!'
                raise FileNotFoundError(error_string)

    def aggiungi_elemento_by_name(self, nome: str, quantita: int):
        lista = self.model.getLista()
        if self.clps.is_present(nome):
            prodotto_salvato = self.clps.get_elemento_by_name(nome)
            nuovo_prodotto = ProdottoConQuantità.costruttore_da_prodotto(prodotto_salvato, quantita)
        else:
            raise ValueError('\'' + nome + '\' non è presente nei prodotti salvati!')
        lista.append(nuovo_prodotto)
        lista.sort(key=get_nome)

    def save_data(self):
        with open(self.path_pickle, 'wb') as handle:
            pickle.dump(self.model.getLista(), handle, pickle.HIGHEST_PROTOCOL)

    def funzione_prova(self):
        pass


if __name__ == "__main__":
    cntr = prova_init()
