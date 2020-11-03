# Linked to the introductory work we did for Booleans, comparision operators if the LHS that produces a Boolean. 

# Below is the comparison operator for equivalence; ==. 
# You don't use one equal sign, =, because Python will think you are trying to assign a variable, as opposed to demonstrating equivalence. 
print(2==2)
print(2==1)

# Equivalence can also be used for other data types like strings. 
print('hello'=='hello')
print('Hello'=='hello')
# Capital letters are enough to differentiate strings, so be careful using them. 

#Python will also consider data types when checking for equivalence. 
print('2'==2)
# Floating points however, are considered the same as an integer. 
print(2.0==2)
# The same rules for equality hold true for other comparitive statments.

# Below is the comparison operator for inequality; !=. 
print(2!=2)
print(2!=1)

# You then have greater than and less than, as well as equal to; which are pretty self-explanatory. 
print(2>3)
print(2<3)
print(2>=3)
print(2<=3)