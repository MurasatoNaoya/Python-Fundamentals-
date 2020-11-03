# Write a function that computes the volume of a sphere given its radius. Given that the volume of a sphere is given as 4/3(pi)(rad)^3. 
def sphere(rad):
    return (4/3)*(3.14)*(rad)**3 # Using estimated Pi. Also bear in mind that you have to mention '*' to signify multiplicaiton; even between brackets. 

# Check
print(sphere(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low). 
def range_checker(num,low,high):
    if num in range(low, high+1):
        return 'Yes, this number is within this range.'
    elif num > high:
        return 'This number is above the accepted range.'
    else:
        return 'This number is below the accepted range.'

print(range_checker(5,2,10)) # Test case for within the range. 
print(range_checker(12,2,10)) # Test case for above the range. 
print(range_checker(0.5,2,10)) # Test case for below the range. 

# If you only wanted a boolean output - 
def range_checker(num,low,high):
    if num in range(low, high+1):
        return True
    else:
        return False


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def ups_lows(mixed_string):
    
    upper_letter_counter = 0
    lower_letter_counter = 0
    
    for letter in mixed_string:
        if letter.isupper():
            upper_letter_counter += 1
        elif letter.islower():
            lower_letter_counter +=1 # You cannot just use an 'else' statement here, otherwise the program will count numbers and spaces too. 
        else:
            pass
    print('Number of upper letters -' +  str(upper_letter_counter))
    print('Number of lower letters - ' + str(lower_letter_counter))

print(ups_lows('Hello World'))

# Here is an alternativr method using dictionaries. 
def ups_lows2(other_string):
    
    d = {'upper' : 0, 'lower' :0} # It perhaps makes more sense to use dictionaries for this problem, because they are 

    for letter in other_string:
        if letter.isupper():
            d['upper'] +=1
        elif letter.islower():
            d['lower'] +=1
        else:
            pass
    print('No. of upper case letters : ', d['upper']) # When you want to input specific key values into a string, you use commas (,) and value indexing. 
    print('No. of lower case letters : ', d['lower'])

print(ups_lows2('Hello World'))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(one_list):
    empty_list = []
    for element in one_list:
        if element in empty_list:
            pass
        else:
            empty_list.append(element) # You have to use the .append() method, because in order to use +=, the data type on the right side has to be iterable; which an integer is not. 
    return empty_list                  # In any case, just bear in mind that on the right side of +=, needs to be an iterable data type. 

print(unique([1,2,2,5,6,6,7,8,8,8])) 
print(unique([1,1,1,1,2,2,3,3,3,3,4,5]))


# Write a Python function to multiply all the numbers in a list.
def multiply(num_list):
    total = 1
    for num in num_list:
        total *= num     # Much like +=, *= means multiply with the left side, and then become the new left side. 

    return total

print(multiply([1,2,3,-4]))


# Write a Python function that checks whether a passed in string is palindrome or not.
def palindrome_checker(a_string):
    if a_string.lower() == a_string.lower()[::-1]:
        return 'This is a palindrome!'
    else:
        return 'This is not a palindrome.'
print(palindrome_checker('Racecar'))
print(palindrome_checker('Hello'))


# Write a Python function to check whether a string is pangram or not. 
# In order to answer this question, we will have to import the string module to obtain the necessary methods to refer to the alphabet. 
# A module is a file of applicable Python functions, classes and variables. 

import string # This imports the string module. 

def panagram_checker(str1, alphabet=string.ascii_lowercase): # ascii_lowercase is an imported variable from the 'string' module, that is s list of the alphabet in lowercase. 
    alphaset = set(alphabet)
    str1 = str1.replace(' ','') # This is necessary in order to remove any spaces, that would add to the alphabet. 
    str1 = str1.lower() # There may be capitals in the inputted strings, you need to match the LOWERCASED alphabet. 
    str1 = set(str1) # It is important to use sets here, due to both sets not being in order, sets allows you to demonstrate equivalence, without both sets being in order. 
    return str1 == alphaset # Checking for SET EQUIVALENCE. 

print(panagram_checker("The quick brown fox jumps over the lazy dog"))

# Here is another perhaps fast way of going about the same problem - 
def panagram_checker(str1, alphabet = string.ascii_lowercase):
    print(set(str1.lower()).intersection(alphabet)) # Here you can see that the lowercased inputted string has an perfect intersection with alphabet. 
    return set(str1.lower()).intersection(alphabet) == set(alphabet) # The intersection method is also imported from the string module, it outputs similarities/intersections between two things. 
                                                                     # In this case, it's a means of removing any spaces within the inputted string, creating a list of only commmon characters. 
                                                                     # Bear in mind however, that the intersection() method can only be used on sets, you will get a 'no attribute' error otherwise.  

print(panagram_checker('The quick brown fox jumps over the lazy dog'))