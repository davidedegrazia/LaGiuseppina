path_data = 'Progetto/data/dipendenti.pickle'
import pickle
class ControlloreListaDipendenti:
    def __init__(self, lista):
        self.model = lista

    # aggiunge un elemento alla lista
    def aggiungi_elemento(self, elemento):
        self.model.aggiungi_dipendente(elemento)

    # ritorna la lista
    def get_lista(self):
        return self.model.get_lista_dipendenti()

    # rimuove un elemento dalla lista per mezzo dell'indice
    def rimuovi_by_index(self, index):
        self.model.rimuovi_dipendente_by_index(index)

    # restituisce un elemento dalla lista per mezzo dell'indice
    def get_elemento_elemento_by_index(self, index):
        self.model.get_dipendente_by_index(index)

    # salva i dati su un file
    def save_data(self):
        with open(path_data, 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    #restituisce il totale da aggiungere al bilancio
    def get_totale(self):
        totale = 0
        for dipendente in self.get_lista():
            totale += dipendente.calcola_stipendio() # Da cambiare nelle altre classi
