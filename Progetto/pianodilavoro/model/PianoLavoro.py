import json
import os
import pickle

from Progetto.pianodilavoro.model.Task import Task


class PianoLavoro:

    def __init__(self):
        super(PianoLavoro, self).__init__()
        self.piano_lavoro = []
        #self.margine_scadenza
        if os.path.isfile('pianodilavoro/data/lista_task.pickle'):
            with open('pianodilavoro/data/lista_task.pickle', 'rb') as f:
                self.piano_lavoro = pickle.load(f)
        else:
            with open('pianodilavoro/data/lista_task.json') as f:
                piano_lavoro_iniziale = json.load(f)
            for task_iniziale in piano_lavoro_iniziale:
                self.aggiungi_task(Task(task_iniziale["nome_task"], task_iniziale["descrizione"],
                                                    task_iniziale["assegnatari"], task_iniziale["giorni_rimanenti_alla_scadenza"],
                                                    task_iniziale["completata"]))

    def aggiungi_task(self, task):
        self.piano_lavoro.append(task)

    def get_lista_task(self):
        return self.piano_lavoro

    def rimuovi_task_by_index(self, index):
        for task in self.piano_lavoro:
            if task.index == index:
                self.piano_lavoro.remove(task)

    def get_task_by_index(self, index):
        return self.piano_lavoro[index]

    def get_lista_task_completate(self):
        completate = []
        for task in self.piano_lavoro:
            if task.completata == True:
                self.completate.append(task)
        return completate

    def get_lista_task_in_scadenza(self, margine_scadenza):
        in_scadenza = []
        for task in self.piano_lavoro:
            if task.giorni_alla_scadenza <= margine_scadenza:
                self.in_scadenza.append(task)
        return in_scadenza

    def get_lista_task_da_completare(self):
        da_completare = []
        for task in self.piano_lavoro:
            if task.completata == False:
                self.da_completare.append(task)
        return da_completare

    def remove_task(self, task):
        self.piano_lavoro.remove(task)

    def save_data(self):
        with open('pianodilavoro/data/lista_task.pickle', 'wb') as handle:
            pickle.dump(self.piano_lavoro, handle, pickle.HIGHEST_PROTOCOL)

