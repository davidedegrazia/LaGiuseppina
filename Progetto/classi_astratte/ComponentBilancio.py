from abc import ABCMeta, abstractmethod

class ComponentBilancio:

    @abstractmethod
    def aggiungi_a_bilancio(self):
        pass

    @abstractmethod
    def get_totale(self):
        pass

    @abstractmethod
    def aggiorna_totale(self):
        pass

    @abstractmethod
    def is_aggiunto_a_bilancio(self):
        pass
