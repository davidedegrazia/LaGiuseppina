PATH_DATA = 'Progetto/data/dipendenti.pickle' #path del file pickle sul quale vengono salvate le informazioni riguardo i dipendenti
import pickle


class ControlloreListaDipendenti:
    def __init__(self):
        with open(PATH_DATA, 'wb') as file:
            lista = pickle.load(file)
            self.model = lista

    # aggiunge un elemento alla lista
    def aggiungi_elemento(self, elemento):
        self.model.aggiungi_dipendente(elemento)
        self.save_data()

    # ritorna la lista
    def get_lista(self):
        return self.model.get_lista_dipendenti()

    # rimuove un elemento dalla lista per mezzo dell'indice
    def rimuovi_by_index(self, index):
        self.model.rimuovi_dipendente_by_index(index)
        self.save_data()

    # restituisce un elemento dalla lista per mezzo dell'indice
    def get_elemento_elemento_by_index(self, index):
        self.model.get_dipendente_by_index(index)

    # salva i dati su un file
    def save_data(self):
        with open(PATH_DATA, 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    # restituisce il totale da aggiungere al bilancio
    def get_totale(self):
        totale = 0
        for dipendente in self.get_lista():
            totale += dipendente.calcola_stipendio()  # Da cambiare nelle altre classi

    def get_numero_dipendenti(self):
        self.model.get_numero_dipendenti()

    def get_totale_stipendi(self):
        lista = self.model.get_lista_dipendenti()
        totale = 0
        for dipendente in lista:
            totale += dipendente.calcola_stipendio()
        return totale

    def get_totale_ore_mensili(self):
        lista = self.model.get_lista_dipendenti()
        totale = 0
        for dipendente in lista:
            totale += dipendente.get_ore_lavorate()
        return totale
