import pickle

from Progetto.dipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti

DATI_DIPENDENTI = 'Progetto/data/dipendenti.pickle'

def load_data(controllore_lista_dipendenti):
    with open(DATI_DIPENDENTI, 'wb') as file:
            lista = pickle.load(file)
            controllore_lista_dipendenti = ControlloreListaDipendenti(lista)

if __name__ == '__main__':
    controllore_lista_dipendenti = None
    load_data(controllore_lista_dipendenti)
