# The [] brackets are used for lists. 
my_list = [1,2,3]  # A list of integers. 

# You can create a list with varying object types. 

my_other_list = [1, 'hey', 1.2] 

#The fucntion 'len', can be used to idenfity the number of variables within the list. 

print(len(my_other_list)) # The len function will only determine the number of variables in your list, you have to use the print function to show the result.  

# We can also use indexing and slicing with lists, because just like a string; it is an ordered sequence.  
print(my_list[0]) # Same thing for indexing, you may of found the specific value, but to show it you have to use the print function. 

# You can also use Concatenation for lists. 	
print(my_list + my_other_list) 

# You can then create a new list from the concatenated string. 
new_list = my_list + my_other_list 
print(new_list) 

# Unlike strings, lists are mutable. Meaning you can change individual items within the list. 

new_list[0] = ' ONE ALL CAPS'
print(new_list)

# You can add a variable to the end of a list permanently, using the append method. 

new_list.append('5')
print(new_list)

# You can also remove the last varible within a string permanently, using the pop function, the output will also be the removed variable. 
new_list.pop()

print(new_list) 
popped_item = new_list.pop()
print(popped_item) 

# The pop method wil always take the (-1) index off a list, thus; reverse indexing works for lists also. 

new_list = ['a', 'x', 'b', 'c']
num_list = [4,1,8,3] 

#You can use the sort lists with the sort method. e.g Alphabetical, asecnding sequence. 

new_list.sort()
num_list.sort()
print(new_list)
print(num_list)

# You can also assign sorted lists to new variables, after sorting. 

new_list.sort()   
num_list.sort()
sorted_new_list = new_list 
sorted_num_list = num_list
print(sorted_new_list)   
print(sorted_num_list)

# Yet another method you can apply to a list, is the reverse method. 

sorted_new_list.reverse() 
reversed_sorted_new_list = sorted_new_list
print(reversed_sorted_new_list)

# You can also have a list, within a list. This is called a 'nested list'
nestedlist = [1,2,3,[4,5,6,'hello']]
print(nestedlist[3][3])

# Remember thos [][] notation for nested lists, you can also use this notation to reassign indexes in the nested list. 

reassignedvalue = 'goodbye'
nestedlist[3][3] = 'goodbye'
print(nestedlist)
