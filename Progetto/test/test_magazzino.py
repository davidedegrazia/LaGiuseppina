import unittest

from Progetto.listaprodotti.model.ListaProdottiSalvati import ListaProdottiSalvati
from Progetto.listaprodotti.model.Prodotto import Prodotto


class Testing_Magazzino(unittest.TestCase):
    lista = ListaProdottiSalvati()

    prod = Prodotto("Pesche", "frutta", "al chilo", 1.23)
    prod2 = Prodotto("Prugne", "frutta", "al pezzo", 1.73)
    prod3 = Prodotto("Carciofo", "verdura", "al chilo", 1.20)
    prod4 = Prodotto("Fichi d'India", "frutta", "al chilo", 2.56)

    def test_aggiungi_nuovo_prodotto(self):
        self.lista.aggiungi_elemento(self.prod)

        self.assertIn(self.prod, self.lista.lista_prodotti_salvati)

        self.assertEqual(self.lista.lista_prodotti_salvati[-1].nome, "Pesche")
        self.assertEqual(self.lista.lista_prodotti_salvati[-1].categoria, "frutta")


    def test_numero_frutta(self):
        self.lista.aggiungi_elemento(self.prod)
        self.lista.aggiungi_elemento(self.prod2)
        self.lista.aggiungi_elemento(self.prod3)
        self.lista.aggiungi_elemento(self.prod4)

        self.assertEqual(self.lista.get_num_frutta(), 3)