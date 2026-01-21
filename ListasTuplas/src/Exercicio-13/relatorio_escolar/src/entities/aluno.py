class Aluno:
    def __init__(self, nome: str, idade: int, nota: float):
        self.nome = nome.strip()
        self.idade = idade
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome}\nIdade: {self.idade}\nNota: {self.nota}"