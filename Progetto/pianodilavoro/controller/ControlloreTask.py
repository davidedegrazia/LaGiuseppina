class ControlloreTask():
    def __init__(self, task):
        self.model = task


    def get_descrizione(self):
        return self.model.descrizione

    def get_assegnatari(self):
        return self.model.assegnatari

    def get_giorni_alla_scadenza(self):
        return self.model.giorni_alla_scadenza

    def is_completato(self):
        return self.model.completata

    def modifica_descrizione(self, descrizione_aggiornata):
        self.model.descrizione = descrizione_aggiornata

    def elimina_assegnatario_by_id(self, id):
        self.model.remove_assegnatario(id)

    def aggiungi_assegnatario_by_id(self, id):
        self.model.add_assegnatario(id)

    def modifica_giorni_alla_scadenza(self, scadenza_aggiornata):
        self.model.giorni_alla_scadenza

    def modifica_completamento(self, compl):
        self.model.completata = compl