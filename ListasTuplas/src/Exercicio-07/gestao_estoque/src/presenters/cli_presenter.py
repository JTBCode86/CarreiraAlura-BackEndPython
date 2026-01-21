class CLIPresenter:
    @staticmethod
    def coletar_estoque(numero: int) -> tuple[str, ...]:
        entrada = input(f"Produtos do estoque {numero} (separados por vírgula): ")
        # Limpa espaços e converte para tupla
        lista_limpa = [item.strip() for item in entrada.split(',')]
        return tuple(lista_limpa)

    @staticmethod
    def exibir_relatorio(estoque_final: tuple):
        print("\nEstoque combinado:")
        print(estoque_final)