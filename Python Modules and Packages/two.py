# To demonstrate the signifiance of __name__, we can test importing one.py instead. 

import one # Make sure that both the direct script and the module are in the ame folder, otherwise you can't just put 'import'. 
           # The code within what is being imported will be run, however, nothing; no functions will be called. 
print('TOP LINE OF TWO.PY')

one.func()

if __name__ == '__main__':
    print('two is being run directly.')
else: 
    print('two has been imported.')

# When you run this, the reason why you have print statements from the one script, is due to the print statements in one.py not being bound in a function, therefore when imported the print statements run. 
# The previous example of module_example had all action enclosed in a fucntion, therefore nothing could be run. 
# The outcome of the __name__ if statement changed, due to the nature of calling one, __name__ was not equal to '__main__' was we were working from two.py; not one.py. 

# In the real world, else statement are rarely used like we have done as it used more to organise code. 
# if __name__ statements will be used to call upon pre-defined functions, given that the script in question has been imported or not. 
# More as a pre-requisite to run the whole script in the first place or otherwise. 




