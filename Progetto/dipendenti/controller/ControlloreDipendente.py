class ControlloreDipendente:
    def __init__(self, dipendente):
        self.model = dipendente



    def modifica(self, nome, ore, compenso_a_ore, tipo_contratto, email, telefono, id):
        self.model.nome = nome
        self.ore = ore
        self.model.compenso_a_ore = compenso_a_ore
        self.model.tipo_contratto = tipo_contratto
        self.model.email = email
        self.model.telefono = telefono
        self.model.id = id


    def get_totale(self):
        return self.model.calcola_stipendio()

    def get_nome(self):
        return self.model.nome


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


