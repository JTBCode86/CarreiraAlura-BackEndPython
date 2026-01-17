from funcoes import registrar_voluntarios, exibir_relatorio

def inicio():
    print("INICIANDO SISTEMA DE CADASTRO...")
    
    # Chama a função de registro e guarda o resultado na variável 'voluntarios'
    voluntarios = registrar_voluntarios()
    
    # Chama a função de exibição passando a lista preenchida
    exibir_relatorio(voluntarios)

if __name__ == "__main__":
    inicio()