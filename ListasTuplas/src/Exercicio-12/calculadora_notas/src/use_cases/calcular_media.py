from ..entities.turma import Turma

class CalcularMediaUseCase:
    def __init__(self, turma: Turma):
        self.turma = turma

    def executar(self) -> float:
        if not self.turma.tem_notas():
            return 0.0
        
        # Lógica de negócio: Média aritmética
        soma = sum(self.turma.notas)
        media = soma / len(self.turma.notas)
        return media