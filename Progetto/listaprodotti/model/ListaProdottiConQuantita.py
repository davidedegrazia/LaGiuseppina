import uuid

from Progetto.listaprodotti.model.Prodotto import Prodotto, CategoriaProdotti


class ListaProdottiConQuantita:
    def __init__(self, file_json):
        super(ListaProdottiConQuantita, self).__init__()
        self.data_json = file_json
        self.lista = []
        self.__len__ = self.lista.__len__()
        self.id = uuid.uuid4()
        self.valore = 0
        self.lista_tuple_categorie_unita = ListaProdottiConQuantita.get_tuple_categorie_unita()
        self.quantita_per_tupla = [self.get_tuple_categorie_unita().__len__()]
        self.valore_per_categoria = [CategoriaProdotti.__len__()]

    @staticmethod
    def get_tuple_categorie_unita():
        lista_tuple = []
        for categoria in Prodotto.get_lista_categorie():
            for unita in Prodotto.get_lista_unita():
                lista_tuple.append((categoria, unita))
        return lista_tuple

    def get_lista(self):
        return self.lista

    def get_id(self):
        return self.id

    def get_lunghezza(self):
        return self.__len__

    def get_valore(self):
        return self.valore

    def get_quantita_per_categoria_unita(self, tupla):
        return self.quantita_per_tupla

    def get_valore_per_categoria(self, categoria: CategoriaProdotti):
        return self.valore_per_categoria[categoria]

    def get_elemento_by_index(self, index):
        return self.lista[index]

    def getLista(self):
        return self.lista
