# Question 3:
# The formula for converting temperatures expressed in Celsius to Fahrenheit is f = 9/5C + 32. 
# Express Cdelta, the temperature difference in Celsius, as a vector formula in terms of Fmin and Fmax

# This problem just wants us to come up with the right formula, but lets do that and run some vectors through it to test the formula out too

import numpy as np

# Create the Fmax array of the elements of our Fmax vector
fmax = [90, 95, 93, 89, 100]

# Create the Fmin array of the elements of our Fmin vector
fmin = [81, 82, 81, 80, 86]

# Use numpy to turn the arrays into matrices and transpose them
fmax_matr = np.transpose(np.matrix(fmax))
fmin_matr = np.transpose(np.matrix(fmin))

# Print for debug
print('Fmax matrix: ', fmax_matr)
print('Fmin matrix: ', fmin_matr, '\n')

# Fahrenheit matrices to Celsius matrices
cmax = np.multiply((5/9),(fmax_matr - 32))
cmin = np.multiply((5/9), (fmin_matr - 32))

# Print for debug
print('Fmax converted to Celsius is: ')
print(cmax, '\n')
print('Fmin converted to Celsius is: ')
print(cmin, '\n')

# Calculate Cdelta
cdelta = cmax - cmin

# Print for debug
print('The answer/Cdelta is: ')
print(cdelta)