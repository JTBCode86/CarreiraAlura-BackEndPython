from entidades import ResultadoCalculo
from processamento import CalculadoraRecursiva
from interface import CliInterface

def executar():
    print("--- ESTUDO DE RECURSIVIDADE ---")
    
    # 1. Entrada
    numero = CliInterface.ler_numero()
    
    if numero is not None:
        # 2. Processamento Recursivo
        valor_final = CalculadoraRecursiva.calcular_fatorial(numero)
        
        # Criando o objeto da entidade
        resultado = ResultadoCalculo(numero, valor_final)
        
        # 3. Saída
        CliInterface.exibir_resultado(resultado)

if __name__ == "__main__":
    executar()