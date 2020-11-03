# A while loops is a loop of executed code, under the assumption a condition is being met. 
# For example, 'fill my pool with water, until it's full.' 
# Make this disticntion clear - FOR loops iterate until all elements have been iterated through; unless said otherwise. 
# WHILE loops does not iterate through, but rather an action(s) and continutes until a condition is met; unless said otherwise. 
# You can of course, add additional action to get closer to that final condition. 

# The basic syntax of a while loop being - while some_boolean_condition:
                                              #do something 

x=0 
while x<6: # The initial condition. 
	print(f'The current value of x is {x}')
	x=x+1 # x increases by one for each iteratio, until x>6. 

# You can also combine a while loop with an else statement. 
# So when the pool is not full is false, something else can happen. Like stopping the water. 
 
x=0 
while x<6: 
	print(f'The current value of x is {x}')
	x=x+1  
else: 
	print('x is now not less than 5')

# To clarify, we are now diverging from while loops specifically, unto to general ideas out loops in Python. 
# When it comes to loops, there are 3 keys words you must know. 
# Break, continue & pass. 

# 'Pass' is used as a place holder. It allows code that is unsatisfied and would otherwise lead to an error to go through. 
# A good example is not defining an action for a for loop. 
# You may be undecided, 'pass' allows the code to run smoothly, ignoring the for loop. 

d = {'key1':'a','key2':'b','key3':'c'} 
for key,value in d.items():
	pass # When you haven't decided on an action. As for loops need an action/purpose for their iteration. 

#'Continue' with a selected element, makes the code skip the selected object; but contuine on with the remaining instructions. 
d = {'key1':'a','key2':'b','key3':'c'} 
for key,value in d.items():
	if value == 'a':
		continue
	print(value)
# 'Continue' leads the code to the top of the loop, ths missing the where 'a' would have been printed. Useful if you want to avoid a specific element for some reason. 

# The final statment is 'break'. 
# 'Break' simply stops the code from running, by breaking out of the loop and ending the loop. 
d = {'key1':'a','key2':'b','key3':'c'} 
for key,value in d.items():
	if value =='b':
		break
	print(value)

# An example with While loops - x	
x=0
while x<5:
	if x==5:
		break
	x=x+1
	print(x)


	
 