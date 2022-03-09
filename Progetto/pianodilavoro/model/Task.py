from Progetto.dipendenti.model.ListaDipendenti import ListaDipendenti


class Task():

   def __init__(self, nome_task, descrizione, assegnatari, giorni_alla_scadenza, completata):


        self.nome_task = nome_task
        self.descrizione = descrizione
        self.assegnatari = assegnatari
        self.giorni_alla_scadenza = giorni_alla_scadenza
        self.completata = completata
