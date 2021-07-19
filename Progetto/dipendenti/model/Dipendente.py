import uuid


class Dipendente():

    #le ore sono le ore da contratto per i dipendenti a ore fisse mentre sono le ore lavorate per i dipendenti a achiamata
    def __init__(self, nome, a_chiamata, ore, compenso_fisso, compenso_a_ore, email, telefono, aggiungere_a_bilancio):

        self.nome = nome
        self.a_chiamata = a_chiamata
        if self.a_chiamata:
            self.compenso_fisso = 0
            self.compenso_a_ore = compenso_a_ore
            self.ore = 0
        else:
            self.compenso_a_ore = 0
            self.compenso_fisso = compenso_fisso
            self.ore = ore
        self.email = email
        self.telefono = telefono
        self.da_aggiungere = aggiungere_a_bilancio
        self.id = uuid.uuid4()

    def calcola_stipendio(self):
        compenso_ore_lavorate = self.compenso_a_ore * self.ore
        return self.compenso_fisso + compenso_ore_lavorate

    def set_ore_lavorate(self, ore):
        self.ore = ore

    def aggiungi_ore(self, ore):
        self.ore += ore

    def set_contratto_a_chiamata(self, nuovo_tipo):
        self.a_chiamata = nuovo_tipo

    def get_ore_lavorate(self):
            return self.ore
