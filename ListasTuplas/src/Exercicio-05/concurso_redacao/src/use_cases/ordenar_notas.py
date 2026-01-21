from ..entities.concurso import Concurso

class OrdenarNotasUseCase:
    def __init__(self, concurso: Concurso):
        self.concurso = concurso

    def executar(self) -> list[float]:
        # Pegamos a lista original
        notas_atuais = self.concurso.notas
        
        # Aplicamos a ordenação (regra de negócio: ordem crescente)
        # Usamos sorted() para retornar uma nova lista, mantendo a original íntegra até a atualização
        notas_ordenadas = sorted(notas_atuais)
        
        # Atualizamos o estado da entidade
        self.concurso.atualizar_notas(notas_ordenadas)
        
        return notas_ordenadas