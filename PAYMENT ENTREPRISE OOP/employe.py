from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def salaire_mensuel(self):
        pass
