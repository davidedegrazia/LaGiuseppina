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
    def __init__(self, nome: str, categoria: CategoriaProdotti, tipo_unita: UnitaDiMisura, prezzo_su_unita):
        self.nome = nome.capitalize()
        self.categoria = categoria
        self.tipo_unita = tipo_unita
        self.prezzo_su_unita = prezzo_su_unita
        self.id = uuid.uuid4()

    def modifica(self, nome, categoria, prezzo_su_unita, tipo_unita):
        self.nome = nome
        self.categoria = categoria
        self.prezzo_su_unita = prezzo_su_unita
        self.tipo_unita = tipo_unita

    def get_prezzo_su_unita(self):
        return self.prezzo_su_unita

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        self.categoria = self.categoria
        return self.categoria

    def get_tipo_unita(self):
        return self.tipo_unita

    def set_prezzo_su_unita(self, nuovo):
        self.prezzo_su_unita = nuovo

    def set_nome(self, nuovo):
        self.nome = nuovo

    def set_categoria(self, nuovo):
        self.categoria = nuovo

    def set_tipo_unita(self, nuovo):
        self.tipo_unita = nuovo

    def get_id(self):
        return self.id

    #Ritorna la lista delle categorie dei prodoti (ogni elemento della lista è di tipo CategoriaProdotti)
    @staticmethod
    def get_lista_categorie():
        lista = []
        for categoria in CategoriaProdotti:
            lista.append(categoria)
        return lista

    #Ritorna la lista delle unità di misura dei prodoti (ogni elemento della lista è di tipo UnitaDiMisura)
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
            "Nome": self.get_nome(),
            "Categoria": str(self.get_categoria()),
            "Unità di misura": str(self.get_prezzo_su_unita()),
            "Prezzo": self.get_string_prezzo()
        }
        return str(dict)
