from entidades import Produto

class CliInterface:
    @staticmethod
    def solicitar_dados_estoque(nome_unidade):
        print(f"\n--- Cadastro da Unidade: {nome_unidade} ---")
        produtos = []
        while True:
            nome = input("Produto (ou 'fim'): ").strip()
            if nome.lower() == 'fim': break
            try:
                qtd = int(input(f"Quantidade de {nome}: "))
                # Já salvamos o produto com o nome da unidade
                produtos.append(Produto(nome, qtd, nome_unidade))
            except ValueError:
                print("Erro: Digite um número inteiro.")
        return tuple(produtos)

    @staticmethod
    def exibir_relatorio(lista_unificada, total_geral):
        print("\n" + "="*45)
        print(f"{'RELATÓRIO UNIFICADO DE ESTOQUE':^45}")
        print("="*45)
        
        for item in lista_unificada:
            print(f"• {item}")
        
        print("-" * 45)
        print(f"TOTAL GERAL EM ESTOQUE: {total_geral} unidades")
        print("="*45)