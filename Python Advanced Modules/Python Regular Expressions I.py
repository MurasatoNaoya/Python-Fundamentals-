
# First we need a string to scan through and match things to. 
text = "The agent's phone number is 020-823-1234. Call back!"


# We can create a simple script to produce a booleon output if the string 'phone' is present. 
print('phone' in text) 

# But we an instead use a regular expression to serach for the word, but have a lot more information given to us. 

import re # First we import the regular expressions module. 

pattern = 'phone'

print(re.search(pattern, text)) # Then we can look for the word that has been assigned to a variable using the .search method. 

# This match object not just if there is a match with the variable, in this case being 'phone', but it will also tell us its index position. 
# In this case, it starts at index 12 and ends at index 17. 

pattern = 'NOT IN TEXT'

print(re.search(pattern, text))
# If there is no match at all, 'None' will be returned.


# We can then reassign this output so we can apply other methods that give us more information. 

matched = re.search(pattern, text)

print(matched.span()) # You can use the .span() method to get the index range specifically, remember, you have to call the method with parentheses (). 
# We can do this same thing with another variable, that has a value not present in the text. 
# If you want to call on an attribute, you don't have to use parentheses, otherwise, you have to. 

print(matched.start()) # There is also the .start() method that tells you when the first index of, in this case, 'phone' appears. 

print(matched.end()) # And vice versa with the .end() method. 

print(matched.group()) # The group method provides the actual text values of the matches, as you will see, essentially the same as the .findall() method. fidn

# This matching script however, only accounts for the first instance of what you're looking for. 
text = 'This phone going once, this phone going twice.'

matched = re.search(pattern, text) # You have to redefine matched due to you redefining text. 

print(matched) # The outout only accounts for the index positions of 5 to 10, the first instance of 'phone', ignoring the second. 

# If you wanted to account for all instances, you can use the .finall() method. 

matched = re.findall(pattern, text)
print(matched)
# You will only get back a list containing the instances of the values you are looking for. 
# You can use the len function to illustrate the number of matches in the entire text. 
print(len(matched))

# However, this in itself is not very useful, as it doesn't tell us anything about the index positions of these cases. 
# Instead, you can iterate through the text to find each individual case, using the .finditer() method with a for loop. 
# The .finditer() method is a combination of .search() that produces a match object and the elements of .findall() as it iterates through the text.


print(re.finditer(pattern, text))

for _ in re.finditer(pattern, text):
    print(_) # You can further apply methods like .span() etc to get more specifc outputs.  

# This works because re.finditer is basically an output of match objects that do not overlap, and the for loop just prints each instance of that each loop. 



