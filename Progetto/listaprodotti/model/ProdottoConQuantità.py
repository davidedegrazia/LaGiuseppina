from Progetto.listaprodotti.model import Prodotto
from Progetto.listaprodotti.model.Prodotto import CategoriaProdotti

#Un'istanza di questa classe descrive un prodotto a cui è associata una quantita: utile per descrivere un prodotto in un ordine o nel magazzino
class ProdottoConQuantità(Prodotto.Prodotto):
    def __init__(self, nome, categoria, tipo_unita, prezzo_su_unita, quantita):
        super().__init__(nome, categoria, tipo_unita, prezzo_su_unita)
        self.quantita = quantita



    #Ritorna un'istanza del Prodotto associato
    def get_prodotto(self) -> Prodotto:
        return Prodotto.Prodotto(self.nome, self.categoria, self.tipo_unita, self.prezzo_su_unita)

    def get_quantita(self) -> int:
        return self.quantita

    def set_quantita(self, quantita: int):
        self.quantita = quantita

    #Ritorna il valore IN CENTESIMI del prodotto
    def get_valore(self):
        valore = self.get_prezzo_su_unita() * self.get_quantita()
        return valore

    #Metodo statico che ritorna un istanza di ProdottoConQuantia
    #prodotto: Prodotto associato
    #quantita: quantita di prodotto misurata secondo il tipo di unità che è descritta in prodotto
    @staticmethod
    def costruttore_da_prodotto(prodotto: Prodotto, quantita:int):
        return ProdottoConQuantità(prodotto.get_nome(), prodotto.get_categoria(), prodotto.get_tipo_unita(), prodotto.get_prezzo_su_unita(), quantita)

    def __str__(self):
        tupl = (self.get_nome(), self.get_string_prezzo())
        return str(tupl)
