from ..entities.estoque import Estoque

class UnificarEstoqueUseCase:
    @staticmethod
    def executar(estoque_a: Estoque, estoque_b: Estoque) -> Estoque:
        # Lógica de unificação de tuplas (concatenação gera uma nova tupla)
        produtos_unificados = estoque_a.produtos + estoque_b.produtos
        return Estoque(produtos_unificados)