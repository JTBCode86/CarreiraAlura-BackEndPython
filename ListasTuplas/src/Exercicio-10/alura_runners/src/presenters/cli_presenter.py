class CLIPresenter:
    @staticmethod
    def exibir_resultado(resultado: dict):
        if resultado["sucesso"]:
            print(f"\nO nome {resultado['nome_antigo']} foi substituído por {resultado['nome_novo']}.")
        else:
            print(f"\nErro: O nome '{resultado['nome_antigo']}' não foi encontrado.")
            
        print(f"Lista atualizada: {resultado['lista_atualizada']}")

    @staticmethod
    def coletar_dados():
        errado = input("Digite o nome incorreto: ")
        correto = input("Digite o nome correto: ")
        return errado, correto