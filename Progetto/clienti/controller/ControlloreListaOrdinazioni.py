from Progetto.clienti.model.ListaOrdinazioni import ListaOrdinazioni
from Progetto.clienti.model.Ordine import Ordine


class ControlloreListaOrdinazioni():

    def __init__(self):
        super(ControlloreListaOrdinazioni, self).__init__()
        self.model = ListaOrdinazioni()

    def aggiungi_ordinazione(self, ordine):
        self.model.aggiungi_ordinazione(ordine)

    def add_ordine(self, nome_cliente, indirizzo, data_consegna, prodotti, quantita):
        self.model.add_ordine(nome_cliente, indirizzo, data_consegna, prodotti, quantita)

    def rimuovi_ordine_by_index(self, index: int):
        self.model.rimuovi_ordine_by_index(index)

    def get_ordine_by_index(self, index: int):
        return self.model.get_ordine_by_index(index)

    def get_lista_ordinazioni(self):
        return self.model.get_lista_ordinazioni()

    def get_numero_ordinazioni(self):
        return self.model.get_numero_ordinazioni()

    def save_data(self):
        self.model.save_data()

    def get_prodotti_by_index(self, index: int):
        return self.model.get_prodotti_by_index(index)

    def get_count_prodotti_by_index(self, index: int) -> int:
        return self.model.get_count_prodotti_by_index(index)



