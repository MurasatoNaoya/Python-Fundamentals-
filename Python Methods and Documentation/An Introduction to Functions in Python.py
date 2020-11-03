
# You have to make a clear distinction about what functions are in not only Python, but programming languages as a whole. 
# The definition of a function is - a block organised, reusable that is used to perform a related action. 
# There are in-built functions, what we have dealt with so far. Like print(), len(), type(); etc. 
# But there are also user defined functions. 
# It is the user created functions that add significant complexity and possibility. Allowing you to reuse self-defined functions; instead of typing out the whole process again using in-built functions. 

# To create user definied funvtions, you must impliment the def() keyword. 
# User defined functions need a very specific syntax and indentation - def name_of_function():
# To make your code readble, you should be using 'snake casing', essentially using underscores (_) to represent spaces in the function name you are defining. 
# The parenthesis you put your arugment or parameters of the fucntion, essentially when you are inputing into the function. 

# If I where in the Jupyter Notebook I'd just call it, but I am in Sublime Text so I have to print to call it. 
# Remember that you need to define your argument, in this case we define our argument as 'name', so program could recoginse it later. 

# It is situation like these where you would just Docstrings as opposed to simple commenting. 
# Docstrings document a process and how something works, while comments are more general helping hands. 

# Here's an example for defining a function using 'print' - 


def printing_function():
	print('Hello there')	
print(printing_function())
# The reason why you get 'Hello there' and then None, is beacause you are calling the printing_function and then checking for a returned value. 
# Printing should only be used to show returned values, for they can not be returned themselves. Therefore this code is a fake way of producing 'Hello there' through a function. 
# It seems like you have to call the fucntion, to even produce anything using print.
# A way to remedy this is my returning the 'Hello there' so you actually have a return. 
# Printing something is not equivalent to a function returning something, it is just an action. Print just shows what is going on, not a returned value. 

def printing_function():
	return('Hello there')
print(printing_function())

# For this reason, when it comes to user-defined functions, it is very rare that we'll use 'print(); it will almost always be 'return()'

# You an also add extra complexity to the function, by including agruments and parameters.

def printing_function(name):
	return('Hello! My name is' + name)
	''' The function assigns 'name' as an argument, then assings the input within return to the assigned variable. '''

introduction = printing_function(' Andrew')
print(introduction)

# Here is another example using numbers and two agruments - 
def addition_function(num1,num2):
	return(num1 + num2)

added_numbers = addition_function(1,2)
print(added_numbers)

# Remember, return() allows something to be called, it creates an output, not to the console, but a real return. 
# Print() is only used to show the real return, not create one. It simply prints something, it doesn't count as a return. 

# You do have to include an argument within he parenthesis if you have a parameter in your code, otherwise you will get an error.
# What you can do instead however, is have a default value. Meaning your program will default to that inputted agrument, if there is not one specified. 
# You set a default argyment by using '=' next to it. 

def consumer_function(name=' dear customer!'):
	return('Hello' + name)

print(consumer_function()) # You would need to put name in the parenthesis, otherwise it would lead to the default value. 

# The print function doesn't directly allow to you save the output of your user-defined function. 
# Return() also allows you to assign your outout to a new variable. 
# Here is an example showing how vriable assignment only works with the return equivalent and not the print. 

def printing_result(a,b):
	print(a*b)

def additon_result(a,b):
	return a*b

print_result = printing_result(1,2)
add_result = additon_result(1,2)

print(print_result)
print(add_result)
print(type(print_result)) # The type is 'NoneType' as there is no returned value. 
print(type(add_result)) # The correct return is 3, which makes sense as the type for the return is 'int'. 

# The final thing to keep into account for function in Python, is the fact that Python is dynamically type; but also the implications of that. 
# In statically typed languages, you would need to first define the data type of the argument. 

def addition_function(num1,num2):
	return(num1 + num2)
print(addition_function(1,2)) # You are using integers here, so the program should work as expectd and produce an output of 3. 
# However, you get different results than expected and even bugs when you involve other data types. 

print(addition_function('1','2')) # This leading to concatination, instead of the intended integer additon.  
# You can't however, involve two multiple data types in one argument. 
# You won't accidentally using a string for numbers, but some output in your program my produce numbers as strings, so when connected such bugs may arise. 



