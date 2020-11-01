# Strings are immutable, meaning you cannot use item assignment on them. 
# e.g this - name = ' Sam '
# name[0] = 'P' 
# This would return an error, instead you can uuse string contatenation. Concatenation is simply the process of adding strings together. 

last_letters = 'am'
name = 'P' +last_letters
print(name)
# This way you can get the name 'Pam', without item assignment. 

# You can also use the * sign, to conduct multiple string contatenations. 
letter = 'z' 
print(letter*10) 

# When using concatenation, you have to be careful about what data types you use. 
print(2+3) 
# This is equal to 5, but what happens when you use strings instead? 
print('2'+'3')
# Instead of using arithmatic, the code conducts concatenation, because the numbers 2 and 3 are strings. 

# You can apply methods and functions to strings. 
x = ' Hello World '
print(x.upper()) # Upper cases all items in the string.

print(x.lower()) # Lower cases all items in the string. 

print(x.split())

# The standard split method will just split, depending on how many spaces there are, creating a list. 
# You can however, input a specific letter, to make the string split at a certain point. 
# The split method always creates a list, as an output from splitting. 

print(x.split('o'))
print(x.split('a'))


