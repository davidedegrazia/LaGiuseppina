import json
import pickle
import os.path

from Progetto.dipendenti.model.Dipendente import Dipendente


class ListaDipendenti:
    @staticmethod
    def prova_classe():
        lista = ListaDipendenti()
        lista.save_data()

    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile('../data'):
            with open('../data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)
        else:
            with open('../data/lista_dipendenti_iniziali.json') as f:
                lista_dipendenti_iniziali = json.load(f)
            for dipendente_iniziale in lista_dipendenti_iniziali:
                self.aggiungi_dipendente(Dipendente(dipendente_iniziale["nome"], dipendente_iniziale["ore"],
                                                    dipendente_iniziale["compenso_a_ore"],
                                                    dipendente_iniziale["tipo_contratto"],
                                                    dipendente_iniziale["email"], dipendente_iniziale["telefono"]))

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente_by_index(self, index):
        for dipendente in self.lista_dipendenti:
            if dipendente.index == index:
                self.lista_dipendenti.remove(dipendente)

    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    def get_numero_dipendenti(self):
        with open('../data/lista_dipendenti_iniziali.json') as file:
            lista = json.load(file)
        return len(lista)

    def save_data(self):
        with open('dipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
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
