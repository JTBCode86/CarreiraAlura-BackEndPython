from interface import CliInterface
from processamento import GestorEstoque

def start():
    # 1. Entrada
    unidade_a = CliInterface.solicitar_dados_estoque("Norte")
    unidade_b = CliInterface.solicitar_dados_estoque("Sul")

    # 2. Processamento
    resultado = GestorEstoque.unificar_estoques(unidade_a, unidade_b)
    soma_total = GestorEstoque.calcular_total_geral(resultado)

    # 3. Saída
    CliInterface.exibir_relatorio(resultado, soma_total)

if __name__ == "__main__":
    start()