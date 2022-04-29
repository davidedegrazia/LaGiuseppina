import json
import os
import pickle
from pathlib import Path

from Progetto.listaprodotti.model.ListaProdottiSalvati import ListaProdottiSalvati
from Progetto.listaprodotti.model.Prodotto import Prodotto, CategoriaProdotti
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità

#Dichiarazione path in cui vengono salvati i file
path_data = Path('../data')
pickle_file = path_data / 'ListaProdottiSalvati.pickle'
json_file = path_data / 'ListaProdottiSalvati.json'

#Test per la classe: ritorna errore se si inserice un prodotto che è già in lista
def prova_init():
    cntr = ControlloreListaProdottiSalvati()
    p = Prodotto('ziopers', CategoriaProdotti.FRUTTA, 'kg', 150)
    ControlloreListaProdottiSalvati.aggiungi_elemento(cntr, p)
    print(ControlloreListaProdottiSalvati.is_present(cntr, 'banana'))
    cntr.save_data()

#Classe utile a gestire i dati relativi ai prodotti che sono utilizzabile nel programma
class ControlloreListaProdottiSalvati:
    def __init__(self):
        super(ControlloreListaProdottiSalvati, self).__init__()
        self.model = ListaProdottiSalvati()
        if os.path.isfile(pickle_file):
            try:
                with open(pickle_file,
                          'rb') as f:
                    self.model.lista = pickle.load(f)
            except EOFError:
                self.model.lista = []
        else:
            with open(json_file) as f:
                self.model.lista = json.load(f)
            for prodotto in self.model.lista:
                self.aggiungi_elemento(Prodotto(prodotto['nome'], prodotto['categoria'], prodotto['tipo_unita'],
                                                prodotto['prezzo_su_unita']))

    #Metodo per aggiungere un prodotto nella lista
    #Se il prodotto è già prsente nella lista viene lanciata un eccezione di tipo ValueError
    def aggiungi_elemento(self, prodotto: Prodotto):
        lista = self.model.getLista()
        for elemento in self.model.lista:
            if elemento.get_nome().lower() == prodotto.get_nome().lower():
                raise ValueError('L \'elemento è già presente all\'interno della lista')
        lista.append(prodotto)
        lista.sort(key=Prodotto.get_nome)

    #Ritorna il prodotto corrispondente al nome specificato, se esiste. ALtrimenti lancia un eccezione di tipo ValueError
    def get_elemento_by_name(self, nome: str) -> ProdottoConQuantità:
        for elemento in self.model.lista:
            if elemento.get_nome().lower() == nome.lower():
                return elemento
        raise ValueError('Prodotto non trovato!')
    #Ritorna vero se l'elemento con il nome specificato è presente in lista, ritorna falso altrimenti
    def is_present(self, nome: str):
        for elemento in self.model.lista:
            if elemento.get_nome().lower() == nome.lower():
                return True
        return False

    #Ritorna l'elemento relativo all'id specificato
    def get_elemento_by_id(self, id):
        lista = self.model.getLista()
        for elemento in lista:
            if elemento.get_id() == id:
                return elemento
        raise ValueError('ID not found')

    #Ritorna l'elemento relativo all'indice specificato
    def get_elemento_by_index(self, index):
        return self.model.getLista()[index]

    #Ritorna la lista degli elementi
    def get_lista(self):
        return self.model.getLista()

    #Salva la lista nel file pickle
    def save_data(self):
        with open(pickle_file,
                  'wb') as handle:
            pickle.dump(self.model.getLista(), handle, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    prova_init()
