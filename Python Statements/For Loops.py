# A 'for loop' is the execution of a piece of code, that iterates from a group of items. 
# The content of the object dicates what code is executed and the number of times it is executed. 
# For loops apply to any data type that can hold multiple items, like a list or dictionary for example. 
# Reading, for object_variable in list_name is confusing, just treat the for as an indictation that there will be iteration and examination of the entire datatype. 

my_list = [1,2,3,6,7]
for num in my_list: 
	print(num)


# The varibale 'num' represents the elements in this list. There is a ditinction between this a my_list. 
# The above code is saying - 'For every element in my list, print the elements.'

# You can of course have any type of code be executed iteratively. 

my_list = [1,2,3,6,7]
for num in my_list: 
	print('hello world')
# This code is saying - 'for every object in my list, print hello world'
# You can use control statments to make your for loop more specific. 
# In this case, iteration if noly used to print even numbers. 

my_list = [1,2,3,6,7]
for num in my_list: 
	# Checking for 	even numbers.
	if num % 2 ==0:
		print(num)

# Once again, you can add compexity to your loop with elif and else statments. 

my_list = [1,2,3,6,7]
for num in my_list: 
	# Checking for 	even numbers.
	if num % 2 ==0:
		print(num)
	else: 
		print(f'Odd Numbers: {num}')

# You can use fstrings to identify odd and even numbers in a for loop. By using the f'Odd/Even Numbers: {object_variable}'

# Indentation is very important regarding the outcome of of a for loop. 
# Here's a summation for loop demonstrating this (using previous variables like my_list) - 
# Imagine the code reader returning to the top of the loop, until all elements have been accounted for. 
# (We are using my_list and num from the previous part.)
# The significance of indentation in this case, is the fact that printing within the for loop will prin every individual loop for each individual element. Showing 1,3,6,12,19; and not just 19. 
my_list_summation = 0 
for num in my_list:
	my_list_summation = my_list_summation + num
	# Iterating through each element, right to left. 
	print(my_list_summation) 

# If the final print command is WITHIN the for loop, then each individual iteration will be shown. 
# However if it's outside of the for loop, only final post-iteration value will be shown. 

my_list_summation = 0 
for num in my_list:
	my_list_summation = my_list_summation + num
print(my_list_summation) 

# For loops can be used for many data type with multiple elements. 
# Strings are another example - 

my_string = 'hello world'
for letter in my_string: 
	print(letter)
# This code being a one-by-one iteration of the inital string. 
# You have to indent a command after a 'for', otherwise the program will not know what the purpose if it iterating is. 

# For strings you don't even need to assign anything.  
for letter in 'Hello world': 
	print(letter)

# This works becuase you are essentially saying a similar thing, 'For every 'letter' in 'Hello world'; print an element of 'Hello world''. 

# Often times, to make your code more readible you can use _ for your object variable if there is no relation to the object. 
for _ in 'Hello world': 
	print(_)

# For loops unsuprisingly work with tuples too. 
tups = (1,2,3) 
for num in tups:
	print(num)		

# For data types like lists and tuples, you can 'unpack' them. 
tups_list = [(1,2),(3,4),(5,6),(7,8)]
# Here you have several tuples within a list. 
# Such a thing can only be done with a list or tuple, due to the abilty for them to contain other data types. 

# We can do the standard thing and print all of the elements within tups_list. 

for elements in tups_list:
	print(elements)

# More importantly you can isolate individual items within the several tuples. 
# When you actually isolate indivudal items, specifiying what indiidual thing you want to iterate through actually matter. You cannot put _. 

for (a,b) in tups_list:
	print(a)
	print(b)
# Another example - 
# You must stick to the alphabetical a,b,c order. 
another_tups_list = [(1,2,3),(4,5,6),(7,8,9)]
for (a,b,c) in another_tups_list:
	print(a)

# Tuple unpacking is using the general form of each tuple as the element varibale, in order to isolate individual items wihin each tuple. 

# Finally, for loops can be used to iterate through a dictionary. 

dictionary = {'ka':1, 'kb':2, 'kc':3}

# Because a dictionary hold key value pairs as opposed to just the value, you cannot just write 'in dictionary:
# Otherwise, by default you would iterate throught the KEYS rather than the values. 

for items in dictionary:
	print(items)

# To fix this and return KEY VALUE PAIRS instead of keys, you have to specifiy this; by using 'in dictionary.items()'
for items in dictionary.items():
	print(items)

# There is a better way of going about this however, via the 'tuple unpacking method' from before. 
# You use the alphabetical system for tuples and 'key,value' system for dictionaries. 
# This time you are not giving the general form of a,b,c or a,b; but rather - key,value. 
for key,value in dictionary.items():
	print(value) 
