from domain.entities import GuestList

class GuestManager:
    """Service to handle Camila's guest list operations."""
    
    def __init__(self):
        # Initial state as per the requirement
        self.guest_list = GuestList(['Ana', 'Pedro', 'Carlos'])

    def run_insertion_process(self, new_name: str, position: int):
        self.guest_list.add_at_position(new_name, position)
        return self.guest_list.current_guests