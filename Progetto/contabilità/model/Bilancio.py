class Bilancio():
    def __init__(self, entrate, ricavo_totale, uscite, spesa_totale, utile):
        super(Bilancio, self).__init__()
        self.voci_di_bilancio = []

        self.entrate = entrate
        self.ricavo_totale = ricavo_totale
        self.uscite = uscite
        self.spesa_totale = spesa_totale
        self.utile = utile

    def get_entrate(self):
        return self.entrate

    def get_ricavo_totale(self):
        return self.ricavo_totale

    def get_uscite(self):
        return self.uscite

    def get_spesa_totale(self):
        return self.spesa_totale

    def get_utile(self):
        return self.utile



