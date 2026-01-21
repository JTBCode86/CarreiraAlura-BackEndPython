class Campanha:
    def __init__(self):
        self._voluntarios = []

    @property
    def lista(self) -> list[str]:
        return self._voluntarios

    def adicionar(self, nome: str):
        if nome and len(nome.strip()) > 0:
            self._voluntarios.append(nome.strip())