# Print Formatting ( String Interpolation ) - 

# .format method - 

print('This is a string {}'.format('okay.')) # The curly braces are placeholders for the variables that you want to input.

# Unless specified otherwise, the string will be formatted in the order you put them in your .format function. 
print('This is a {}, not a {}; or a {}'.format('string', 'dictionary', 'tuple'))

#A solution to this, is using indexing. 
print(" The world is {2}, {0} and {1}".format("lean", "mean.", "cruel"))  # The variable(s) that you input, can also be in a list too. 
#The assigning of objects to letters is also possible. 
print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick')) # Using letters is easier than index position, just do to it being hard to count the spaces. 

# Float Formatting - 

result =  100/777
print('The result was {r}'.format(r = result))

		# Value:Width:Precision. (Mainly dealing with 'Precision'), as the width value only adds white space.  

print('The result was {r:1.3}'.format(r = result)) # Variable inserted to three decimal places, with a width of one. 	

		#fstrings method, alternative to the .format method. 	

name = 'Andrew'
age = 18
weight = 100.5
print(f'Hello my name is {name}') # This works with multiple variables (strings, integers, floats.)

print(f'{name} is {age} years old; and can deadlift {weight} kilograms')  