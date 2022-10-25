import unittest

from Progetto.pianodilavoro.model.PianoLavoro import PianoLavoro
from Progetto.pianodilavoro.model.Task import Task

class Testing_PianoLavoro(unittest.TestCase):
    lista = PianoLavoro()

    task = Task("tagliare erba", "abcd", "[Luigi, Mario]", 3, "True")
    task2 = Task("coltivare pomodori", "abcd", "[Filippo]", 6, "False")
    task3 = Task("arare terra", "abcd", "[Luigi, Filippo]", 8, "False")
    task4 = Task("accarezzare le galline", "abcd", "[Mario]", 1, "False")

    lista.aggiungi_task(task)
    lista.aggiungi_task(task2)
    lista.aggiungi_task(task3)
    lista.aggiungi_task(task4)

    def test_aggiungi_nuova_task(self):
        self.assertIn(self.task, self.lista.piano_lavoro)

        self.assertEqual(self.lista.piano_lavoro[0].nome_task, "tagliare erba")
        self.assertEqual(self.lista.piano_lavoro[0].completata, "True")


    def test_task_completate_e_non(self):
        self.assertEqual(self.lista.get_count_task_completate(), 1)
        self.assertEqual(self.lista.get_count_task_da_completare(), 3)

    def test_rimuovi_task_by_index(self):
        index = 2
        self.lista.rimuovi_task_by_index(index)

        self.assertNotIn(self.task3, self.lista.piano_lavoro)
        self.assertIn(self.task, self.lista.piano_lavoro)
        self.assertIn(self.task2, self.lista.piano_lavoro)
        self.assertIn(self.task4, self.lista.piano_lavoro)

    def test_task_by_index(self):
        index = 1
        self.assertEqual(self.lista.get_task_by_index(index), self.task2)