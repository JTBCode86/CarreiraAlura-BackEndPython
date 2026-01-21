from typing import List

class Concurso:
    def __init__(self, notas: List[float]):
        self._notas = notas

    @property
    def notas(self) -> List[float]:
        return self._notas

    def atualizar_notas(self, novas_notas: List[float]):
        self._notas = novas_notas