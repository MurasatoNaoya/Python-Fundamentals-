# There may be instances where you simply want to change the data type of something. 
int_i_want_to_be_a_string = 3
# Just cast the integer into a string using str()
print(str(int_i_want_to_be_a_string))
# The same thing can be done for all data types
print(float(int_i_want_to_be_a_string))

# There will also be instances where you have to cast something to a list before it can be printed, or even materialised properly. 
print(range(3,2,15))#
# This would literally print - 'range(3,2,15)', which is not what you want. 
# So first assign the output to a list and then print it, so actually get the numbers that satisfy the conditions. 
print(list(range(3,15,2)))

# To refresh, you also check the data type of something with the type() function too. 
print(type(int_i_want_to_be_a_string))