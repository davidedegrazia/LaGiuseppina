import uuid
import os.path
import pickle

class Dipendente():


    def __init__(self, nome, ore, compenso_a_ore, tipo_contratto, email, telefono):

        self.nome = nome
        self.ore = ore
        self.compenso_a_ore = compenso_a_ore
        self.tipo_contratto = tipo_contratto
        self.email = email
        self.telefono = telefono


    def calcola_stipendio(self):
        compenso_ore_lavorate = self.compenso_a_ore * self.ore
        return compenso_ore_lavorate

    def set_ore_lavorate(self, ore):
        self.ore = ore

    def aggiungi_ore(self, ore):
        self.ore += ore

    def set_contratto_a_chiamata(self, nuovo_tipo):
        self.a_chiamata = nuovo_tipo

    def get_ore_lavorate(self):
        return self.ore

