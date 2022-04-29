from Progetto.dipendenti.model.ListaDipendenti import ListaDipendenti


class ControlloreListaDipendenti:

    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()

    # aggiunge un elemento alla lista_prodotti_salvati
    def aggiungi_elemento(self, elemento):
        self.model.aggiungi_dipendente(elemento)
        self.save_data()

    # ritorna la lista_prodotti_salvati
    def get_lista(self):
        return self.model.get_lista_dipendenti()

    # rimuove un elemento dalla lista_prodotti_salvati per mezzo dell'indice
    def rimuovi_by_index(self, index):
        self.model.rimuovi_dipendente_by_index(index)
        self.save_data()

    # restituisce un dipendente dalla lista_prodotti_salvati per mezzo dell'indice
    def get_dipendente_by_index(self, index):
        self.model.get_dipendente_by_index(index)

    # restituisce il totale da aggiungere al bilancio
    def get_totale(self):
        totale = 0
        for dipendente in self.get_lista():
            totale += dipendente.calcola_stipendio()  # Da cambiare nelle altre classi

    def get_numero_dipendenti(self):
        return self.model.get_numero_dipendenti()

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
