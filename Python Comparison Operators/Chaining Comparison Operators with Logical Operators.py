# Logical operators allow you to chain comparision operators togther, allowing the implementation of mroe complex and nuancied statments. 
# These logical operators are similar to conditonal statments used for Venn diagrams. 

# The first of such operator is the 'and' logical operator. 
# A True statemtn will only be produced, if both conditions are satisfied. 
print(2>1 and 3>2) # This will produce a True result, as both statments are correct. 
print(1>2 and 2>1) # This wll produce a Flase result, becuase the right statement is incorrect. 

# The same thing can be done with different data types too. 
print( 'h'=='h') and (2==2) 

# The second logical opeator is 'or'
# For an 'or' operator, only one of the statements presented has to be true, for a True result to be produced. 
print(2>1 or 1>2) # An instance where one statment is true. 
print(2>1 or 3>2) # An instance where both are true. 
print(1>2 or 2>3) # An instance where neither statment is true. 

# You can use an inequality rather than using such logical operators, but 'and', 'or' operators make the code a lot mroe readable and easy to grasp. 
print(1<2<3) 
print( 1<2 and 2<3) 

# Finally, there is the 'not' operator. 
# The 'not' operator is used to recieve the opposite Boolean output; contrary to the normal Booelan output. 
print(not(1==1)) # The statment is True, but the opposite Boolean will be returned due to the 'not' operator.
print(not(1==2)) # And vice-versa. 