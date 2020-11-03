# The flow of code can be controlled through the use of conditions, like 'if', 'else' and 'elif' statements. 
# Such a process is referred to 'control flow'.

# Firstly, the 'if' statement descirbes an action is that to be carried, out IF a prerequisite has been met. Hence the 'if'. 
# Importantly, it's if the prerequisite is True. 
# e.g if some_condition
	# execute some code


# In the case that the 'if' statement does not go through, you can then use the 'else' statement. 
# The 'else' statement will then go onto execute another piece of code in the positive 'if' statement outcome. 

# e.g if some_condition
	# execute some controlled
# else: 
	# do something else 


# Finally the 'elif' statement is simply used to add extra conditions or prerequisites, other than your inital 'if' statment. 
# It is useful to have this, you often to have more than one filter, before you ask for everything else in the else statement. 
# In summary it is an alternative if statement, rather than generalising completely with else statments. 

# e.g if some_condition
	# execute some code
# elif some_other_condition
	# execute another type of code
# else: 
	# do something else 


# Now for some examples - 

hungry = True
if hungry:
	print('GIVE ME SOME FOOD!')
# This intercation shows that 'if' statments only execute on True inputs, just as 2>3 would give a True output. Explain the False outcome also. 	

hungry = False
if hungry: 
	print('GIVE ME FOOD')


# Arithmetic can also clearly be used as a condition. 
if 3>2:
	print('Crocs like large prey..')

# 'else' statments can also be easily be implement as an alternative outcome to a void output. 

hungry = False
if hungry:
	print('GIVE ME SOME FOOD!')
else: 
	print('I am not too hungry right now, thanks.')

# For more complex control flow, elif statment can be used. 

dinnerpartyconversation = 'Philosophy'
if dinnerpartyconversation == 'Economics':
	print('That was an interesting conversation!')

elif dinnerpartyconversation == 'Philosophy':
	print('That was an interesting conversation!')

elif dinnerpartyconversation == 'Mathematics':
	print('That made my head hurt..')

elif dinnerpartyconversation == 'History':
	print('Hard to believe that happened.') 	
else: 
	print('Ah yes, politics again..')

