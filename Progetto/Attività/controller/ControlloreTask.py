class ControlloreTask:
    def __init__(self, task):
        self.model = task

    def modifica(self, descrizione, scadenza, completamento):
        self.model.descrizione = descrizione
        self.model.scadenza = scadenza
        self.model.completamento = completamento

    def get_descrizione(self):
        return self.model.descrizione

    def get_assegnatari(self):
        return self.model.assegnatari

    def get_giorni_alla_scadenza(self):
        return self.model.giorni_alla_scadenza

    def aggiungi_assegnatario(self, assegnatario):
        self.model.aggiungi_assegnatario(assegnatario)
        self.save_data()

    def elimina_assegnatario(self):
        return self.elimina_assegnatario

