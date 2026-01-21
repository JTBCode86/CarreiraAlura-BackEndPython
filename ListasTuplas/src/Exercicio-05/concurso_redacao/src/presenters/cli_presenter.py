import ast

class CLIPresenter:
    @staticmethod
    def coletar_notas() -> list[float]:
        try:
            entrada = input("Notas: ") # Espera algo como [85, 70, 90]
            # ast.literal_eval converte a string "[85, 70]" em uma lista real de forma segura
            lista = ast.literal_eval(entrada)
            if isinstance(lista, list):
                return [float(n) for n in lista]
            return []
        except (ValueError, SyntaxError):
            print("Erro: Digite a lista no formato [85, 70, 90]")
            return []

    @staticmethod
    def exibir_resultado(notas: list[float]):
        print(f"Notas ordenadas: {notas}")