# NB I WAS UNABLE TO IMPORT numpy
# Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy 
# arrays are that they are fast, easy to work with, and give users the opportunity to perform 
# calculations across entire arrays.

# In the following example, you will first create two Python lists. Then, you will import 
# the numpy package and create numpy arrays out of the newly created lists.

# Create 2 new lists, height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create two numpy arragys from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Print out the type of np_height
print(type(np_height))

# Element wise calculations
# Now we can perform element wise calculations on height and wight, eg we could calculate
# BMT for each.  These operations are fast and computationally efficient.

# Calculate BMI
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
bmi > 23

# Print only those above 23
bmi[bmi > 23]

# Exercise
# First, convert the list of weights from a list to a Numpy array. Then, convert all of 
# the weights from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram 
# to make your conversion. Lastly, print the resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
import NumpyArrays as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)
