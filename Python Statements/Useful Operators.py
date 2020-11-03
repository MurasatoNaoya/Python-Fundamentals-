# An operator, is a specific type of function, often mathematical in nature. 
# There are some operators specifyecific to Python, that can make your life a lot easier. 

# Like the range operator for example, which, as you would expect, provides a range of values of focus.
# You can iterate through them, simply print under parameters or  whatever.

# Here is an example of using a for loop to iterate through a range of values.  
for _ in range(10):
	print(_)
# What this is essentially saying is - 'print every element within a range of 10'. 
# Bear in mind that for programming in general, the first integer will be '0', meaning in the range of 10; the final number will be 9. 

# Using this same for loop, you can iterate elements within another more specific range. 
# The structure of the 'range' functio can be (start,stop,step-size)

for _ in range(3,10):
	print(_)

# What this says is - 'print every element within the range of 3 up to, but not including 10'.
# Much like slicing, you can specify a range, but also a in the size of intervals. 
for _ in range(3,10,2):
	print(_)

# Another important concept is the idea of 'generators'. The range operator is in itself a generator. 
# A function that will create or generate information, without saving it direct memory, AKA - assigning a variable. 
# creating a group of values, but by itself it is just that; only a group of information. 
range(3,10,2)

# Generators like 'range' can then be cast to other things, like a list for example. 
list(range(3,10,2))
print(list(range(3,10,2)))

# Another useful operator function is the 'enumerate' operator function. 
# May times it is useful to know how may times you have iterated through a for loop, what index you have arrived at and what the value actually is. 
# You could use fstirngs or .format. 

# This example using fstrings.
index_count = 0
for _ in 'abcde':
	print(f'We are currently at index position {index_count} at letter {_}')
	index_count += 1

# This is an example of the .format method. 
index_count = 0
for _ in 'abcde':
	print('We are currently at index position {} at letter {}'.format(index_count,_))
	index_count += 1

# However, instead of writing all of this, you can simplu use the enumerate function. 
# You should recieve tuple pairs, assigning values to different indexes. 
for _ in enumerate('abcde'):
	print(_)

# As we have already described, you can use tuple unpacking with for loops to isloate the indexes and values. 
for (index, value) in enumerate('abcde'):
	print(index)
	print(value)
# To concluude, the 'enumerate' operator fucntion uses any iterative loop to present indexes and their associated element values. 

# Next is the 'zip' operator fucntion, used to 'zip' together two lists
# Remember, you are not joining the end of one list and the beginning of another, you are forming a list of tuples, by pairing values of the same index.   
# For example, you could join to lists together by assigning the final list to a string. 
# The list function creates a list out of the information inside of it. 

the_first_list= [1,2,3,4,5]
the_second_list = [6,7,8,9,10] 
print(zip(the_first_list, the_second_list))
 
# Note that in Python 3, you cannot get a zipped list to return just with the print function. (You apparently could in Python 2)
# Instead you have to iterate thorugh, or cast the zipped list to a list itself. 
# Otherwise you will just get a data storage position of the zip string on your computer. 
the_first_list= [1,2,3,4,5]
the_second_list = [6,7,8,9,10] 
print(list(zip(the_first_list, the_second_list)))

# The other and perhaps better alternative, is to iterate using the zip operator function. 
the_first_list= [1,2,3,4,5]
the_second_list = [6,7,8,9,10] 
for _ in zip(the_first_list, the_second_list):
	print(_)
# Essentially what this has said is - 'For every index in each of the two lists, print a tuple of the index in question, with values associated with each index form each list.'

# This also emphasizes the importance of tuple unpacking in iterative loops. 
# So many operator fucntion will return in the form of tuples, therefore is important to be able to isolate vlaue in the tuple with tuple unpacking. 

the_first_list= [1,2,3,4,5]
the_second_list = [6,7,8,9,10] 
for (index,value) in zip(the_first_list, the_second_list):
	print(index)
	print(value)

# You also don't have to keep assigning the list variables, but I am just doing this to make it less confusing. 

# If the lists are unbalanced in the number of elements, then the zip function will only include the lowest number of elements, to ensure every list can be joined together. 	
the_first_list = [1,2,3]
the_second_list = [7,8,9,10,11,12,13,14,15,16]
the_third_list = [17,18,19,20]
for _ in zip(the_first_list, the_second_list, the_third_list):
	print(_)

# You can also isolate lists within a iterative loop, in this case, with a zip operator function. 
# Because you are using several lists, you can specify which one you want to isolate by being specific with your items. 

the_first_list = [1,2,3]
the_second_list = [7,8,9,10,11,12,13,14,15,16]
the_third_list = [17,18,19,20]
for a,b,c in zip(the_first_list, the_second_list, the_third_list):
	print(b)
# But once again, due to the lowest elemt within one of the lists being 3, the zip function makes it so the output of 'b' is only 3 elements of the 2nd list. 

# Another operator, is the 'in' operator function. 
# We have already seen 'in', in our for loops, describing the presence of something within something else. 
# A clear example for this can be seen within True and False statements. 

T_and_F = [1,2,3,4,5]

print('x' in T_and_F)
print(2 in T_and_F)

# 'in' also works fine within a string
T_and_F_string = ' Hello World'
print('l' in T_and_F_string)

# As well as dictionaries. 
T_and_F_dictionary = {'key1':1, 'key2':2}
print('key1' in T_and_F_dictionary) 
# You can also specify if what you're looking for is a value or a key. 
# You can do this by using the dictionary specific methods, .values and .keys. 
# These methods take the values or keys and picks them from the dictionary; for reference. 

print(1 in T_and_F_dictionary.values())
print('key1' in T_and_F_dictionary.keys())

# Yet other more mathematical operator fucntion is the 'min' and 'max' functions. 
# They simply retrieve the minimun and maximum value from a list of numbers. 
num_list = [1,2,3]
print(min(num_list))
print(max(num_list))
# You cannot use the min and max operators for a random list of numbers however, you must define your list first and then you can use the two operators. 

# All of the functions we have dealt with so fat, have been built in functions within Python. 
# To have access to a wider range of fucntions, we have to use the random library within Python.hh
# One such function is the 'shuffle' function. 
# The shuffe fuction randomly shuffles elements within a list into a random order. 

from random import shuffle 
shuffle_list = [1,2,3,4,5,6,7,8,9,10]
print(shuffle(shuffle_list))
# Note that this doesn't work, as by shuffling you are changing what you have assigned. Therefore, after shuffling, you just return what your original list was. 
# A function that doesn't return anything and changes the ASSIGNED value, is called an in-place function. 
# You also cannot 'save' or assign the output of in-place functions, due to there being no output. 
print(shuffle_list)

# Another operator fucntion is the 'randint', as you would think, this function selects a random integer within a list. 
from random import randint
print(randint(1,100))
# 'randint' does give an output (is not an in-place function) and therefore can be assigned and saved. 
saved_number = randint(1,100)

# Yes, yet another function is the 'input' function. 
# In theory, the string inside of the input function will be proposed, but then an input wll be required. 
# You will mostly save the answer as a result, so that it can be used later on. 
input('Enter a number here')
consumer_name = input('What is your name?')
# The consumer would be posed the question and their name would be saved for later use. 
# Most importantly, the input given to the input funciton, will always be processed as a string. Even if you proivide an integer to begin with. 