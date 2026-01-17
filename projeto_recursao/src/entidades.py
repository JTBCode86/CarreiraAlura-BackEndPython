from dataclasses import dataclass

@dataclass(frozen=True)
class ResultadoCalculo:
    numero_original: int
    valor_fatorial: int

    def __repr__(self):
        return f"O fatorial de {self.numero_original} é {self.valor_fatorial}"