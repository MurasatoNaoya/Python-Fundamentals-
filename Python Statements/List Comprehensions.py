# There will be instances where you want to seperate each individual element within a string into a list. 
# This can be easily accomplished by using the knowledge we have acquired already - (for loops and the .append method)
# A quick reminder, the .append method adds the first element of something to the beginning of something. 
# Note that it does not copy, but it SUBTRACTS and ADDS. 

string_to_be_split = 'Hello'
empty_list = []
for _ in string_to_be_split:
	empty_list.append(_)
print(empty_list)

# Bear in mind that if you return 'string_to_be_split', you get nothing.
# All of the elements within the string have been appended to the empty list, due to the for loop iterating for every element. 

# An alternative to using the for loop method, is to to use a one string comprehension method; unique to Python. 
# This is leads to more streamlined and efficient code. 
# As of now, there doesn't seem to be any logic I can understand in the syntax, but just remember this as a flattened out for loop; in a sense. 

empty_list = [_ for _ in string_to_be_split]
print(empty_list)

# You don't even need to assign any of the strings you are using. 
empty_list = [_ for _ in 'Hello there']
print(empty_list)

# List comprehension can be paired with other useful operator functions to create more useful lists. 
empty_list = [_ for _ in range(1,21)]
print(empty_list)

# Much like the for loop method, you can apply mathematical operations to the .append function to adjust your list. Just make sure you are dealing with numbers.. 
int_list = [1,2,3,4,5]
empty_int_list = []
for _ in int_list:
	empty_int_list.append(_**3)
print(empty_int_list)
# Remember, you are appending the list you want to add to, as the for loop iterates through the elements of the 'int_list' and appends the first or next elements to the 'empty_int_list'. 
# This can be represented in the one line list comprehension format, by simply applying the numerical operator, in this case power, to the first item holder; in this case '_'. 

# To add even further complexity to your generated list, you can add filtering criteria, through the use of if, else and elif statements. 
# However in for the one-line list comprehension alternative, you need you need to do something different.
# There also doees't seem to be a way to incorporate an 'elif' statement into the one line method. 
int_list = [1,2,3,4,5]
third_int_list = []
for _ in int_list:
	if _ % 2==0:
		third_int_list.append(_*2)
	elif _ % 3==0:
		third_int_list.append(_**3)
	else: 
		third_int_list.append(_*4)

print(third_int_list)
# You cannot use 'elif' statements in single line list comprehension. 
# The alternative is to use several if statements, apired with else statements; this essentially having the same effect. 
# This emphasizes the idea that 'elif' is just another 'if'. 
# Also bear in mind that due to the nature of the 'else' statment, it must be the last of the 3 statements. 

# Here is the more compact 'List Comprehension' version, using if, else and essentially elif statements. 
# This syntax where the if and then else staments are stated first, just has to be remembered. 
second_empty_list = [_*2 if _ % 2==0 else _*4 if _ % 3==0 else _*4 for _ in int_list]
print(second_empty_list)

# If you just want to put a single 'if' statement however, the if stament goes at the end instead. 

second_empty_list = [_ for _ in int_list if _ % 2==0]
print(second_empty_list)

# Although the single line list comprehension is more compact, the for loop alternative is far more readable; bear this in mind for the long term readability of projects. 

# Finally, nested lists can be used in list comprehensions also.
# The idea of a loop within a loop may be confusing, but it allows you to iterate through every elements of the two variables from each list. 
# The easier way to understand it, is to try and follow how the compiler would process the code. 
# I put 'print' inside of the nested loop to make how the program was being processed clearer. 

for i in range(0,4):
	for j in range(0,4):
		print(i,j)
# The first number within the first for loop range is picked (i), but then the program runs to the second for loop; for more iteration. 
# The second loop then iterates for every integer within the range and continues to do so for every available integer. (As there is not a third loop.)
# The code print the result each time, then when there are no more integers to be iterated and printed in the second loop, it return to the top loop. 
# This process continues until there are no more available integers in the first for loop. 

