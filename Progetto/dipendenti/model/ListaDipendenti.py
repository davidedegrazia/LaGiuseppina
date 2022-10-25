import json
import pickle
import os.path
from pathlib import Path

from Progetto.dipendenti.model.Dipendente import Dipendente

PATH_JSON = Path(r"C:\Users\Utente\Desktop\progettogiuseppina\Progetto\dipendenti\data\lista_dipendenti_iniziali.json")
PATH_PICKLE = Path('dipendenti/data/lista_dipendenti_salvata.pickle')

class ListaDipendenti:
    @staticmethod
    def prova_classe():
        lista = ListaDipendenti()
        lista.save_data()

    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile('../data'):
            with open(PATH_PICKLE, 'rb') as f:
                self.lista_dipendenti = pickle.load(f)
        else:
            with open(r"C:\Users\Utente\Desktop\progettogiuseppina\Progetto\dipendenti\data\lista_dipendenti_iniziali.json") as f:
                lista_dipendenti_iniziali = json.load(f)
            for dipendente_iniziale in lista_dipendenti_iniziali:
                self.aggiungi_dipendente(Dipendente(dipendente_iniziale["nome"], dipendente_iniziale["ore"],
                                                    dipendente_iniziale["compenso_a_ore"],
                                                    dipendente_iniziale["tipo_contratto"],
                                                    dipendente_iniziale["email"], dipendente_iniziale["telefono"]))

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def get_num_dipendenti(self):
        i = 0
        for dip in self.lista_dipendenti:
            i += 1
        return i

    def rimuovi_dipendente_by_index(self, index):
        self.lista_dipendenti.remove(self.lista_dipendenti[index])

    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    def get_numero_dipendenti(self):
        with open(PATH_JSON) as file:
            lista = json.load(file)
        return len(lista)

    def save_data(self):
        with open(PATH_JSON, 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)

def testprova():
    lista = ListaDipendenti()
    print(lista.get_lista_dipendenti())
    print(lista.get_numero_dipendenti())
    print(lista.get_dipendente_by_index(0))
    dipendente0 = lista.get_dipendente_by_index(0)
    print(dipendente0.nome)
    print(dipendente0.ore)
    print(dipendente0.compenso_a_ore)

if __name__ == "__main__":
    testprova()
