from src.entities.estoque import Estoque
from src.use_cases.unificar_estoque import UnificarEstoqueUseCase
from src.presenters.cli_presenter import CLIPresenter

def bootstrap():
    presenter = CLIPresenter()
    unificador = UnificarEstoqueUseCase()

    # 1. Coleta de entradas
    dados_1 = presenter.coletar_estoque(1)
    dados_2 = presenter.coletar_estoque(2)

    # 2. Criação das entidades (Dados de entrada imutáveis)
    estoque_1 = Estoque(dados_1)
    estoque_2 = Estoque(dados_2)

    # 3. Execução do Caso de Uso
    estoque_combinado = unificador.executar(estoque_1, estoque_2)

    # 4. Exibição do resultado
    presenter.exibir_relatorio(estoque_combinado.produtos)

if __name__ == "__main__":
    bootstrap()