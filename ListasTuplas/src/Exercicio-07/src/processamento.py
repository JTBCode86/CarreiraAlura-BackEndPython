class GestorEstoque:
    @staticmethod
    def unificar_estoques(estoque_a: tuple, estoque_b: tuple) -> list:
        return list(estoque_a + estoque_b)

    @staticmethod
    def calcular_total_geral(estoque_unificado: list) -> int:
        # Soma todas as quantidades da lista
        return sum(produto.quantidade for produto in estoque_unificado)