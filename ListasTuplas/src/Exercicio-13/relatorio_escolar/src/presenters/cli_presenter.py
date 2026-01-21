class CLIPresenter:
    @staticmethod
    def coletar_dados_entrada() -> list[str]:
        entrada = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ")
        # Quebra a string por vírgula e remove espaços extras
        return [item.strip() for item in entrada.split(',')]

    @staticmethod
    def exibir_relatorio(alunos: list):
        if not alunos:
            print("\nNenhum dado válido foi processado.")
            return

        for aluno in alunos:
            print(f"\n{aluno}")