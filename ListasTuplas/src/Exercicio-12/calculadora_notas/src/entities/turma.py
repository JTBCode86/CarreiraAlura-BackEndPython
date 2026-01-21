from typing import List

class Turma:
    def __init__(self, notas: List[float]):
        self._notas = notas

    @property
    def notas(self) -> List[float]:
        return self._notas

    def tem_notas(self) -> bool:
        return len(self._notas) > 0