class ListaConvidados:
    def __init__(self, nomes_iniciais: list[str]):
        self._convidados = nomes_iniciais

    @property
    def convidados(self) -> list[str]:
        return self._convidados

    def inserir_em_posicao(self, nome: str, posicao: int):
        # Ajusta a posição para o índice 0 (Ex: posição 1 vira índice 0)
        indice = max(0, posicao - 1)
        self._convidados.insert(indice, nome)