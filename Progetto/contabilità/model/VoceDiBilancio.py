import uuid

class VoceDiBilancio():

    def __init__ (self, prodotto, entrata, ricorrenza, data):


        self.prodotto = prodotto
        self.entrata = entrata
        self.ricorrenza = ricorrenza
        self.data = data
        self.id = uuid.uuid4()

    def get_prodotto(self):
        return self.prodotto

    def get_entrata(self):
        return self.entrata

    def get_ricorrenza(self):
        return self.ricorrenza

    def get_data(self):
        return self.data

    def get_id(self):
        return self.id













