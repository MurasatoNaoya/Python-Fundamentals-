# It is important to notem, that the assignment of variables within functions only take effect when the function itself is called. 

x = 25
def printer():
     x = 50 
     return x

print(x)
print(printer())
# The terminal outputs for both of these print statement is a testament to that. 
# The may seem obvious, but it is a common mistake and such a distinction will be very useful down the line. 

# The reason for Python prioritising 
# L - Local, names assigned in any way within a function (def or lambda), and not declared global in that function. 
# E - Enclosing function locals, names in the local scope of any and all enclosing functions (def or lambda), from inner to outer. 
# G - Global (module), names declared at the top of a module file, or declared global in a def within the file. All the way to the left. 
# B - Built-in (Python), names preassigned in the built-in names module: open, range, SyntaxError etc.. 

# Therefore, the reaosn why the x=25 was prioritised over the x=50, is because x=25 is local to the calling/printing of itself. 
# However, if you instead call the fucntion, the value of x that is most local to the function 'printer', is x=50. 

# This idea of being local for functions can be better explained through nested functions. 

name = 'THIS IS A GLOBAL STRING' # Text editors cannot represent this as output, as there is one. Juypter provides the terminal output as well as genra output. It's better for this kind of stuff. 
def greet():
    name = 'James' 
    
    def hello():
        print('Hello there'+ name)

print(greet()) 

# In the above code, you would recieve an output 'Hello there James', as there is no 'name' definied locally, but the next most local variable name would be in the  enclosed function; 'James'. 


name = 'THIS IS A GLOBAL STRING' 
def greet():
    # name = 'James' 
    
    def hello():
        print('Hello there'+ name)

print(greet()) 
# However, if you were to chnange name = 'James' into a comment, and then call greet(), name would be equal to 'THIS IS A GLOBAL STRING'; as that would be the next most local assignment to 'name'. 
# The same example can be made of local assignments. 

name = 'THIS IS A GLOBAL STRING' 
def greet():
    # name = 'James' 
    
    def hello():
        name = 'I AM A LOCAL STRING'
        print('Hello there'+ name) 


# The highest priority is the built-in functions and commands, like errors that say your code is faulty. Makes sense how these take precedent, otherwise your program that is incorrect would run fine. 

# Here is another example demonstrating the flow of LEGB. 
x = 50
def func(x):
    print(f'X is {x} ')

    #LOCAL REASSIGNMENT! 
    x = 20
    print(f'I just reassigned the value of x to {x}')

print(func(x))

# If you want to have a definite value of x, you can use the 'global' keyword to force the program to jump to global priority and take the global value of (in this case) x.
# Meaning, if global x is stated, any change to x later on has a permanent GLOBAL effect on the x variable. 
# In this case, the final global value of x would end up being 20. 

x = 50
def func(): # In this instance you don't need an arugment, because the function is only assigning x based on what x is assign to below. 
    global x # The function will jump to the global name space.
    print(f'X is {x} ')

    #GLOBAL REASSIGNMENT! 
    x = 'NEW VALUE' # The new global value of x would be 'NEW VALUE'. Your local variable assignments now affect your global variables. 
    print(f'I just reassigned GLOBAL X  x to {x}')

# This works in principle, but using the global keyword as a beginner or in big sets of code can lead to complicated bug and errors; due to the drastic shift in priority. 
# Instead, it is better to make the local function x a new value, and then return that x value at the end of your function. You can then reassign your global x, to the function output. 

x = 50
def func(x):
    print(f'X is {x} ')

    #LOCAL REASSIGNMENT! 
    x = 20
    print(f'I just reassigned the value of x to {x}')
    return x

x = func(x)
print(x)
# The value of x has been reassigned, without having to use the global key word. 
# This is generally a much better way of reassigning a global variable, due to the it being cleaner and avoiding control flow bugs or confusion. 




