import numpy
from numpy import random

car = numpy.array([['Tom', 'Bob', 'Sara', 'Rose'], [1,2,3,4], [1,2,3,4], ['Tom', 'Bob', 'Sara', 'Rose']])
# print(car)

# print(type(car))
# print(car.ndim)

import numpy as np

# star =  random.choice([3,4,9,6], p=[0.1,0.3,0.4,0.2], size=(3,6))

star =  random.choice(['John','Peter','Sarah'], p=[0.6,0.1,0.3], size=(4,4))

n = numpy.array([1,2,3,4,5,6,7])

print('Before...')
print(n)

random.shuffle(
    n
)
print('After...')
print(n)

random


# print(star)
# print(dir(car))

# print(car.reshape(4,2,2))
# print(car.reshape(2,4,2))

# print(car[0])

# # Create a 3D array of zeros with shape (layers, rows, columns)
# # Let's imagine a 3-layer cake, each layer is 4x4
# cake = np.zeros((3, 4, 4))

# # Create a 3D array with specific values
# # Shape: 2 layers, 3 rows, 2 columns
# data = np.array([
#     [[10, 11], [12, 13], [14, 15]], # Layer 0
#     [[20, 21], [22, 23], [24, 25]]  # Layer 1
# ])

# # Accessing data
# print(data[1, 0, 0])  # Output: 20 (Layer 1, Row 0, Col 0)