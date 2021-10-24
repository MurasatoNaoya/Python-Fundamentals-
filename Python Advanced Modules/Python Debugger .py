# Typically, if you are confronted with a type error, you have to use several print funcitons to see where you went wrong by checking the values of your variables. 
# Instead of this inefficient process, you can use the debugger module to check your error in realtime. 
# An example of such an error could be a type error or an indentation error. 

import pdb 

x = [1,2,3]
y = 2
z = 3 

result1 = y + z # An integer and a list cannot be added together, only concatenated, thus leading to a type error. 
print(result1)

pdb.set_trace()

result2 = y + x # Both x and y are integers, therefore there is no problem in adding them. 
print(result2)

# The Python debugger module allows you to play around with the variables, particularly when dealing with large sets of code. 
# Essentially putting a pause in your script, so you can see what variable values your dealing with and see what is causing the error. 
# Instead of having to use several print functions to have an idea. 

# Finally, when you're done, you can input 'q' into the debugger terminal leave the terminal. 



# If you wanted to add x and y together, then you could add them together as the same data type; being lists in this case. 

