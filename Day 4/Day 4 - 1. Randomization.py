# RANDOMIZATION MODULE IN PYTHON

# The "random" library is an automatic part of Python's code which you can import into any code
import random

# You can always create sub-files that are their own modules to import for specific functions
import my_module    # This is just a test file that has some values in it

random_integer = random.randint(1, 10)      # Random integer
print(random_integer)

random_float = random.random()                    # Random float between 0.0 and 1.0 (not including 1)
print(random_float)

print(random_float * 5)                           # Now it can generate random floats between 0 and 5 (not 5 though)

# You can call values from any module using the naming format "module.value"
print(my_module.pi)

# You can use random number for just about anything; like the fake love score thing
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")
