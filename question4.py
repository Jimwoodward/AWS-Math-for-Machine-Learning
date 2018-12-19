# Question 4: 
# Often time multiple vector data-points are assembled into a single matrix where the columns of
# the matrix are the collection of vectors in your data. Which of the following is the correct way of
# assembling the following data points along with their difference, into a single matrix?

import numpy as np

# Create the fmin and fmax arrays
fmin = [49, 62, 66, 69, 61]
fmax = [71, 75, 75, 81, 80]

# Create the fmin and fmax matrices
fmin_matr = np.transpose(np.matrix(fmin))
fmax_matr = np.transpose(np.matrix(fmax))

# Print for debug
print('Fmin matrix: ')
print(fmin_matr, '\n')
print('Fmax matrix: ')
print(fmax_matr, '\n')

# Calculate the difference between Fmax and Fmin
fdelta_matr = fmax_matr - fmin_matr

# Print for debug
print('Fdelta is: ')
print(fdelta_matr, '\n')

# Concatenate the Fmin, Fmax, and Fdelta matrices along the x axis (axis 1)
fminmax_matr = np.concatenate((fmin_matr, fmax_matr, fdelta_matr), axis = 1)

# Print for debug
print('Fmin concatenated with Fmax: ')
print(fminmax_matr, '\n')