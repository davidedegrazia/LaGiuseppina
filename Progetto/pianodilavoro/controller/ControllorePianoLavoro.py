from Progetto.pianodilavoro.model.PianoLavoro import PianoLavoro


class ControllorePianoLavoro:

    def __init__(self):
        super(ControllorePianoLavoro, self).__init__()
        self.model = PianoLavoro()

    # aggiunge una task alla lista_prodotti_salvati
    def aggiungi_task(self, task):
        self.model.aggiungi_task(task)

    # ritorna la lista_prodotti_salvati delle task
    def get_lista_task(self):
        return self.model.get_lista_task()

    def rimuovi_task_by_index(self, index):
        self.model.rimuovi_task_by_index(index)

    def get_task_by_index(self, index):
        return self.model.get_task_by_index(index)

    # ritorna la lista_prodotti_salvati delle task completate
    def get_task_completate(self):
        return self.model.get_lista_task_completate()

    # ritorna la lista_prodotti_salvati delle task in scadenza
    def get_task_in_scadenza(self):
        return self.model.get_lista_task_in_scadenza()

    # ritorna la lista_prodotti_salvati delle task da completare
    def get_task_da_completare(self):
        return self.model.get_lista_task_da_completare()

    # ritorna il margine di scadenza
    def get_margine_di_scadenza(self):
        return self.model.margine_scadenza()

    # modifica il margine di scadenza
    def modifica_margine_di_scadenza(self, margine_di_scadenza_aggiornato):
        self.model.margine_scadenza = margine_di_scadenza_aggiornato

    # elimina una task
    def elimina_task(self, task):
        self.model.remove_task(task)

    # save data
    def save(self):
        self.model.save_data()
