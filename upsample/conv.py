import numpy as np
import scipy

h = np.arange(1, 6)

padding = np.zeros(h.shape[0] - 1, h.dtype)
first_col = np.r_[h, padding]
first_row = np.r_[h[0], padding]
H = scipy.linalg.toeplitz(first_col, first_row)

x = np.random.randint(5, size=(5, 1))

conv = scipy.convolve(x.flatten(), h, mode='full')
y = np.dot(H, x)
assert np.all(yconv == ytop.flatten())


