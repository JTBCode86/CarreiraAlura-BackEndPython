from ..entities.lista_convidados import ListaConvidados

class InserirConvidadoUseCase:
    def __init__(self, lista: ListaConvidados):
        self.lista = lista

    def executar(self, nome: str, posicao: int) -> list[str]:
        if nome:
            self.lista.inserir_em_posicao(nome, posicao)
        return self.lista.convidados