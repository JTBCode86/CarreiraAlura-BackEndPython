import random
from domain.entities import Matrix

class MatrixService:
    """Service responsible for matrix manipulation algorithms."""
    
    @staticmethod
    def fill_sequential(matrix: Matrix):
        counter = 1
        for r in range(matrix.rows):
            for c in range(matrix.cols):
                matrix.set_value(r, c, counter)
                counter += 1

    @staticmethod
    def fill_random(matrix: Matrix, start: int = 1, end: int = 100):
        for r in range(matrix.rows):
            for c in range(matrix.cols):
                random_value = random.randint(start, end)
                matrix.set_value(r, c, random_value)