class CLIPresenter:
    @staticmethod
    def coletar_pedidos() -> list[str]:
        entrada = input("Pedidos feitos (separados por vírgula): ")
        # Transforma a string em lista e limpa espaços extras
        return [item.strip() for item in entrada.split(',')]

    @staticmethod
    def exibir_resultado(pedidos_finais: list[str]):
        print(f"Pedidos finais: {pedidos_finais}")