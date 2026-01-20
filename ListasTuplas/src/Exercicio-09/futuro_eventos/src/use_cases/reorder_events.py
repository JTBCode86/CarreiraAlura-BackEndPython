from typing import List
from domain.entities import Evento

class ReorderEventsUseCase:
    """Regra de negócio: Corrigir a sequência invertida."""
    def execute(self, eventos_nomes: List[str]) -> List[Evento]:
        # Inversão da lista para ordem cronológica
        nomes_corrigidos = eventos_nomes[::-1]
        return [Evento(nome) for nome in nomes_corrigidos]