class ControlloreVoceDiBilancio:
    def __init__(self, vocedibilancio, elimina_elemento_selezionato):

        self.model = vocedibilancio
        self.elimina_elemento = elimina_elemento_selezionato

    def aggiungi_voce_di_bilancio(self, voce):
        self.voce += voce

    def modifica(self, ricorrenza, costo, quantità):
        self.model.ricorrenza = ricorrenza
        self.model.costo = costo
        self.model.quantità = quantità


    def elimina_elemento_selezionato(self):
        return self.elimina_elemento

