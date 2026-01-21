import ast

class CLIPresenter:
    @staticmethod
    def obter_lista_inicial() -> list[str]:
        entrada = input("Lista atual de convidados: ")
        try:
            return ast.literal_eval(entrada)
        except:
            return []

    @staticmethod
    def obter_detalhes_insercao():
        nome = input("Digite o nome do novo convidado: ")
        try:
            posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
            return nome, posicao
        except ValueError:
            print("Posição inválida. Usando posição 1 por padrão.")
            return nome, 1

    @staticmethod
    def exibir_atualizacao(lista: list[str]):
        print(f"Lista atualizada de convidados: {lista}")