
# We have already gone over how we can go about Tuple Unpacking using for loop iteration. 
# Remember when defining a tuple, you have the use a string to denote the key. 
stock_prices = 	[('APPLE',200),('GOOGLE',150),('MSFT', 100)]

# This would be a loop for each individual tuple - 
for _ in stock_prices:
	print(_)

# But you can of course isolate the key and the value itself - 
for key,value in stock_prices:
	print(key)
	print(value)

# So we have demonstrated that we can use for loops for tuple unpacking, but we can then use this for loop method to make mre complex processes with functions. 
# An example of this would be the employee of the month problem - 

def best_employee_checker(workhours_tuple_list):

	maximum_hours = 0				# Make sure that your base values are within the function (indented within the :) that you are defining. 
	employee_of_month = []

	for name,hours in workhours_tuple_list: # Remember, the function creates a general form, so you don't need to have a specific list ot iterate through. You are setting up a process. 
		if hours > maximum_hours:
			maximum_hours = hours 
			employee_of_month = name
		else:
			pass 

	return (employee_of_month, maximum_hours) # The return here just specifies the output of the function, remember, you have to; but can, define this as anything you would like. 

employee_workhours1 = [('Andrew',400), ('James', 300), ('Mary', 320)] 
print(best_employee_checker(employee_workhours1))

# It seems you need an example of tuple to have the for loop function property and therefore have a gall this specific 'machine' that has a job. 
# In this case, this 'machine' selects a best employee based on hours worked. eneral form function. 
# The benefit of this function, but really functions as a whole, is that it allows you to quickly rec
# Otherwise you would have to constantly rewrite blocks of code, when you can just make a general formula function in one go. 

# We can also do a similar thing to the stock model we used to begin with -  
def highest_stock_price_checker(stocks_tuple_list):
	highest_price = 0          # We are jut looking for the most expensive stock. 
	mst_expensive_stock = []

	for stock,price in stocks_tuple_list:
		if price > highest_price:
			mst_expensive_stock = stock
			highest_price = price
		else:
			pass 
	return (mst_expensive_stock, highest_price) # Remember, it does matter what iteration you are onto to return. 
	# If you are getting a problem where only the last tuple is being presented, you may have misstated what you are returning. 

stock_prices = 	[('APPLE',200),('GOOGLE',150),('MSFT', 100),('AND',1000)]
print(highest_stock_price_checker(stock_prices))
