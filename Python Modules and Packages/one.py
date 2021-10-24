# Python is special in the fact that it runs all of the code on indentation level 0, no further questions asked. 
# In other languages, you define a main() piece of code that is always run automatically. 

# We have deal with built in functions and operators already, but we have yet to see a built in variable.   
# __name__ is such a variable. 
# In the backgroud, if you are running a Python script direcly, as opposed to importing other sripts in the form of modules, Python will assign the variable __name__ = '__main__'. 
# This is very useful, because amongst complicated code whether or not your are running a script directly or not. 

def func():
    print('func1 is in one.py')

print('TOP LEVEL IN one.py')
# You can use an expression like this to have your program to adjust considering if it's run directly or not - 
if __name__ == '__main__':
    print('one.py is being run directly.')
else: 
    print('one.py has been imported.')

# The significance of __name__ is that you can have a script perform specific actions, based on whether it has been called directly; or has been imported. 
