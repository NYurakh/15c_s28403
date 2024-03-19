import math

# Task 1
print("# Task 1")

squares = [x**2 for x in range(1, 11)]

print(squares)



# Task 2
print("# Task 2")

def e_squares(start, end):
    return [x**2 for x in range(start, end+1)]

print(e_squares(1, 10))



# Task 3
print("# Task 3")

class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end+1)]

squares2 = SquareGenerator()
print(squares2.generate_squares(1,10))



# Task 4
print("# Task 4")

print([math.sqrt(i) for i in squares2.generate_squares(1, 10)])