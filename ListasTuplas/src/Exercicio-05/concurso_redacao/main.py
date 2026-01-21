from src.entities.concurso import Concurso
from src.use_cases.ordenar_notas import OrdenarNotasUseCase
from src.presenters.cli_presenter import CLIPresenter

def bootstrap():
    presenter = CLIPresenter()
    
    # 1. Coleta dados
    notas_iniciais = presenter.coletar_notas()
    
    if notas_iniciais:
        # 2. Inicializa Domínio e Caso de Uso
        concurso = Concurso(notas_iniciais)
        servico_ordenacao = OrdenarNotasUseCase(concurso)
        
        # 3. Executa a lógica
        notas_final = servico_ordenacao.executar()
        
        # 4. Exibe o resultado
        presenter.exibir_resultado(notas_final)

if __name__ == "__main__":
    bootstrap()