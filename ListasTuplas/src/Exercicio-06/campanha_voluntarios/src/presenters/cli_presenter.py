class CLIPresenter:
    @staticmethod
    def iniciar_coleta(callback_registro):
        """
        Recebe uma função (callback) para processar cada nome 
        enquanto o usuário não digita 'sair'.
        """
        while True:
            entrada = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
            
            if entrada.lower() == 'sair':
                break
            
            callback_registro(entrada)

    @staticmethod
    def exibir_resultado(voluntarios: list[str]):
        print(f"\nVoluntários registrados: {voluntarios}")