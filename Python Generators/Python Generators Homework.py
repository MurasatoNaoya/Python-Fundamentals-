# Problem 1, Create a generator that generates the squares of numbers up to a certain limit 'n'. 

def square_generator(n):
    for num in range(n):
        yield (num)**2


# The yielded values can be printing using a for loop to show the for loop works - 
for _ in square_generator(5):
    print(_)



# Problem 2, Create a generator that yields 'n' random numbers between a low and a high number (that are inputs). 

import random 

def random_number_generator(lower,upper,n): # It is important to note that the parameter n represents the number of outputs you want; in this case the number of random number outputs you want. 
    for num in range(n):                    # The range keyword indicates the number of cycles, when a for loop is involved. 
        yield random.randint(lower,upper)

for _ in random_number_generator(1,20,10):
    print(_)



# Problem 3, use the iter() function to covert the string 'hello' into a iterator. 

s = 'hello'

s_is_now_an_iterator = iter(s)

print(next(s_is_now_an_iterator))
print(next(s_is_now_an_iterator))
print(next(s_is_now_an_iterator))
print(next(s_is_now_an_iterator))
print(next(s_is_now_an_iterator))

# The next keyword is shown to return without an iterable error, therefore the string 'hello' is shown to now be an iterable. 



# Problem 4, explain a use case of a generator function, as opposed to a normal function to iterate through a list of an example and return values - 

# The benefit of generators, is that you can declare a function that iterates through objects without commiting the results to memeory, but rather, outputing a result by account for the stepsize and the previous value. 
# This is particularly useful when dealing with very large lists, where having all the information committed to memory would be very computationally inefficient.  



# Problem 5, explain what 'gencomp' does in the below code - 

my_list = [1,2,3,4,5]   # Individual parts of larger objects like lists are called 'items'. 

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)


# The generator consists of a for loop in generator comprehension form. If a item in the list is greater than 3, it will yield the value. 
# The second for loop is in conventional form, is there for the sole purpose of printing the yielded values, in this case being 4 and 5. 
# The format of generator is the same as list comprehension, but rather than using square brackets, you use parenthesis and it will yield values as opposed to creating a list.      
# Generator comprehension adds shorter syntax, as opposed to writing a full yield for loop. 