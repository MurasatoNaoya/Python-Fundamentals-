

import math

# help(math) Why does the program not print anything after when 'help' is used? 

value = 4.35

print(math.floor(value)) # The floor method returns the nearest integer value, which is less than or equal to the specific value. 

print(math.ceil(value))  # The ceil method returns the nearest rounded up integer. If there are no decimals to round up, the number will just be left alone. 

# The round method round the inputted number to the nearest integer, hwoever, it will always prioritise returning an even integer. 

value1 = 4.5
value2 = 5.5 

print(round(value1)) # In this case, the round method will round downwards to the even integer of 4.

print(round(value2)) # In this case however, the round method will round upwards to the even integer of 6. 

# This is a means of balacing out estimates. If all inputs were rounded down, over time, your output would be a lot smaller than it should be. 
# By having an alternating direction of rounding, the uncertiaty of our total output would be smaller. 
# The opposite is true for rounding upwards. 


# You can also retrieve a number of mathematical constants using the 'math' module. 

print(math.pi)

# If you want to use pi without referring to it via a method, you must import it from the math module first. 
# Using 'import math', you have access to the module, but you have to open the functions from the module using methods. Things like pi are treated as attributes to the class 'math'. 
# If you want to have access to all functions in standard form and not .NAME form, then you have to import all of the modules like so - from math import * ; or for just pi - from math import pi.

from math import *
# or
from math import pi 

print(pi)

print(math.e)
print(e) # We can refer to e as a constant and not a method, due to using importing all functions from math. Using from math import * 

# There are also representations for things that are not numbers or are infinite. 

print(math.inf) # You can stil use methods, even if all functions and constants witin the math module have been imported.  

print(math.nan) # NAN = Not A Number. 

# You can also use logrithims with the math module. 

# For an example, we know that log(e) = 1.
math.log(math.e)

# Finally we have trigonometric functions. 

print(math.degrees(math.pi/2))

print(math.cos(90))

print(math.radians(180))


# The next module to look at is the random module. 

import random 

# The randint method takes two numerial arguments and outputs a random number in the range between them. 
print(random.randint(0,100))

# You can set a seed for your random numbers, essentially a specific instance of random integers. 
random.seed(101)

# If we set a specific seed, we will know what numbers will be produced by the random number generator. Like seeds in minecraft, it produces a specific map. 
# The seed doesn't specifically produce 74 or 24 for the first and second number, it just refers to a specific sequence of random numbers. 
print(random.randint(0,100)) # 74
print(random.randint(0,100)) # 24
print(random.randint(0,100)) # 69
print(random.randint(0,100)) # 45
print(random.randint(0,100)) # 59
print(random.randint(0,100)) # 6

# Another method is .choice, it chooses a random item from a list for example. 
my_list = list(range(0,20))

print(random.choice(my_list))
# This does not premanently affect your list, but just refers to it. 

# There is also the .choices method, that allows you to take a random sample from a list for example. 

# A sample with replacement meaning you can have duplicate items when randomly choosing your sample. 
print(random.choices(population = my_list, k = 10))

# You can also have sample selection without such replacements. 
print(random.sample(population = my_list, k = 10))

# You can also shuffle a list randomly, bear in mind that this will actually transform the list, so you won't to reassign it to anything.
# Don't forget about it though, you don't want to use a shuffled list by accident. 

random.shuffle(my_list) # You cannot print this, because it is a purely transformative function, there is no output. 

# You can also use the random module to output numbers in relation to a distribution. 

print(random.uniform(0,100)) # This will produce a random number between the range of 0 and 100, it is continous, meaning all floating point numbers are considered. 
# It is called uniform because every individual number, integer or obscure floating point has a uniform chance of being chosen. 

# We can also do the same, but for a normal/gauss distribution. 

print(random.gauss(mu = 0, sigma = 1)) # This picking a random number out a defined normal distribution, where mu is the mean and sigma is the standard deviation. 
# Bear in mind that once you have defined a seed, all particular instances random numbers will from the same sequence and therefore will be the same. 
# That's why we get the same value from the uniform and gauss distributions. 