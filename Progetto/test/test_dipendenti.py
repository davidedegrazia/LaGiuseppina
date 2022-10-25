import unittest

from Progetto.dipendenti.model.Dipendente import Dipendente
from Progetto.dipendenti.model.ListaDipendenti import ListaDipendenti


class Testing_Dipendenti(unittest.TestCase):
    lista = ListaDipendenti()

    dip = Dipendente("Mario", 8, 10, "apprendista", "aaa@gmail.com", 3810002343)
    dip2 = Dipendente("Matteo", 8, 10, "full-time", "matteo@gmail.com", 3810002666)
    dip3 = Dipendente("Davide", 6, 12, "part-time", "dav@icloud.com", 389477564)

    def test_aggiungi_nuovo_dipendente(self):
        self.lista.aggiungi_dipendente(self.dip)

        self.assertIn(self.dip, self.lista.lista_dipendenti)

        self.assertEqual(self.lista.lista_dipendenti[-1].nome, "Mario")
        self.assertEqual(self.lista.lista_dipendenti[-1].ore, 8)
        self.assertEqual(self.lista.lista_dipendenti[-1].compenso_a_ore, 10)

    def test_get_numero_dipendenti(self):
        self.lista.aggiungi_dipendente(self.dip)
        self.lista.aggiungi_dipendente(self.dip2)
        self.lista.aggiungi_dipendente(self.dip3)

        self.assertEqual(self.lista.get_num_dipendenti(), 3)

    def test_rimuovi_dipendente(self):
        self.lista.aggiungi_dipendente(self.dip)
        self.lista.aggiungi_dipendente(self.dip2)
        self.lista.aggiungi_dipendente(self.dip3)

        self.lista.rimuovi_dipendente_by_index(1)

        self.assertIn(self.dip, self.lista.lista_dipendenti)
        self.assertNotIn(self.dip2, self.lista.lista_dipendenti)
        self.assertIn(self.dip3, self.lista.lista_dipendenti)