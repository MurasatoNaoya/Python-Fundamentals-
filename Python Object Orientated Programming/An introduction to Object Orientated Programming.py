
# The key principle to object-orientated programming is the 'class' function as well as assigning attributes to the class. 

# There are types of objects that we have worked with before, ones that are built into Python. 
# Objects like sets, lists and tuples. 
# We can even check the name of such built-in objects, using the type() function; like so - 

my_list = [1,2,3]
my_tup = (1,2,3)
my_set = set([1,2,3]) # You can also use curly braces instead, if you want to define a set. {}

print(type(my_list))
print(type(my_tup))
print(type(my_set))

# These are fine, but how about creating our own objects.. 
# For this we need the class function, the class fucntion defines the nature and use of an object later on. 
# From classes you can create an instance of an object, an instance being a particular object of one class; but this will be clearer later. 

# When defining a class, it is good practice to use CAMEL CASING, as opposed to SNAKE CASING using when defining functions. 

class SampleClass(): # Here is a simple definition of a class, the only attribute being pass. Here, SampleClass is an instance of a class. 
    pass 

my_sample = SampleClass()

# Here is another class, this time with more descriptive and complex attributes, using the 'init' keyword. 
class Dog():
    def __init__(self,breed): # The init keyword allows you to create a class description. Such description, is commonly referred to as 'attributes'. 
    # What this actually does is create an instance within the class, that can later be called upon specifically. 
        self.breed = breed # The keyword 'self' is important to specify that all of the attributes being created, are in relation or regarding the specfic class. In this case 'Dog'. 

my_dog = Dog(breed = 'Lab') # You can then assign specific instances (specific objects) to other variables. Thus, my_dog is an instance of the dog class, where breed = 'Lab'. 
print(my_dog.breed) # You can then print out the attributes of these specific objects (instances). 
print(type(my_dog)) # Here the __main__.Dog output we get, demonstrates that 