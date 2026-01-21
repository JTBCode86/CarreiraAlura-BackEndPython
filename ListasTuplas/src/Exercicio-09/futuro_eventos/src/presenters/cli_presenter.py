class CLIPresenter:
    @staticmethod
    def exibir_estado_inicial(eventos: list[str]):
        print(f"Eventos registrados (ordem incorreta): {eventos}")

    @staticmethod
    def exibir_estado_final(eventos: list[str]):
        print(f"Lista final (sequência correta): {eventos}")