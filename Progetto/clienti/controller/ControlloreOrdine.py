from Progetto.clienti.model.Ordine import Ordine


class ControlloreOrdine():

    def __init__(self, ordine: Ordine()):
        self.model = ordine

    def get_nome_cliente(self):
        return self.model.nome_cliente

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_data(self):
        return self.model.data

    def get_prodotti(self):
        return self.model.prodotti

    def set_nome_cliente(self, nome: str):
        self.model.nome_cliente = nome

    def set_indirizzo(self, indirizzo: str):
        self.model.indirizzo = indirizzo

    def set_data(self, data):
        self.model.data = data

    def set_prodotti(self):
        pass
