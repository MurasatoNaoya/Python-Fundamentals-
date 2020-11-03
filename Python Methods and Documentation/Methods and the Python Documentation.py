# Methods are specific functions that apply directly to objects. 
# Thus, taking the form of .method. 
#Also don't forget, that you must include double brackets after a method. 
# We have gone over method before, but I will quickly recap the methods we have encountered so far - 



# You can also use the 'help()' function to actually check what the method will do.
# The output is called 'docstrings'.

# The .upper() method makes the entire variable upper case. 
classic_statement = 'Hello World'
print(classic_statement.upper())

# The .lower() method makes the entire variabe lower case. 
print(classic_statement.lower())

# The append() method takes the first element of a variable and adds it to the back of another variable. 
# You can only append to a list, and append FROM a list. 
empty_list = []
append_list = [1,2,3,4,5]
for _ in append_list:
	empty_list.append(_)
print(empty_list)

# The .split() method splits a strong at a specific point that you can define.
# If you don't define anything, it will just split eadh element into a list. 
print(classic_statement.split())
print(classic_statement.split('e'))


		

mylist = [1,2,3,4]
help(mylist.insert)	

# Somewhat unrelated, is Python Documentation. In a sense these are the patch notes and descripitions of base or additional features in Python. 
# At the time of writing, documentation for Python 3.8.5 can be found with this link - https://docs.python.org/3/ 
# The 'Tutorial' section is where the fundamental ideas and principles of Python are. 