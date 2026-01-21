class Ranking:
    def __init__(self, corredores: list[str]):
        self._corredores = corredores

    @property
    def lista(self) -> list[str]:
        return self._corredores

    def substituir(self, antigo: str, novo: str) -> bool:
        if antigo in self._corredores:
            idx = self._corredores.index(antigo)
            self._corredores[idx] = novo
            return True
        return False