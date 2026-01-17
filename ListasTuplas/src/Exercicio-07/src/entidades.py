from dataclasses import dataclass

@dataclass(frozen=True)
class Produto:
    nome: str
    quantidade: int
    unidade: str  # Indica de onde o produto veio
    
    def __repr__(self):
        return f"[{self.unidade}] {self.nome}: {self.quantidade} unidades"