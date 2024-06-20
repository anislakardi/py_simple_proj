from abc import ABC, abstractmethod
from entreprise import Entreprise

class Employe(ABC ,Entreprise):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salaire_mensuel(self):
        pass
