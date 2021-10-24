# Decorators are a more complex concept in Python. 
# You may want to add new capabilities to an already exisiting function, there are two 'standard' ways to go about this - 
# You can either add more code, or functionality to the function. 
# Or you can create a completely new function for this purpose. 

# Both of these methods are laborious and not efficient and can lead to 'calling' problems. 
# You may change your mind and might want to remove that functionality, you would have to manually go through your code the remove the necessary code. 
# Decorators are so useful, due to them serving as an on/off switch for added features and functionalities. Allowing you to add on on/off functionality to other pieces of code. 

# The key syntax for python decorators is the @ symbol. 


# One key idea is that functions are objects that can be passed onto other objects, meaning they create a new copy of themselves when assigned to something new - 
def Hello():
    return 'Hello there!' 

Greet = Hello 

# We can call them and we wil get our expected outputs. 
print(Hello())
print(Greet())


# We can then delete the Hello() function, so that we won't be able to directly call from it. 

del Hello
# print(Hello())     We will get an error here, because after using del on Hello(), we can't directly call it, as it will not be defined. 

# But even after using del on the Hello() function, we can call it from within the Greet() fucntion by calling Greet(). 

print(Greet()) # Here, we will get the same output as Hello(), demonstrating the the Greet() function does not point back to the orignal function, but to its very own iteration. 

# Here is the basic sytax for nested functions, in the first order for the time being -
def example(name='Andrew'):
    print('The example function has been run.')  # You have to make sure that this is a print statment, not return, as it would end the return function before anything is printed. 
    def one():
        return '/t The one function has been executed within the example function.' 
    def two():
        return '/t The two function has been executed within the example function.'
    print(one())
    print(two())

print(example())

# Bear in mind that the one() and two() functions are only within the example() fucntion, meaning their scope is example(). 
# If you try to call either of them outside of the scope of example(), they will not be defined, which makes sense, as they are not global functions. Their scopes are within example(). 


# But what if you wanted to access the functions one() and two() outside of example()? 
# To do this, we can have the example() function return the other functions.  

def example(name='Andrew'):
    print('The example function has been run.')  # You have to make sure that this is a print statment, not return, as it would end the return function before anything is printed. 
    def one():
        return '/t The one function has been executed within the example function.' 
    def two():
        return '/t The two function has been executed within the example function.'
    print('I am going to return a function!')
    if name == 'Andrew':
        return one
    else: 
        return two

my_new_func = example('Andrew')
# By doing this, we are demonstaring the same persistance of reassigning functions, can be done with nested functions also. 
print(my_new_func())
# In summary, you can return a function within another function. 

# Here's another simple example of this - 

def cool():
    def super_cool():
        return 'Hey man, I am so cool!'
    return super_cool

rand_func = cool()

print(rand_func())  # The nature of the cool() function, means that it returns the super_cool, therefore by reassigning the function, we can call super_cool, even though it's in the scope of cool. 

# The next thing we will need to consider when creating a decorator, is having the argument of a function being another function. 

def hi():
    return 'Hi Andrew!'

def other(some_func): # Another function can be used as our argument, it doesn't matter what you name the fucntion here, it just represents our function argument.
    print('Other code runs here!')
    print(some_func())

other(hi)  # We can then use specific functions. 

# So far, we have reassigned exisiting functions to have access to other functions in their scope and also used a general function argument, so we can print them through other functions. 

# With these new ideas, we can begin to create our rudamentary decorator - 

def new_decorator(original_function): # This is a decorator, adding functionality at its most fundamental level. 
    def wrap_func(): 
        print('Some extra code, before the original function.')

        original_function()

        print('Some extra code, after the original function.')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated!!')

decorated_function = new_decorator(func_needs_decorator) # The 'unwrapped' function is passed through our decorator function and is then 'wrapped' and the result is then reassigned. 
# You can think of this decorator process of an assembely line almost, adding new fucntionality to an exisiting function. 

decorated_function()

# The perhaps most important final part, is implementing the @ keyword, this allows you to specify a decorator function, and have an exisiting function be passed through it. 

@new_decorator
def another_function_that_needs_decorating():
    print('I too want to be decorated!')

print(another_function_that_needs_decorating()) # Make sure you're calling the function when you print it. 
# In terms of an on/off switch, you can just comment out the line of code with the @ and the function passing through it will will no longer be decorated. 
# You will rarely be creating your own decorator, you will often instead be using other decorators from exisiting libraries and just applying them to your functions with @.