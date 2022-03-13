from Progetto.listaprodotti.model.ListaProdottiConQuantità import ListaProdottiConQuantita


class ControlloreListaProdotti():
    def __init__(self):
        super(ControlloreListaProdotti, self).__init__()
        self.model = ListaProdottiConQuantita
        self.var == False

    def aggiungi_elemento(self, prodotto):
        self.model.elemento(prodotto)

    def get_elemento_by_id(self, id):
        return self.model.elemento_by_id(id)

    def get_lista(self):
        return self.model.lista()

    def get_id(self, id):
        return self.model.id(id)

    def get_totale(self):
        return self.model.totale

    def rimuovi_elemento_by_index(self, index):
        self.model.elemento_by_index(index)

    def aggiorna_totale(self):
        self.model.totale()

    def load_data(self):
        self.model.data()

    def save_data(self):
        self.save_data()
        self.var == True

    def is_saved(self):
        return self.var























