from ..entities.aluno import Aluno

class ProcessarRelatorioUseCase:
    def executar(self, dados_brutos: list[str]) -> list[Aluno]:
        alunos = []
        # A lógica percorre a lista de 3 em 3 (Nome, Idade, Nota)
        for i in range(0, len(dados_brutos), 3):
            try:
                nome = dados_brutos[i]
                idade = int(dados_brutos[i+1].strip())
                nota = float(dados_brutos[i+2].strip())
                
                novo_aluno = Aluno(nome, idade, nota)
                alunos.append(novo_aluno)
            except (IndexError, ValueError):
                # Ignora entradas malformadas ou incompletas
                continue
        return alunos