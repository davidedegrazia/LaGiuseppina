
class Magazzino:
    def __init__(self):
        super(Magazzino, self).__init__()
        self.lista_magazzino = []
        self.valore = 0
        self.numero_elementi = 0
        self.__len__ = self.lista_prodotti_salvati.__len__()

        if os.path.isfile('/Users/davidedegrazia/PycharmProjects/LaGiuseppina/Progetto/listaprodotti/data/ListaProdottiSalvati.pickle'):
                with open('/Users/davidedegrazia/PycharmProjects/LaGiuseppina/Progetto/listaprodotti/data/ListaProdottiSalvati.pickle','rb') as f:
                    self.lista_prodotti_salvati = pickle.load(f)
        else:
            with open('/Users/davidedegrazia/PycharmProjects/LaGiuseppina/Progetto/listaprodotti/data/ListaProdottiSalvati.json') as f:
                lista_prodotti_salvati_iniziale = json.load(f)
            for prodotto in lista_prodotti_salvati_iniziale:
                self.aggiungi_elemento(Prodotto(prodotto['nome'], prodotto['categoria'], prodotto['tipo_unita'],
                                                prodotto['prezzo_su_unita']))

    def aggiungi_elemento(self, prodotto: Prodotto):
        for elemento in self.lista_prodotti_salvati:
            if elemento.get_nome().lower() == prodotto.get_nome().lower():
               raise ValueError('L\'elemento è già presente all\'interno della lista_prodotti_salvati')

        self.lista_prodotti_salvati.append(prodotto)
        #self.lista_prodotti_salvati.sort(key=Prodotto.get_nome)









