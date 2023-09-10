# Exercise 3 - Numpy List
# I used chatGBT to help generate numpy numbers

# Import numpy class
import numpy as nump

# Generate 10 random floats between 0 and 1 using numpy and convert to a list
random_floats = list(nump.random.rand(10))

# Print the list
print("Random Floats:", random_floats)

# Compute and print mean, median, and standard deviation using numpy functions
print("Mean:", nump.mean(random_floats))
print("Median:", nump.median(random_floats))
print("Standard Deviation:", nump.std(random_floats))