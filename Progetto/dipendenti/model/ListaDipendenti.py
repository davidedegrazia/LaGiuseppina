class ListaDipendenti:

    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []

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
        len(self.lista_dipendenti)
