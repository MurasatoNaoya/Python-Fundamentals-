mystring = 'Dichotomy' 
print(mystring) 
print(mystring[0])

# This is known as indexing for strings, using the square brackets to pick out a value within the string; the first character being zero. 
# You can also use negative numbers within the square brackets for inversing, this just reverses the order of selected values. This is called reverse indexing. 

print(mystring[-1]) 

# Slicing is similar to indexing, but instead of retrieving just one value, you are retrieving a whole sub-section of the string. 

print(mystring[0:3])

# The above code means - Retrieve all values from point 0 UP UNTL, BUT NOT INCLUDING value 3.  
# Much like indexing, negative values can be used also. 

print(mystring[0:-3])

# For negative values, the very last value is -1, as -0 doesn't make any sense. 
# The final parameter is step size, which uses 2 semi-colons. The number at the end of the second semi-colon is what determines the step size. 

print(mystring[::2]) # This will just present the string, but in intervals of 2 from the beginning. 

# A nice way of thinking about indexing, slicing and step size is; START,  UP TO, BUT NOT INCLUDING & STEP SIZE. 
print(mystring[1:6:2])

# The final point, which is Python specific, is you can use a negative number for step size (e.g -1 and it will reverse your string).
# As ::1 represents the string itself; forward intervals of one step; -1 represents the reverse of the string; or the backwards movement of one step. 

print(mystring[::-1]) 
print(mystring[::-2])

# INDEXING CALLS OF A SINGLE INDEX POSITION. 
# SLICING RETRIEVES PARTS OF AN OBJECT, IN RELATION TO INDEX POSITION. 