from typing import List
from corrida import Corrida

class Motorista:
    def __init__(self, corridas: List[Corrida], nota: int):
        self.corridas = corridas
        self.nota = nota

    def adicionar_corrida(self, corrida: Corrida):
        self.corridas.append(corrida)
