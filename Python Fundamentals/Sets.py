# Sets are unordered collections of UNIQUE elements. 
# Meaning there can only be one representative of the same object. 
# E.g, you can't have the number '2' there more than one time. 
my_set = set()

# If you want to add a variable to your set you can use the add method. 
my_set.add(1) 
print(my_set)
my_set.add(2)
print(my_set)
# If you used to add method to add either 1 or 2, you would get an error. 
# Because there can only be one of each representative object in a set. 
# Sets can be used to retreieve unique values from a list for example. 
my_list = [1,2,1,1,2,4,3,2,1,2,2,2,1]
print(set(my_list))

# Thereefore, it is useful to cast a string to a set in order to isloate the individual elements within your string. 
# So no matter the complexity or repetition in your string, you are able to identify these values. 
# Your output will also be in curvy brackets {}, indicative of a dictionary. This is wrong however, as there are no key value pairs. Just coincidental notation. 