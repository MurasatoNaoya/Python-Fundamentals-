
# What is the boolean output of the cell block below?

# two nested lists
 l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
​
# True or False?
l_one[2][0] >= l_two[2]['k1']


# Isolate the string 'hello' in these dictionaries. 

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1]) # Solved, treat it almost like a directory. 

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2]) # Quite tough, but solved. 

