# Question 1:
# Let Fmin and Fmin be the vectors containing the min and max temperatures recorded in Seattle in Fahrenheit for a period of 1 week. What is the daily temperature variation (Fdelta = Fmax - Fmin) in that week?


import numpy as np

# Create arrays of the elements of our vectors
fmin = [49, 62, 66, 69, 61] # First question about going from theory to code is that all of my vectors will 1xn vectors on input. What does a transposed vector look like in code? Once printed?
fmax = [71, 75, 75, 81, 80]

# Print for debug
print(fmin)
print(fmax, '\n')

# Use numpy to turn the arrays into vectors
fmin_vec = np.array(fmin)
fmax_vec = np.array(fmax)

# Print for debug
print(fmin_vec)
print(fmax_vec, '\n')

# Subtract the min temps vector from the max temps vector to create the delta vector
fdelta = fmax_vec - fmin_vec

# Print the answer
print(fdelta, '\n')


################################################################################################################################################################################
################################################################################################################################################################################

# Bonus work

# 1. What if we treated those 1xn vectors as 1xn matrices?

# Use numpy to turn the arrays into matrices
fmin_matr = np.matrix(fmin)
fmax_matr = np.matrix(fmax)

# Print for debug
print(fmin_matr)
print(fmax_matr, '\n')

# Matrix subtraction
fdelta = fmax_matr - fmin_matr

# Print the answer
print(fdelta, '\n')

# 2. What if we transposed the original vector/matrix data object so that it was nx1 instead of 1xn (or so the vector/matrix as Python knows it is a column vector instead of a row vector)? This is how the first question is actually set up.

# 2.a. Attempt with vectors

# Use numpy to turn the arrays into vectors and then to transpose those vectors
fmin_vec = np.transpose(np.array(fmin))
fmax_vec = np.transpose(np.array(fmax))

# Print for debug
print(fmin_vec)
print(fmax_vec,'\n')

# Vector subtraction
fdelta = fmax_vec - fmin_vec

# Print the answer
print(fdelta, '\n')

# 2.b. Attempt with matrices

# Use numpy to turn the arrays into matrices and then to transpose those matrices
fmin_vec = np.transpose(np.matrix(fmin))
fmax_vec = np.transpose(np.matrix(fmax))

# Print for debug
print(fmin_vec)
print(fmax_vec,'\n')

# Matrix subtraction
fdelta = fmax_vec - fmin_vec

# Print the answer
print(fdelta, '\n')