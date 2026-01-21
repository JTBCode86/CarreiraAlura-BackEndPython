from ..entities.campanha import Campanha

class RegistrarVoluntarioUseCase:
    def __init__(self, campanha: Campanha):
        self.campanha = campanha

    def executar(self, nome: str):
        # Aqui poderiam existir regras como: "Não permitir nomes duplicados"
        self.campanha.adicionar(nome)

    def obter_todos(self) -> list[str]:
        return self.campanha.lista