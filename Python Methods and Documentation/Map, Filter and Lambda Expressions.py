# There are more built-in funtions in Python hat are related to functions, all build-in functions in VS are represented by yellow font. 

# The first one of these would be the map() function. 
# The map function() 'maps' a user-defined function unto a sperate data set, by defining the particular function and the data set you want to map unto. 

def square(num):
    return num**2
# If you want to square every number within a list, you would need to iterate through the list using a for loop. 
# This coudld take time, so to avoid this you use the map() function to map this square process onto every individual element within the list. 
# Finally, bear in mind that if you print the output of just the map() function, all it will give you is the data location on you computer, which is not helpful. 
# To avoid this you must cast it the mapping to a list, or print the output within a for loop. The former however makes more sense in this case. 

num_list = [1,2,3,4,5]
print(list(map(square,num_list))) # This is the cast to a list example, that prints the mapped list. 

for num in map(square,num_list):  # This casts the list onto each element individually, then prints them. 
    print(num)

# The map() function however, doesn't really do anything different compared to a for loop that accomplishes the same outcome. 
# There is more debate about how the map function() looks possibly cleaner and that when you see a map() function you know what is goin gon immediately, rather than a for loop that could be about anything. 
# The map function may not be the go-to or most familiar method, but it is nonetheless a note worthy built-in function. 
for num in num_list:
    print(square(num)) # The for loop that accomplishes the same thing. 

# You can also use the map function() for more complex functions. 
def splicer(a_string):
    if len(a_string) %2==0:
        return 'EVEN'
    else:
        return a_string[0]

name_list = ['Andrew','James','Mary']
print(list(map(splicer,name_list)))    

# There is of course another for loop alternative. 
for name in name_list:
    if len(name) % 2==0:
        print('EVEN')
    else:
        print(name[0]) # To cast the outputs to a list, you could append an empty list or use list comprehension. 

# The list comprehension variant - 
applied_list = ['EVEN' if len(name) % 2==0 else name[0] for name in name_list] # Perhpas the map() function is more readable in the end.. 
print(applied_list)

# The append variant - 
empty_list = []
for name in name_list:
    if len(name) % 2==0:
        empty_list.append('EVEN')
    else:
        empty_list.append(name[0])

print(empty_list)

# The map function is another, perhaps cleaner way of going about this. 
# Map makes sense to use, when you have alrrady definied a function, perhaps c complex on and want to map it onto something else. 
# Rather than a single use case, where for simple code intended for one time use, a for loop would be more optimal. 


# The next in-built function is the fliter() function. 
# As the name suggests, the filter function filters through a list, selecting the few that pass the critera; creating a new filtered list. 

def even_checker(num):
    return num % 2==0 # This function will return a True boolean value if the number is divisible by 2. 

num_list = [1,2,3,4,5]
print(list(filter(even_checker,num_list))) # It is very important to note that the filter only operates with a boolean critera. 
# So if an element is True for a function, then the element will not be filtered. Much like the map() function, the pure output of filter will just be the data location; it must be cast to something. 
for num in filter(even_checker,num_list): # Remember that you can use both filter() and map() next to 'in'. 
    print(num)

# It is important to note that you do not have to call the map and filter functions, for they already do so with the inputted function and input list. 


# Now that we have gone over both of the built-in functions filter() and map(), we can begin to go over Lambda expressions. 
# When it comes to Lambda expressions, context is very important. 
# If you are using a function that is imperative to your code and one that you will be calling a lot of the time, defining the function is best. 
# But if you want to use a function use one time, for one figure or process, then you are most likely better off using Lambda expressions. 
# Lambda expresion allow you to carry out a comple process like a function, without needing to define the process or even give the process a name in the first place. 

square = lambda num: num**2 # This expression says it will be squaring thr inputted num value. It is asummed everything on the right side of the colon will be returned. 
print(square(5))
# This is fine, but lambda expression shine the brightest when they are used in tandem with other functions, like filter() and map().

# Here is an example of the earlier map() function example, of squaring a list of numbers. 
print(list(map(lambda num: num**2, num_list))) # This is exactly the same output to a similar question we had earlier, but instead of defining a function, we used a single used lambda expression. 

# Here is an example of the earlier filter() function example, filtering for only even numbers. 
print(list(filter(lambda num: num % 2==0, num_list)))

# You can of course use lambda expression to deal with strings - 
print(list(map(lambda letter: letter[0], name_list))) # This lambda expression takes the first index of a name list and then maps it onto a new list. 

print(list(map(lambda letter: letter[::-1], name_list))) # You can even use slicing to reverse each individual element, as you could do with a normal function. 





