class CliInterface:
    @staticmethod
    def ler_numero():
        try:
            num = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
            if num < 0:
                print("Por favor, digite apenas números maiores ou iguais a zero.")
                return None
            return num
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")
            return None

    @staticmethod
    def exibir_resultado(resultado_obj):
        print("\n" + "="*40)
        print(f" RESULTADO: {resultado_obj.valor_fatorial}")
        print("="*40)
        print(f"Detalhes: {resultado_obj}")