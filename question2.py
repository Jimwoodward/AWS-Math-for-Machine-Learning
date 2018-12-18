# Question 2:
# The formula for converting temperatures expressed in Celsius to Fahrenheit is f = 9/5C + 32. Suppose you are given a vector Fmax
# of maximum temperatures in Fahrenheit. Express Cmax, the maximum daily temperatures in Celsius, as a formula containing scalars
# and vectors. You may use the vector 1 for the vector with all one entries

# This problem just wants us to come up with the right formula, but lets do that and run some vectors through it to test the formula out too


import numpy as np

# Create an Fmax array of the elements of our vector
fmax = [90, 95, 93, 89, 100]

# Print for debug
print(fmax, '\n')

# Use numpy to turn the array into a matrix and to transpose the matrix
fmax_matr = np.transpose(np.matrix(fmax))

# Print for debug
print(fmax_matr, '\n')

# Create the "1 matrix". We meed 5 items so that we can do the element wise multiplication against fmax
one_matr = np.transpose(np.matrix([1, 1, 1, 1, 1]))

# Print for debug
print(one_matr, '\n')

# Create cmax
# Basically what we are doing here, as far as order of operations go...
# 1. Scalar multiplication of 32 by the one matrix. This is so that we have a 1x5 matrix of "32"s. We need this since all 5 elements in fmax need to have 32 subtracted from them
# 2. Subtract our 1x5 matrix of "32"s from the fmax matrix
# 3. Scalar multiplication of 5/9 by the resultant of fmax minus the 32 matrix
cmax_matr = np.multiply((5 / 9), (fmax_matr - (np.multiply(32, one_matr))))

# Print the answer
print(cmax_matr, '\n')


################################################################################################################################################################################
################################################################################################################################################################################

# Bonus work

# 1. Do we really need to multiply 32 by the one_matr in order to get a matrix of 32s so that we can then later subtract that resultant from the fmax matrix, or can the numpy library handle a matrix minus a integer?

# Try out the above formula, but this time subtrac the integer 32 directly from the fmax matrix
cmax_matr = np.multiply((5 / 9), (fmax_matr - 32))

# Print the answer
print(cmax_matr, '\n')