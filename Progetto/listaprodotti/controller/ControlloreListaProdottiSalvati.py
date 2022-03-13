from Progetto.listaprodotti.model.ListaProdottiSalvati import ListaProdottiSalvati


class ControlloreListaProdottiSalvati():
    def __init__(self):
        super(ControlloreListaProdottiSalvati, self).__init__()
        self.model = ListaProdottiSalvati()
        self.var == False

    def aggiungi_elemento(self,prodotto):
        self.model.elemento(prodotto)

    def get_lista(self):
        self.get_lista()

    def rimuovi_elemento_by_index(self, index):
        self.model.elemento_by_index(index)

    def get_elemento_by_index(self, prodtto):
        return self.model.elemento_by_index(prodtto)

    def get_id(self, id):
        return id(id)

    def load_data(self):
        self.load_data()

    def save_data(self):
        self.save_data()
        self.var == True

    def is_saved(self):
        return self.var






