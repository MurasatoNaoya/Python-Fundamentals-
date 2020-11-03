# Unlike the attributes that we have definied using __init__, there are class object variables that are global for every instance within the class. 
# This point can be further illustrated using the 'Dog' class we used before, but with added attributes - 


class Dog():

# Class Object Attribute (SAME FOR ANY INSTANCE OF A CLASS) - 
    species = 'Mammal' # In reality, Mammal falls into a biological class, not species, but to avoid confusion we are using class. 
    # The ordering should go as, 1st class, 2nd class object attribtes; 3rd __init__ to define instance attributes. 
    def __init__(self,breed,name,spots):
        self.breed = breed 
        self.name = name

        # You can also have attributes return Boolean values - 
        self.spots = spots 

my_dog = Dog(breed = 'Lab', name = 'Brock', spots = False) # We have not define what species is in this instance. 
print(my_dog.breed) 
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species) # See that even though we didn't define what species would be in this instance, it still is returned; as it is a class object attribute. 
print(type(my_dog)) 

# Next we have to elaborate on method in object orientated programming. 
# In this case, method are functions that are define within a class to perform specific operations, that often utilise the attributes defined. 
# In this case, they will look very much like functions defined within the class like so - 

class Dog():

    species = 'Mammal' 
    
    def __init__(self,breed,name,spots):
        self.breed = breed 
        self.name = name
        self.spots = spots
    
    def bark(self):
        print('WOOF!')

my_dog = Dog(breed = 'Lab', name = 'Brock', spots = False)
    

    
# A key distinction to be made between attributes and methods, is that attributes do not have () at the end of them; because nothing is being executed. 
# Methods do, because there is an innate process behind them, not just information to be presented. 

print(my_dog.bark()) # If you don't use parenthesis, you will just print the data location of the method. 
print(my_dog.bark())

# In this case we have only printed a string, you could make the function more complex by incorperating attributes that you have defined in your class. 

class Dog():

    species = 'Mammal' 
    
    def __init__(self,breed,name,spots): # The special __init__ funcion allows us to create an instance and build attributes onto our class. 
        self.breed = breed # The point of these re-assignments is so that when whatever you define as 'self' is called with a method, the information in relation to the method is returned. ]
        self.name = name   # In a sense, this is assignment is what creates your method to output link. 
        self.spots = spots
    
    def bark(self):
        print('WOOF! My name is {}!'.format(self.name)) # It is not enough to just say 'name' you have to specify that you are referring to the specific name of this instance. 
            # You can use .format, fstrings or concatination. Whatever is better for you. 

my_dog = Dog(breed = 'Lab', name = 'Brock', spots = False) # my_dog would be an 'instance' if our class. 
print(my_dog.bark())
# The key point being - Method can call ipon attributes for their process. 
# That being, you can directly use arguments for a method, that have been directly defined within the method.

class Dog():

    species = 'Mammal' 
    
    def __init__(self,breed,name,spots):
        self.breed = breed 
        self.name = name
        self.spots = spots
    
    def bark(self,age):
        print('WOOF! My name is {} and I am {} years old!'.format(self.name, age)) # Due to age being an argument not defined elsewhere like witin __init__, it can be called without referring to self. 

my_dog = Dog(breed = 'Lab', name = 'Brock', spots = False)
print(my_dog.bark(20)) # But you then of course have to give an input to the argument in the method. 

# Here's another example of a class and its applications using some geometry - 

class circle():
    # Class object attributes - 
    pi = 3.14 

    def __init__(self,radius=1):  # Like we have explored with functions before, you can set default values, in case there is none inputted. In this case, the radius is set to a default 1. 
        self.radius = radius 
        self.area =self.pi*radius*radius # We are only defining attributes, so you do not HAVE to set an attribute as an argument/parameter. 

    # Circumference method - 
    def circumference_checker(self):
        return 2*self.pi*self.radius # Remember you have to refer to self.etc, to specify the instance you are referring to, because there may be different instances with different name assignments. 

my_circle = circle()
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.circumference_checker())

# One key point is that when referring to class object attributes, in this case you can use self.pi. 
# But another perhaps more commonly used alternative is in our case using - circle.pi. 

class circle():
    # Class object attributes - 
    pi = 3.14 

    def __init__(self,radius=1):  
        self.radius = radius 
        self.area = circle.pi*radius*radius 

    # Circumference method - 
    def circumference_checker(self):
        return 2*circle.pi*self.radius 
    
my_circle = circle()
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.circumference_checker())

# As you can see, both classes are equivalent. 
# Down the line using this circle.py version will be easier, when you are dealing with several instances
           



