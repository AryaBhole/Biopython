import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = arr * 2
print(result)

data = np.arange(20).reshape(4, 5)
print(data)
#print(data[:, 2])
print(data[1:3, 2:5])

rng = np.random.default_rng()

print(rng.integers(1, 11, 2))