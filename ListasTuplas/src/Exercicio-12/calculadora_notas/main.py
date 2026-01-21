from src.entities.turma import Turma
from src.use_cases.calcular_media import CalcularMediaUseCase
from src.presenters.cli_presenter import CLIPresenter

def main():
    presenter = CLIPresenter()
    
    # Coleta e processamento inicial
    lista_notas = presenter.coletar_notas()
    
    if lista_notas:
        # Injeção das notas na entidade e caso de uso
        turma = Turma(lista_notas)
        calculadora = CalcularMediaUseCase(turma)
        
        # Execução
        resultado_media = calculadora.executar()
        
        # Saída formatada
        presenter.exibir_relatorio(resultado_media)

if __name__ == "__main__":
    main()