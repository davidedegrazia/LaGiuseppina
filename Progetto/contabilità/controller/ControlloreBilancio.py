PATH_DATA = 'Progetto/data/bilancio.pickle'
import pickle


class ControlloreBilancio():
    def __init__(self):
        with open(PATH_DATA, 'wb') as file:
            lista = pickle.load(file)
            self.model = lista


    def get_lista(self):
        return self.model.get_voci_di_bilancio()

    



