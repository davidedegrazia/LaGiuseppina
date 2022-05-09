import uuid

from enum import IntEnum


# nome del prodotto, categoria a cui appartiene, tipo di unita con cui si misura, prezzo su unita di misura


class CategoriaProdotti(IntEnum):
    FRUTTA = 0
    VERDURA = 1
    ERBE_AROMATICHE = 2
    ALTRO = 3

    def __str__(self):
        return {
            CategoriaProdotti.FRUTTA: "Frutta",
            CategoriaProdotti.VERDURA: "Verdura",
            CategoriaProdotti.ERBE_AROMATICHE: "Erbe aromatiche",
            CategoriaProdotti.ALTRO: "Altro"
        }.get(self, "None")


class UnitaDiMisura(IntEnum):
    PEZZO = 0
    KILOGRAMMO = 1
    LITRO = 2

    def __str__(self):
        return {
            UnitaDiMisura.KILOGRAMMO: "Kg",
            UnitaDiMisura.LITRO: "L",
            UnitaDiMisura.PEZZO: "Pz",
        }.get(self, "None")


# classe che descrive un prodotto dell'attività agricola
# nome del prodotto, categoria a cui appartiene, tipo di unita con cui si misura, prezzo su unita di misura
class Prodotto:
    def __init__(self, nome: str, categoria: str, tipo_unita, prezzo_su_unita):
        self.nome = nome
        self.categoria = categoria
        self.tipo_unita = tipo_unita
        self.prezzo_su_unita = prezzo_su_unita
        self.quantita = 0


    def modifica(self, nome, categoria, prezzo_su_unita, tipo_unita, quantita ):
        self.nome = nome
        self.categoria = categoria
        self.prezzo_su_unita = prezzo_su_unita
        self.tipo_unita = tipo_unita
        self.quantita = quantita

    def get_prezzo_su_unita(self):
        return float(self.prezzo_su_unita)

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_tipo_unita(self):
        return self.tipo_unita

    def get_quantita(self):
        return self.quantita

    def set_prezzo_su_unita(self, nuovo):
        self.prezzo_su_unita = nuovo

    def set_quantita(self, quantita):
        self.quantita = quantita

    def set_nome(self, nuovo):
        self.nome = nuovo

    def set_categoria(self, nuovo):
        self.categoria = nuovo

    def set_tipo_unita(self, nuovo):
        self.tipo_unita = nuovo


    #Ritorna la lista_prodotti_salvati delle categorie dei prodotti (ogni elemento della lista_prodotti_salvati è di tipo CategoriaProdotti)
    @staticmethod
    def get_lista_categorie():
        lista = []
        for categoria in CategoriaProdotti:
            lista.append(categoria)
        return lista

    #Ritorna la lista_prodotti_salvati delle unità di misura dei prodoti (ogni elemento della lista_prodotti_salvati è di tipo UnitaDiMisura)
    @staticmethod
    def get_lista_unita():
        lista = []
        for unita in UnitaDiMisura:
            lista.append(unita)
        return lista

    #Ritorna una stringa che descrive il prezzo del prodotto
    def get_string_prezzo(self):
       return str(self.get_prezzo_su_unita() / 100) + ' €/' + str(self.get_prezzo_su_unita())

    def __str__(self):
        dict = {
            "nome": self.get_nome(),
            "categoria": str(self.get_categoria()),
            "tipo_unita": str(self.get_prezzo_su_unita()),
            "prezzo_su_unita": self.get_string_prezzo(),
            "quantita": str(self.get_quantita())
        }
        return str(dict)
