import numpy as np
x = np.array([[1,2],[5,6],[7,9]])
print(x)
y=x.flatten()
print(y)
x2 = np.reshape(y, [2, 3])
print(x2)