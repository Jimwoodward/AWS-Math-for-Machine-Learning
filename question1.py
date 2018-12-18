# Question 1:
# Let Fmin and Fmin be the vectors containing the min and max temperatures recorded in Seattle in Fahrenheit for a period of 1 week. What is the daily temperature variation (Fdelta = Fmax - Fmin) in that week?


import numpy as np

# Create arrays of the elements of our vectors
fmin = [49, 62, 66, 69, 61] # First question about going from theory to code is that all of my vectors will 1xn vectors. What does a transposed vector look like in code?
fmax = [71, 75, 75, 81, 80]

# Print for debug
print(fmin, "\n")
print(fmax, "\n")

# Use numpy to turn the arrays into vectors
fmin_vec = np.array(fmin)
fmax_vec = np.array(fmax)

# Print for debug
print(fmin_vec, "\n")
print(fmax_vec, "\n")

# Subtract the min temps vector from the max temps vector to create the delta vec
fdelta = fmax_vec - fmin_vec

# Print the answer
print(fdelta)