from src.use_cases.processar_relatorio import ProcessarRelatorioUseCase
from src.presenters.cli_presenter import CLIPresenter

def main():
    presenter = CLIPresenter()
    processador = ProcessarRelatorioUseCase()

    # 1. Coleta a entrada (Ex: "João, 16, 8.5, Maria, 17, 9.2")
    dados_brutos = presenter.coletar_dados_entrada()

    # 2. Processa os dados transformando-os em objetos Aluno
    lista_alunos = processador.executar(dados_brutos)

    # 3. Exibe o relatório formatado
    presenter.exibir_relatorio(lista_alunos)

if __name__ == "__main__":
    main()