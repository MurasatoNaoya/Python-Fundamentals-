# Alongside the __init__ function, there are other useful functions in a similar double underscore form. 

# First is the __str__ function that interprets the information at a data storage. 
# If you just print such a thing, you will just get the data location. 
# This idea can be reproduced when you try and check for the len() or type() of the instance you have created, If you do so with a plain class, you will get an error or just be fed back the data local. 
# In any case, both are not very useful, at least not on their own. 

class Sample():
    pass 
simple_sample = Sample()
print(type(simple_sample))
# print(len(simple_sample))   This is commented, because produces the 'Has no len()' error we have already mentioned. 

print(simple_sample)

# The  __str__ function is a good solutions the second of these problems. 
# It makes it so whenever a string representation of anything to do with your class, it will not display the data storage location, but rather whatever you want to return.   

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
    def __str__(self):
        return '{} by {}'.format(self.title,self.author)
        # Now, whenever a string representation of the Book class is requested, the __str__ function will run and return this. 

a = Book('Basic Economics','Thomas Sowell', 1000)
print(a) # This can now be demonstrated, so long as you have defined parameters. 


# Now onto the len(), instead of occuring an error, you can use the __len__ function to return something, when the length of an instance is requested. 

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
    def __str__(self):
        return '{} by {}'.format(self.title,self.author)
    def __len__(self):
        return self.pages

a = Book('Basic Economics','Thomas Sowell', 1000)

print(len(a)) # Note that the __len__ fucntion in itself does not output anything, it just creates the link between the stimulus of length checking and anything you want to return. 

# Another special method to do with objetc, is the __del__ function. 
# Much like the others, the __del__ function doesn't do anything in itself, but link the deletion of something to another action. 
# In our case, we can just have something letting the user know.

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
    def __str__(self):
        return '{} by {}'.format(self.title,self.author)
    def __len__(self):
        return self.pages
    def __del__(self):
        print( 'You have deleted {} by {} from the Grand Library'.format(self.title, self.author))
        # You would want to have print here rather than return, otherwise you won't have a visable respone in the terminal.
a = Book('Basic Economics','Thomas Sowell', 1000)

del a 

