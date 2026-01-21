from src.entities.cronograma import Cronograma
from src.use_cases.corrigir_ordem import CorrigirOrdemUseCase
from src.presenters.cli_presenter import CLIPresenter

def main():
    # Dados fornecidos pelo problema
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    
    # Inicialização das camadas
    cronograma = Cronograma(eventos_registrados)
    use_case = CorrigirOrdemUseCase(cronograma)
    presenter = CLIPresenter()

    # Fluxo de execução
    presenter.exibir_estado_inicial(eventos_registrados)
    
    # O Use Case corrige a ordem internamente na entidade
    lista_corrigida = use_case.executar()
    
    presenter.exibir_estado_final(lista_corrigida)

if __name__ == "__main__":
    main()