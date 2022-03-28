from Progetto.listaprodotti.model import Prodotto
from Progetto.listaprodotti.model.ProdottoConQuantità import ProdottoConQuantità


class ControlloreProdotto:
    # controllore prodotto con relativa quantità
    def __init__(self, prodotto: Prodotto, quantita: int):
        self.prodotto = prodotto
        self.model = ProdottoConQuantità(prodotto, quantita)

    def get_prodotto(self) -> Prodotto:
        return self.prodotto

    # ritorna il valore del prodotto con relativa quantità
    def get_valore(self) -> int:
        valore = self.model.getProdotto.get_prezzo_su_unita * self.model.get_quantita
        return valore

    def get_prezzo_su_unita(self):
        return self.prodotto.prezzo_su_unita

    def get_nome(self):
        return self.prodotto.nome

    def get_categoria(self):
        return self.prodotto.categria

    def get_tipo_unita(self):
        return self.prodotto.tipo_unita

    # ritorna la stringa relativa alla categoria alla quale il prodotto appartiene

    def get_string_categoria(self):
        Prodotto.get_string_categoria(self.prodotto)
