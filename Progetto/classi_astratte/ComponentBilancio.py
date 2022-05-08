from abc import abstractmethod


class ComponentBilancio:

    @abstractmethod
    def aggiungi_a_bilancio(self):
        pass

    @abstractmethod
    def get_valore(self):
        pass

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def aggiorna_totale(self):
        pass

    @abstractmethod
    def is_aggiunto_a_bilancio(self):
        pass

    def get_valore_euro(self):
        valore = self.get_valore()
        centesimi = valore % 100
        if valore >= 100:
            euro = int((valore - centesimi) / 100)
        else:
            euro = 0
        return euro, centesimi
