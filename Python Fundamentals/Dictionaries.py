
# While lists is a means of storing information in a consistent, sequential manner, dictionaries store information via 'key value pairings'.
# Much like the name suggests, it's like your variable is a word and the object is its defintion.
# Dictionaries are useful, becuase you do not need to know an index position to retreive an object, just the variable in question. 
# Unlike strings, dictionary syntax is curly brackets {}, as opposed the block brackrts [], used for strings. 	
# A downside to this howeever, is the that you are unable to sort a dictionary, sacrificing convient retrival; for sorting fuctionality.  
# In terms of syntax, the keys should always be written as strings, while the values assocaited with them are flexible;  at least in Python. 
# A very important distinction, is that within a key, you may find a list. So you will have to define an index to isolate the desired element within the list. 

my_dictionary = {'key1':'value1', 'key2':'value2'}

# When retreiving a value from a dictionary however, you use block brackets []. 
print(my_dictionary['key1'])

# Implementing this into a more realisitic situation, dictionaries are often used to retrieve prices for goods. 
price_lookup_library = {'cod_fillet': '4.2', 'salmon_fillet': '5.0'}
print(price_lookup_library['salmon_fillet'])

# Dictionaries have been shown to be able to hold integers and floats, but they can hold a list or even other dictionaries. 

my_dictionary1 = {'key4': 'value3', 'key5': [1,2,3], 'key6':'value4'}
print(my_dictionary1['key5'])

# You can also use indexing for a specific value within the list, within the dictionary. 
print(my_dictionary1['key5'][2])

# 	Now for the dictionary. 
# For a string, you would need to use a fuction like .append to add anything to the string.
# For dictionaries, there is no need for a fucntion, you can add a keyvalue using block brackets []. 

my_dictionary1['key7'] = 'value5'
print(my_dictionary1)

# Using this same logic, you can also overwrite and reassign keyvalues in a dictionary. 
my_dictionary1['key4'] = 'NEW VALUE'
print(my_dictionary1)
 
# There are however, functions that are specifically for dictionaries. 
# If you want to recall all objects within a specfic dictionary, you can use the .keys() functions. 
print(my_dictionary1.keys()) 
# If you want to recall the values that are associated with the keys, then you use the .values() function. 
print(my_dictionary1.values())
# Finally, if you want to recall the keyvalue pairs, then you use the .items() function. 
print(my_dictionary1.items())