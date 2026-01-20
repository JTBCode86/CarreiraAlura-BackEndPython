from src.entities.ranking import Ranking
from src.use_cases.update_ranking import UpdateRankingUseCase
from src.presenters.cli_presenter import CLIPresenter

def bootstrap():
    # Inicialização de dados
    ranking_data = Ranking(['Ana', 'Carlos', 'Pedro'])
    use_case = UpdateRankingUseCase(ranking_data)
    presenter = CLIPresenter()

    # Fluxo de execução
    nome_errado, nome_correto = presenter.coletar_dados()
    resultado = use_case.execute(nome_errado, nome_correto)
    
    # Exibição
    presenter.exibir_resultado(resultado)

if __name__ == "__main__":
    bootstrap()