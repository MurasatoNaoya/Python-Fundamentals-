# Tuples are similar to lists, they can store many object types, objects are retrieved via index locations. 
# However, unlike lists, Tuples are immutable; meaning objects within the tuple cannot be reassigned. 

# Pre-reassignment
first_list = ['breakfast', 'lunch', 'missing']
print(first_list) 

#Post-reassignment
first_list[2] = 'dinner'
print(first_list) 

# If you did this exact thing but with a tuple, you would get an error due to its property of Immutability. 
# Specifically - 'Tuple does not support item assignment'.

# Instead of [] for lists and {} for dictionaries, for tuples; you use ().
t = (1,2,3,4,2,2)
print(type(t))
print(len(t))
# Just standard stuff, making a tuple variable, and checking its length. 

# There are two built in method for tuples in Python. 
# The count method, .count(), counts how many times a certain item shows up in a tuple. 

# Let's say I wanted to count how many twos are in my tuple. 
print(t.count(2))

# The second method, .index(), this shows the very first time a certain item appears - its index position. 
# Let's check when the item 3 shows up first in this tuple. 
print(t.index(3))

# There is also a sort method, that allows you to rearrange numbers in ascending order. 

# As mentioned before, unlike lists; tuples are immutable. Meaning lists support item assignment, whilst tuples do not. (You will get an error.)
# However the fact that tuples are so sttuborn is an advantage, because this is so impotant for DATA INTEGRITY. 
# When you are dealing with very large code, it isn't uncommon to have items assigned accidentally. 
# The immutibilty of tuples guards against that, thus making them very useful; even if they have less methods than strings.

# You can also use arithmetic with lists, ** does not work apprently..  
print([0,0]*3)