class Cronograma:
    def __init__(self, eventos: list[str]):
        self._eventos = eventos

    @property
    def eventos(self) -> list[str]:
        return self._eventos

    def inverter_sequencia(self):
        """Altera a ordem interna dos eventos para a inversa."""
        self._eventos.reverse()