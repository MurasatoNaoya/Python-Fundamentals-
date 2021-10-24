 
# This would be a normal function that instead commits the list of results to memory and prints the values.  
 
def square_iterator_return_list_test(n):
    empty_squared_list = []

    for num in range(n+1): 
        empty_squared_list.append(num**2)

    return empty_squared_list


print(square_iterator_return_list_test(10))

# This is what you'd do if you wanted each individual squared number to be printed - 

def square_iterator_return_individual_print_test(n): 
    for num in range(n+1):
        print(num**2)

    
print(square_iterator_return_individual_print_test(10))




# Here is another example, an incorrect one however. 

def incorrect_square_function(n):
    for num in range(n+1):
        return num**2 


print(incorrect_square_function(10))


# This is outputting 0, why? 
# The code ends at the first value due to the return function, so the program does not get the chance to interate through the rest of the integers. 
# That's why the yield keyword is useful, it returns the value, but allows the program to iterate through whatever, in this case a list of numbers up to and including 'n'. 
# In this case, the return fucntion can only be used for the first function, where an output is only reported once, in the form of a long, single list. 

 


# Instead of using iteration with for loops, implementing generators can often be a lot easier; but more importantly, more memory effiient. 
# Generator function do not commit final results to memory, instead, a generator obhect is created, and for every iteration cycle, a suitable value is created in real time, as opposed to being recollected.  

def squared_gen(n):
     
    for num in range(n+1):
        yield num**2      # In this context, what the yield keyword is saying here is - "Produce a generator object that squares all inputs;  the inputs accounting for all numbers in the range of 0 to 11. "
                          # Please, bear in mind, these are not the values or items you want, this is the generator object itself. 

for gen_nums in squared_gen(10):    # This final for loop is necessary to print the GENERATED ITEMS as opposed to the GENERATOR OBJECT itself. 
    print(gen_nums)
 

print(squared_gen(10)) # If you print this, you'll get back the generator object and not the items you want, because you didn't iterate through the intangible list that is the generator. 


# The next thing we should talk about, are the relevant methods associated with generators, like next() and iter() keyword. 

# Firstly, the next() function allows us to see what the next item in out generator object will be. 
# For the sake of not typing a large name out each, let's just redefine an instance of our generator function to the letter 'z'. 

z = squared_gen(10)

print(next(z))
print(next(z))
print(next(z))

 # This is useful when you want to identify a singular item within a specific generator object you've created. 
 # Eventually, you would get a StopIteration error, meaning you have gone through all available items and that there are no more you can go through. 
 # This next() function is automatically run within a forloop, but is automatically stopped once the forloop has recognise that there are not more items to iterate through. 


# The next function and keyword we can focus on, is the iter() keyword 

# In python, there are objects that you can iterate through; meaning they are iterable. For an example - lists, tuples, dictionaries and sets. 
# However, even if these objects are iterable, it does not mean that these objects are iterators - you cannot apply the next() function to them. 
# Specifically, in this case, lists and suhc contain multiple items, but an individual string does not, therefore it is not an interator. 
# However, the iter() function, allows you to apply functions, like next() to object that previously would not be an iterator. 

# For an example - 

z = 'Hello World' # You would recieve an error if you tried to apply the next() method to this string, as it is not an iterator. 

# (Incorrect) print(iter(z))

            # TypeError: z is not an iterator object 



z_iter = iter(z)

print(next(z_iter))     # Now that we have changed 'z' into an iterator, we are able to apply functions like next(). 
print(next(z_iter))
print(next(z_iter))




# Python generators homework task - 


# Q1: Create a generator that squares the numbers up to a certain number 'n'. 
# We have just done this, but just for the sake of the questions and the homework, why not do it again.. 

def gensquares (n): 

    for num in range(n+1):
        yield num**2 


for item in gensquares(5):
    print(item) 

# Question 1 is correct! 


# Q2 : Create a generator that yields "n" random numbers between a low and high number (that are inputs).

import random


def rand_num(low,high,n):
    
    for num in range(n+1):
        yield random.randint(low,high) # This is a useful method from python's random module, that produces a random number. Nice. 



for item in rand_num(1,100,10):
   print(item)


# With a bit of help, question 2 is also correct!! 


# Q3: Use the iter() function to convert the string below into an iterator:

s = 'hello' 

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter)) # The fact that this runs smoothly without a type error, makes it clear that the iter() function has been applied and that 's' is not an iterator. 



# Q4: The preference of using generators with a yield statment over a normal function with a return statment (or other forloop memory saved equivalent) is how memoery efficient generators are. 

# When dealing with smaller data objects, let's say lists of 10 items, it's not such a big deal to be memory efficient, because the memory efficiency you gain from not committing 10 items to memory is insignificant. 
# However, when you're with objetcs with hundreds, even thousands of items, then standard return functions begin to be extremely inefficient. 

# In summary, use generators when dealing with a large number of items, due to generators being more efficient, due to not commiting items to memory; instead just generating the numbers on the spot. 
# Maybe you want the large list for another purpose. That's fine. 
# But if you just want to iterate through it and you have no other purpose for the list, then you would want to use a generator. 



# Extention Q5: 

# 























