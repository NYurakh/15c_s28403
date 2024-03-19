import math

from generators.cubic_generator import CubicGenerator
from generators.square_generator import SquareGenerator

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

squares2 = SquareGenerator()
print(squares2.generate_squares(1,10))



# Task 4
print("# Task 4")

print([math.sqrt(i) for i in squares2.generate_squares(1, 10)])



# Task 5
print("# Task 5")

try:
    print(squares2.generate_squares(10,1))
except ValueError as e:
    print("Error:", e)




# Task 8
print("# Task 8")

cubics = CubicGenerator()
print(cubics.generate_squares(1, 10))

# Task 9
print("# Task 9")

cubic_gen = CubicGenerator()
try:
    print("Cubes from 5 to 1:", cubic_gen.generate_squares(5, 1))
except ValueError as e:
    print("Error:", e)