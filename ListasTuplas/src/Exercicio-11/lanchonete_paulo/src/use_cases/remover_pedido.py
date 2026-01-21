from ..entities.pedido import Comanda

class RemoverUltimoPedidoUseCase:
    def __init__(self, comanda: Comanda):
        self.comanda = comanda

    def executar(self) -> list[str]:
        self.comanda.remover_ultimo()
        return self.comanda.itens