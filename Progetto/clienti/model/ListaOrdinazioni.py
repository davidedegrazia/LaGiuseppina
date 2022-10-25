import json
import os
import pickle
from pathlib import Path

from Progetto.clienti.model.Ordine import Ordine

PATH_JSON = Path(r"C:\Users\Utente\Desktop\progettogiuseppina\Progetto\clienti\data\lista_ordinazioni.json")
PATH_PICKLE = Path('clienti/data/lista_ordinazioni.pickle')


class ListaOrdinazioni():

    def __init__(self):
        super(ListaOrdinazioni, self).__init__()
        self.lista_ordinazioni = []
        if os.path.isfile(PATH_PICKLE):
            with open(PATH_PICKLE, 'rb') as f:
                self.lista_ordinazioni = pickle.load(f)
        else:
            with open(PATH_JSON) as f:
                lista_ordinazioni_iniziale = json.load(f)
            for ordine in lista_ordinazioni_iniziale:
                self.aggiungi_ordinazione(Ordine(ordine["nome"], ordine["indirizzo"], ordine["data"], ordine["prodotti"],  ordine["quantita"]))



    def aggiungi_ordinazione(self, ordine):
        self.lista_ordinazioni.append(ordine)

    def rimuovi_ordine_by_index(self, index):
        with open(PATH_JSON) as f:
            data = json.load(f)
            del data[index]
        with open(PATH_JSON) as file:
            json.dump(data, file, indent=4)

    def add_ordine(self, nome_cliente, indirizzo, data_consegna, prodotti, quantita):
        with open(PATH_JSON) as f:
            data = json.load(f)

            new_ordine = {
                "nome": str(nome_cliente),
                "indirizzo": str(indirizzo),
                "data": str(data_consegna),
                "prodotti": prodotti,
                "quantita": quantita
              }

            data.append(new_ordine)

        with open(PATH_JSON, 'w') as file:
            json.dump(data, file, indent=4)


    def modifica_ordine_by_index(self, index, nome_cliente, indirizzo, data_consegna, prodotti, quantita):
        with open(PATH_JSON) as f:
            data = json.load(f)

            ordine_modificato = {
                "nome": str(nome_cliente),
                "indirizzo": str(indirizzo),
                "data": str(data_consegna),
                "prodotti": prodotti,
                "quantita": quantita
              }

            data[index] = ordine_modificato

        with open(PATH_JSON, 'w') as file:
            json.dump(data, file, indent=4)


    def get_ordine_by_index(self, index):
        return self.lista_ordinazioni[index]

    def get_lista_ordinazioni(self):
       return self.lista_ordinazioni

    def get_numero_ordinazioni(self):
        with open(PATH_JSON) as file:
            lista_ordini = json.load(file)
        return len(lista_ordini)
    def save_data(self):
        with open(PATH_JSON, 'wb') as handle:
            pickle.dump(self.lista_ordinazioni, handle, pickle.HIGHEST_PROTOCOL)

    def get_prodotti_by_index(self, index: int):
        return self.lista_ordinazioni[index]['prodotti']

    def get_count_prodotti_by_index(self, index: int) -> int:
        with open(PATH_JSON) as file:
            lista = json.load(file)
        ordine_selezionato = lista[index]
        return len(ordine_selezionato['prodotti'])


    def get_totale_by_index(self, index: int) -> int:
        pass


def testprova():
    lista = ListaOrdinazioni()
    print(lista.get_lista_ordinazioni())
    print(lista.get_numero_ordinazioni())
    print(lista.get_ordine_by_index(0))


if __name__ == "__main__":
    testprova()

