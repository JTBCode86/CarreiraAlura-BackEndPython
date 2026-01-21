class Comanda:
    def __init__(self, itens: list[str]):
        self._itens = itens

    @property
    def itens(self) -> list[str]:
        return self._itens

    def remover_ultimo(self) -> bool:
        """Remove o último item da lista se ela não estiver vazia."""
        if self._itens:
            self._itens.pop()
            return True
        return False