# When dealing with fucntions, you will eventually be setting arbitrary parameters for your functions. 

def myfunc(a,b):
    return sum((a,b))*0.05  # This functions returns 5% of the sum of a and b. If you are going to multiply anything too, it has to be at the back of the return statement. 
    # Instead of just using a+b, you can use the 'sum()' function to make your code more scableable.

print(myfunc(60,40)) # This is an example of a 'positional argument', for due to the position of the arguments; 60 will be assigned to 'a' and 40 to 'b'.  

# If you want to account for the possibility of other arguments, you can add more general form arguments in your function. 
def myfunc(a,b,c=0,d=0): # You can make the defaults for the extra arguments equal to zero, meaning they will not be accounted for, unless another argument in inputted. 
    return sum((a,b,c,d))*0.05 # You should get the same result as the defults of c and d are zero, but you can of course input other values if you want - 

print(myfunc(60,40,100,300))

# This is fine, but you would need to keep adding another arugment for a new argument value input; which is not viable for very large numbers of arguments. 
# *args allows you to input an arbitrary number of arugments, which solves this scalability problem. 

def myfunc(*args):
    return sum((args))*0.05 # It is very important to remember that when you are defining the *args argument you need to include the '*; BUT YOU DO NOT WHEN YOU ARE DESCRIBING YOUR FUNCTION. 

print(myfunc(40,60)) # Note that we get the same values, as the *args argument almost creates each individual parameter for you. 
print(myfunc(40,60,70,80,3,4,1,7,5,5834)) # You can keep doing this indefinitely for as many argument inputs as you would like. 

# If you just print what 'args' is, you recognise that is a tuple, as args just uses the inputted arguments as a tuple in your function.  
def myfunc(*args):
    return args

print(myfunc(40,60,70,80,3,4,1,7,5,5834))

# Another key thing to note, is that by convention, we use *args, but it is really just the '*' function that assigns creates the tuples and assigns arguments. 
def myfunc(*anything_but_args):
    return anything_but_args

print(myfunc(40,60,70,80,3,4,1,7,5,5834))

# Much like how '*args' assigns args to a tuple including all of the inputted arguments, **kwargs does the same but instead of assigning the information to a tuple, it does so to a dictionary. 
def myfunc(**kwargs):
    if 'Fruit' in kwargs:
        return('Oh, there is the {} I was looking for!'.format(kwargs['Fruit'])) # This .format takes the value from the key of 'Fruit'.
    else:
        return('There is not fruit that I like here.')

print(myfunc(Fruit = 'Apple', Vegetable = 'Lettuce')) # Noramlly, without first defining what these dictionaries would be in the fucntion, Python would complain.
                                                      # But **kwargs allows us to make these indefinite dictionaries. Again, the assigning of input arguments to dictionaries is the '**' function, not kwargs. 
                                                      # Although, it is good pratice to use args and kwargs, to make it clear what you are doing in your code. 
                                                       
# You can then of course use both *args and **kwargs together, for both indefinite arguments in a tuple and dictionary format. 
def gorcery_interaction(*args,**kwargs):
    print(args)
    print(kwargs)
    return('I would like {} of {} and {} {} please.'.format(args[2], kwargs['fruitA'], args[0], kwargs['fruitB']))

print(gorcery_interaction(10, 30, 'a handful', fruitA = 'oranges', fruitB = 'lemons') )

# *args and **kwargs and thus an arbitrary number of arguments will not be incredibly useful right now, but as you use other libraries and import things from the internet, they will become very useful. 