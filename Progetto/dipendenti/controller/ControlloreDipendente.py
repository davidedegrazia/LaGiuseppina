class ControlloreDipendente:
    def __init__(self, dipendente, da_aggiungere_a_bilancio):
        self.model = dipendente
        self.da_aggiungere = da_aggiungere_a_bilancio


    def modifica(self, nome, a_chiamata, compenso_fisso, compenso_a_ore, email, telefono, id, aggiungere_a_bilancio):
        self.model.nome = nome
        self.model.a_chiamata = a_chiamata
        if self.model.a_chiamata:
            self.model.compenso_fisso = 0
            self.model.compenso_a_ore = compenso_a_ore
        else:
            self.model.compenso_a_ore = 0
            self.model.compenso_fisso = compenso_fisso
        self.model.email = email
        self.model.telefono = telefono
        self.model.id = id
        self.model.da_aggiungere = aggiungere_a_bilancio

    def get_totale(self):
        return self.model.calcola_stipendio()

    def get_nome(self):
        return self.model.nome

    def get_a_chiamata(self):
        return self.model.a_chiamata

    def get_compenso_fisso(self):
        return self.model.compenso_fisso

    def get_email(self):
        return self.model.email

    def get_telefono(self):
        return self.model.telefono

    def get_id(self):
        return self.model.id

    def is_da_aggiungere_a_bilancio(self):
        return self.da_aggiungere
