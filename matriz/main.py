from domain.entities import Matrix
from application.services import MatrixService

def main():
    print("--- Sistema de preenchimento de matriz ---")
    
    try:
        rows = int(input("Entre com o número de linhas: "))
        cols = int(input("Entre com o número de colunas: "))
        
        # Domain Entity Instantiation
        matrix_instance = Matrix(rows, cols)
        
        print("\nEscolha como quer preencher:")
        print("[1] Sequencial")
        print("[2] Aleatório")
        choice = input("Opção: ")

        # Service Orchestration
        if choice == "1":
            MatrixService.fill_sequential(matrix_instance)
        elif choice == "2":
            MatrixService.fill_random(matrix_instance)
        else:
            print("Opção inválida. Saindo.")
            return

        print("\n--- Resultado Final da Matriz ---")
        print(matrix_instance)
        
    except ValueError:
        print("Erro: Por favor, entre apenas com numeros.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()