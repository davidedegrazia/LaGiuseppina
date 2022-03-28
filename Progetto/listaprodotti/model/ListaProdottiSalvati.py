
PATH_PRODOTTI_PICKLE = 'listaprodotti/data/ListaProdottiSalvati.pickle'
PATH_PRODOTTI_JSON = 'listaprodotti/data/ListaProdottiSalvati.json'

#Classe che modella la lista dei prodotti presenti nel programma
class ListaProdottiSalvati:
    def __init__(self):
        super(ListaProdottiSalvati, self).__init__()
        self.lista = []
        self.valore = 0
        self.numero_elementi = 0
        self.__len__ = self.lista.__len__()

    def getLista(self):
        return self.lista
