# The collections module in python privides a variety of more specialised container objects, as opposed to the general containers we normally have' like dictionaries and tuples. 


# Let's say for example, we wanted to count how many 1,2 or 3s there are in a list. 
# Normally we would have to iterate through the list using a for loop and have someone kind of counting mechanism. 
# The Counter class does this for us instead - 

from collections import Counter

my_num_list = [1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3]

print(Counter(my_num_list))


# This works with letters and strings too -

my_letter_list = ['a','a','a','b','b','b','b','b','c','c']
my_str = ('aabbccddeess')
sentence = 'How many times does each word show in this sentence with a  word'

print(Counter(my_letter_list))
print(Counter(my_str))
print(Counter(sentence.lower().split())) # If you don't use the split() method, then Count will coutn each individual letter. 
# You can use lower to ensure that the same word is group together, and not seperated because of captials.  

# If you have one item, then Count will focus in each individual character, if you have a comma denoting a list, then Count will count on each individual item.     

# Although the outout of the Counter class is similar to that of a dictionary, they are not the same. 
# Counter is a sub-class of dictionaries.   


# There are also a variety of methods you can use alongside Count.

# You can use .most_common() to recieve an output of tuples, showing you the most common item in what you inputted. 
# Count already seems to do this, but maybe having it tuple form is useful. 

letters = ('abbsshhhhffffffsii')

c = Counter(letters)

print(c.most_common()) 
# You can provide an arguement for the most common method to ask for the top n values, in this case the nth most common. 

print(c.most_common(3))

# If you cast your assigned object to a list, you can get a list of the most common items. 
unique_c = list(c)
print(unique_c)

# There are a variety of other methods that specialise in the counting and finding of unique items. 






# The next import is default dictionary.

from collections import defaultdict

# Normally when you have a dictionary and you call on a key that does not have a value, you will get a key error. 
# Default dictionaries allow you to produce a default value, in the case of there being a key error. 

d = {'a':10}
print(d['a' ])

# print(d['NONE']). This would produce a key error. 


d = defaultdict(lambda:0)
print(d['NONE']) # The default value of zero has been automatically assigned to 'NONE'. 



# Another noteworthy thing you can import from defualt dictionary are named tuples. 
# Normally, all you would have is an index number associated with some sort of value. 
# This is normally fine, but when you have a very large tuple with possibily hundreds of indexs and associated values, it is impossible to keep account of the pairs 
# Using named tuples, you can associated a value with a string instead, to easily call upon it. 

# Named tuples function as easy to create, light weight objects, like what we looked at in OOP. 
# Named tuples are used for easier function, but also to make your code more readable. 

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
point_one = Point(1.0 , 3.0)
point_two = Point(2.5 , 6.0)

from math import sqrt 

line_length = sqrt((point_one.x - point_two.x)**2 + (point_one.y - point_two.y)**2)
print(line_length)  


