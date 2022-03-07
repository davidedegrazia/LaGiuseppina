class ControlloreDipendente:
    def __init__(self, dipendente):
        self.model = dipendente
        #self.da_aggiungere = da_aggiungere_a_bilancio


    def modifica(self, nome, ore, compenso_a_ore, tipo_contratto, email, telefono, id):
        self.model.nome = nome
        self.ore = ore
        #self.model.a_chiamata = a_chiamata
        #if self.model.a_chiamata:
        #    self.model.compenso_fisso = 0
        #    self.model.compenso_a_ore = compenso_a_ore
        #else:
        self.model.compenso_a_ore = compenso_a_ore
        self.model.tipo_contratto = tipo_contratto
        #self.model.compenso_fisso = compenso_fisso
        self.model.email = email
        self.model.telefono = telefono
        self.model.id = id
        #self.model.da_aggiungere = aggiungere_a_bilancio

    def get_totale(self):
        return self.model.calcola_stipendio()

    def get_nome(self):
        return self.model.nome

    #def get_a_chiamata(self):
    #return self.model.a_chiamata

    #def get_compenso_fisso(self):
    #return self.model.compenso_fisso

    def get_ore(self):
        return self.model.ore

    def get_compenso_a_ore(self):
        return self.model.compenso_a_ore

    def get_tipo_contratto(self):
        return self.model.tipo_contratto

    def get_email(self):
        return self.model.email

    def get_telefono(self):
        return self.model.telefono

    def get_id(self):
        return self.model.id

    #def is_da_aggiungere_a_bilancio(self):
    #return self.da_aggiungere
