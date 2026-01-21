from typing import Tuple

class Estoque:
    def __init__(self, produtos: Tuple[str, ...]):
        self._produtos = produtos

    @property
    def produtos(self) -> Tuple[str, ...]:
        return self._produtos