# Exercise 2 - Fibonacci Sequence
# I used the two links provided in the instructions to learn more about fibonacci and time at
# https://docs.python.org/3/library/time.html and https://www.mathsisfun.com/numbers/fibonacci-sequence.html
# I also used chatGBT to learn more about implementations of the methods in python

# Import time class for recording time
import time

# Import random class to generate a random number
import random

# Fibonacci method
def fibonacci(n):
    if n <= 1:
        return n  #returns the number when n is equal to 1 or less
    else:
        return fibonacci(n-1) + fibonacci(n-2) # Increments and adds the two numbers

# Generate a random number between 15 and 35
num = random.randint(15, 35)

# Start time
start_time = time.time()

# Compute the nth Fibonacci number
result = fibonacci(num)

# Calculate the elapsed time
elapsedTime = time.time() - start_time

# Print the fibonacci result and time taken
print(f"fib({num}) = {result}")
print(f"fib({num}) took {elapsedTime:.5f} seconds")
