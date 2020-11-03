
# 1.) Use for, .split(), and if to create a Statement that will print out words that start with 's':
# It is better to use the .lower() function for your criteria, to ensure that you don't only count lower case 's's, but aldo upper case ones. 
# You could also use the 'or' statement, to specify 's' or 'S'. 

st = 'Sam, print all of the words that start with s' 

for _ in st.split():
	if _[0].lower() == 's':
		print(_)	
# You have to apply the .split function otherwise the for loop will consider the whole string as on element. 
# This will be standard procdure when you want to iterate through individual elements of a long string. 

# 2.) Use range() to print all the even numbers from 0 to 10.

for _ in range(0,11):
	if _ % 2==0:
		print(_) 
# Each individual number can be iterated through using the range function and therefore can be printed based on divisibility. 

# 3.) Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# This can be done in two ways, via one line list comprehension or the for loop method. 
numbers_divisible_by_three = [ _ for _ in range(1,51) if _ % 3==0 ] 
print(numbers_divisible_by_three)

numbers_divisible_by_three_2 = []
for _ in range (1,51):
	if _ % 3==0:
		numbers_divisible_by_three_2.append(_)
print(numbers_divisible_by_three_2)
		
# 4.) Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for _ in st.split():
	if len(_)% 2==0:
		print(_ + '- This word is even!')
# Remember if you want to refer to the length of something, then you have to use the len fucntion THEN use brackets to specify what you're unit you are checking. 
# You can also use the '+' sign to add to lists too, if you have trouble remembering, refer back to the lists page. 

# 5.) Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number. 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for _ in range(1,101):
	if _ % 3==0 and _ % 5==0:
		print('FizzBuzz')
	elif _ % 5==0:
		print('Buzz')
	elif _ % 3==0:
		print('Fizz')
	else: 
		print(_)
# Always put the most criteria in your first 'if' statement, the code will allocate a Fizz, before checking for %3 and %5 for FizzBuzz. 
# Don't forget that the 'and' statment can be used to chain more complex criteria. 

# 6.) Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

# The first method is to use a for loop to append the first index onto an empty list. 
empty_list = []
for _ in st.split():
	empty_list.append(_[0])
print(empty_list)

# The second method is to use the one line formula, that specifically deals with list comprehension. 
first_ltr_list = [_[0] for _ in st.split()]
print(first_ltr_list)

# There is no other real way, you can find the first index individually, but the only way to cast this to a list is to use the append method in the first place. 
for _ in st.split():
	print(_[0])

# Also remember the syntax for indxes, they have to go inside of the bracket of the fucntion. 
# Makes sense, as you are declaring the first index to to under go the funciton, not vice-versa. 
