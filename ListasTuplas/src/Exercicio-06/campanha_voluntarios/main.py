from src.entities.campanha import Campanha
from src.use_cases.registrar_voluntario import RegistrarVoluntarioUseCase
from src.presenters.cli_presenter import CLIPresenter

def main():
    # Inicialização
    campanha_ong = Campanha()
    use_case = RegistrarVoluntarioUseCase(campanha_ong)
    presenter = CLIPresenter()

    # Execução do loop de coleta
    # Passamos o método 'executar' do use_case como comando para o presenter
    presenter.iniciar_coleta(use_case.executar)

    # Finalização e exibição
    lista_final = use_case.obter_todos()
    presenter.exibir_resultado(lista_final)

if __name__ == "__main__":
    main()