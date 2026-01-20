from use_cases.reorder_events import ReorderEventsUseCase
from adapters.controller import EventController

def main():
    # Dados de entrada (poderiam vir de um DB ou API)
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

    # Instanciação das camadas (Injeção de Dependência)
    use_case = ReorderEventsUseCase()
    controller = EventController(use_case)

    # Execução
    controller.handle(eventos_registrados)

if __name__ == "__main__":
    main()