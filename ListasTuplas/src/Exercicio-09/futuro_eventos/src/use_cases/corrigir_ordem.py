from ..entities.cronograma import Cronograma

class CorrigirOrdemUseCase:
    def __init__(self, cronograma: Cronograma):
        self.cronograma = cronograma

    def executar(self) -> list[str]:
        # Aplica a reversão definida na entidade
        self.cronograma.inverter_sequencia()
        return self.cronograma.eventos