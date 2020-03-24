import numpy as np
x = np.array([[1, 2, 3], [3, 4, 6]])

print(np.size(x))

print(np.size(x, 1))

print(np.std(x))

print(np.std(x, 1))

print(x.sum())

print(np.random.rand(50))
print(np.random.normal(size=100))
print(np.array(range(0,100),float)/100)