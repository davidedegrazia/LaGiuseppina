from Progetto.dipendenti.model.ListaDipendenti import ListaDipendenti


class Task():

     def __init__(self, nome, descrizione, giorni_rimanenti, completata):

          self.nome = nome
          self.descrizione = descrizione
          self.giorni_rimanenti = giorni_rimanenti
          self.completata = completata
          self.assegnatari = ListaDipendenti()



