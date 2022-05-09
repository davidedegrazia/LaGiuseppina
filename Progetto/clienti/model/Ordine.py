import json


class Ordine():


    def __init__(self, nome_cliente: str, indirizzo: str, data, prodotti: [], quantita: []):

        self.nome_cliente = nome_cliente
        self.indirizzo = indirizzo
        self.data = data
        self.prodotti = prodotti
        self.quantita = quantita

    def get_nome_cliente(self):
        return self.nome_cliente

    def get_indirizzo(self):
        return self.indirizzo

    def get_data(self):
        return self.data

    def get_prodotti(self):
        return self.prodotti

    def get_prodotto_by_index(self, index:int):
        return self.prodotti[index]

    def get_quantita(self):
        return self.quantita

    def get_quantita_by_index(self, index:int):
        return self.quantita[index]

    def set_nome_cliente(self, nome: str):
        self.nome_cliente = nome

    def set_indirizzo(self, indirizzo: str):
        self.indirizzo = indirizzo

    def set_data(self, data):
        self.data = data

    def set_prodotti(self):
        pass

    def get_count_prodotti(self):
        return len(self.prodotti)


#if __name__ == "__main__":
 #   with open("/Users/davidedegrazia/PycharmProjects/LaGiuseppina/Progetto/clienti/data/lista_ordinazioni.json", 'r') as f:
  #      data = json.load(f)
   #     ordine = Ordine(data[0]['nome'], data[0]['indirizzo'], data[0]['data'], data[0]['prodotti'], data[0]['quantita'])
    #    print(ordine.get_quantita())
