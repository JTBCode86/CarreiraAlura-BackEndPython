class CalculadoraRecursiva:
    @staticmethod
    def calcular_fatorial(n: int) -> int:
        # 1. Caso Base: O ponto de parada da recursão
        if n == 0 or n == 1:
            return 1
        
        # 2. Caso Recursivo: A função chama a si mesma com um problema menor
        return n * CalculadoraRecursiva.calcular_fatorial(n - 1)