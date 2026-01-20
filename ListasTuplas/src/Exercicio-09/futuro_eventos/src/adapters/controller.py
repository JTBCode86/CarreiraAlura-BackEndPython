from use_cases.reorder_events import ReorderEventsUseCase

class EventController:
    def __init__(self, use_case: ReorderEventsUseCase):
        self.use_case = use_case

    def handle(self, raw_data: list):
        # Transforma os dados brutos em objetos de domínio via Use Case
        cronograma = self.use_case.execute(raw_data)
        
        print("\n[Futuro Eventos] Cronograma Corrigido:")
        for idx, evento in enumerate(cronograma, 1):
            print(f"{idx}. {evento.nome}")