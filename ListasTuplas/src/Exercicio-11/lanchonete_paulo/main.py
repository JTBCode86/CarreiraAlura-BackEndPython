from src.entities.pedido import Comanda
from src.use_cases.remover_pedido import RemoverUltimoPedidoUseCase
from src.presenters.cli_presenter import CLIPresenter

def main():
    presenter = CLIPresenter()
    
    # 1. Coleta dados da interface
    lista_inicial = presenter.coletar_pedidos()
    
    # 2. Inicializa Entidades e Casos de Uso (Injeção de Dependência)
    comanda = Comanda(lista_inicial)
    caso_de_uso = RemoverUltimoPedidoUseCase(comanda)
    
    # 3. Executa a lógica de negócio
    pedidos_finais = caso_de_uso.executar()
    
    # 4. Exibe o resultado
    presenter.exibir_resultado(pedidos_finais)

if __name__ == "__main__":
    main()