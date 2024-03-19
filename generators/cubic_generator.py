from generators.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End must be greater or equal to start.")
        return [x**3 for x in range(start, end+1)]