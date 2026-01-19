class GuestList:
    def __init__(self, initial_guests: list = None):
        # Encapsulates the list to prevent direct external manipulation
        self._guests = initial_guests if initial_guests else []

    @property
    def current_guests(self):
        """Returns a copy of the list to maintain encapsulation."""
        return list(self._guests)

    def add_at_position(self, name: str, position: int):
        """
        Inserts a guest at a specific position.
        In Python, lists are 0-indexed. Position 1 = index 0.
        """
        index = position - 1  # Adjusting for human-readable position
        
        if 0 <= index <= len(self._guests):
            self._guests.insert(index, name)
        else:
            # If position is out of bounds, we append to the end
            self._guests.append(name)

    def __str__(self):
        return str(self._guests)