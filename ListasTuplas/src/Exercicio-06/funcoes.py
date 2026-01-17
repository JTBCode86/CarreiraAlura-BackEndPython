# funcoes.py

def registrar_voluntarios():
    """Realiza o cadastro de voluntários até que 'sair' seja digitado."""
    lista = []
    
    while True:
        nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ").strip()

        if nome.lower() == 'sair':
            break
        
        if nome:
            lista.append(nome)
        else:
            print("Atenção: O nome não pode estar em branco.")
            
    return lista

def exibir_relatorio(lista):
    """Formata e exibe a lista final de voluntários."""
    print("\n" + "="*40)
    print("RELATÓRIO FINAL DA ONG")
    print("="*40)
    print(f"Voluntários registrados: {lista}")
    print(f"Total de ajudantes: {len(lista)}")
    print("="*40)