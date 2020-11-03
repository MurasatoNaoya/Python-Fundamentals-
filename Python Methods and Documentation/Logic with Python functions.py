# Function can be used to quickly solve or provide insights into logic problems. 
# If you recall back to the 'mod' operator, you will find that we can create a function for divisibility or odds and even - 

def odd_check(num):
	return num % 2!=0 # remember that == is equivalent to and != is not equivalent to. So if you were checking for evens, you would put ==. 

print(odd_check(20))

# Using a function to check the 'evenness' of a single number is fine, but you can also incorporate you've learnt already to do the same for a list of numbers. 

list_of_numbers = [235,95,4235,765,2865,47,77]

def evenness_check(num):
	for _ in list_of_numbers:
		if _ % 2==0:
			return True
		else:
			return False
print(evenness_check(list_of_numbers))

# This function above however, is incorrect. As it demonstrates a key misunderstanding of what the return function does. 
# The return breaks out of the function, not accounting for the code beneath it. 
# Therefore, the else statement is essentailly ignored. 

# The return for false must be indented in such a way that it is in line with the for loop. 
# Essentially saying - 'Hey, if you don't come across any even numbers after the iteration and return 'True', then go ahead and return 'False'; because this means there was no even number. After iteration.  
# Let's change the list to all odd numbers to suit this. 
# Bear in mind that due to the nature of return, you will not get a boolean for each number, but rather only one after your condition has been met. 
# Making it a - 'I will return this once I find at least one example of your parameter'kind of process.

list_of_numbers = [235,95,4235,765,2865,47,77]

def evenness_check(num):
	for _ in list_of_numbers:
		if _ % 2==0:
			return True
		# You don't need an else statement, because if 'True' is not returned, nothing will show up to the console; allowing 'False' to be returned. 
		return False # Remeber the key indentation. 
print(evenness_check(list_of_numbers))

# The key take away - returns cannot be indented together, pay attention to the logic of the statements you write. 
# Here is a program using a list of numbers and providing a list of booleans according to their 'evenness'. 
# You also need the 'num_list' argument in order to input a list of numbers in the first place. 

boolean_outcome_list = []

def evenness_check(num_list):
	for _ in num_list:
		if _ % 2==0:
			boolean_outcome_list.append(True)
		
		else:
			boolean_outcome_list.append(False)
	return boolean_outcome_list # You need this return to acually have any output for the boolean_outcome_list. 

print(evenness_check(list_of_numbers))

 # Bear in mind that this could also be a list of numbers like [1,2,3,4,5].
# Also be careful using the same function for different strings, if you iterate with another string, the information of the previous task will be left over.