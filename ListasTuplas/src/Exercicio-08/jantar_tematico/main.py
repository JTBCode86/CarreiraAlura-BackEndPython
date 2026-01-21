from src.entities.lista_convidados import ListaConvidados
from src.use_cases.inserir_convidado import InserirConvidadoUseCase
from src.presenters.cli_presenter import CLIPresenter

def main():
    presenter = CLIPresenter()
    
    # 1. Setup Inicial
    nomes_iniciais = presenter.obter_lista_inicial()
    lista_entidade = ListaConvidados(nomes_iniciais)
    use_case = InserirConvidadoUseCase(lista_entidade)

    # 2. Captura Novos Dados
    novo_nome, posicao = presenter.obter_detalhes_insercao()

    # 3. Execução
    lista_atualizada = use_case.executar(novo_nome, posicao)

    # 4. Saída
    presenter.exibir_atualizacao(lista_atualizada)

if __name__ == "__main__":
    main()