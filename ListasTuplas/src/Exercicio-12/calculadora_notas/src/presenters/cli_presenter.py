class CLIPresenter:
    @staticmethod
    def coletar_notas() -> list[float]:
        try:
            entrada = input("Digite as notas dos alunos separadas por vírgula: ")
            # Converte string para float, tratando espaços
            return [float(nota.strip()) for nota in entrada.split(',')]
        except ValueError:
            print("Erro: Certifique-se de digitar apenas números separados por vírgula.")
            return []

    @staticmethod
    def exibir_relatorio(media: float):
        # Formata para 2 casas decimais conforme o exemplo (7.875 -> 7.88)
        print(f"Média final da turma: {media:.2f}")