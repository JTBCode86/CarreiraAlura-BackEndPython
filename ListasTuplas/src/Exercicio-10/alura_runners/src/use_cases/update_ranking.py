from ..entities.ranking import Ranking

class UpdateRankingUseCase:
    def __init__(self, ranking: Ranking):
        self.ranking = ranking

    def execute(self, nome_errado: str, nome_correto: str) -> dict:
        sucesso = self.ranking.substituir(nome_errado, nome_correto)
        return {
            "sucesso": sucesso,
            "nome_antigo": nome_errado,
            "nome_novo": nome_correto,
            "lista_atualizada": self.ranking.lista
        }