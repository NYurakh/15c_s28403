class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End must be greater or equal to start.")
        return [x**2 for x in range(start, end+1)]