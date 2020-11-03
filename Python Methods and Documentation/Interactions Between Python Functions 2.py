# Like we have done before, we are able to import certain functions jusing the 'from random import _' generl form. 
# In this case, we wil be importing the shuffle() function, a function that randomly sorts a list. 
from random import shuffle 
basic_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(basic_list)

# Using this function, we are able to model a ball and cup game, where a ball will be shuffled randomly between three cups and it is up to the user to pick and cup and guess where the ball is. 
# We will do so be using all of the knowledge we have assembled thus far and also the shuffle() function. 
# First we must model the cups and ball themselves and then the shuffling of those cups - 

cup_list = ['','O','']

def shuffler(general_cup_list):
    shuffle(general_cup_list)
    return general_cup_list 


# Now that we have a returned shuffled value, we can actually assign the shuffled list to it's own variable. 
shuffled_cup_list = shuffler(cup_list)

# Next we have to model the user actually picking the cup itself, the mst effective way of doing this is via index position. 
def guessing_input():
    guess = ''       ''' Guess will be a place holder, before the user has inputed a number.''' 
    
    while guess not in ['0','1','2']:
        guess = input('Please enter one of these numbers - 0,1 or 2.') # We need to have an index position of between 0 and 2 being picked, because there are only three cups. 
    
    return int(guess)  # The output of the input function will always be a string, so we have to use the int() function to be able to work with indexes.
        # Make sure that the return statement is outside of the loop, otherwise is will break the loop prematurely. 
# To summarise, the guessing_input() function has allowed us to store the guess value in a processable way, next we have to check the outcome with another function. 
    

# The next step is to compare the guess value with the randomised cup and ball strings to see the outcome. We will have responses for the outcomes of course.  
def game_outcome(shuffled_cup_list, guess):
    if shuffled_cup_list[guess]=='O':       # If the index position the user chose matched the index position where the 'O' lies (the ball), then you get the positive outcome and vice versa. 
        print('Good job! You found the ball!')
    else: 
        print('Oh no! You just missed it')
        print(shuffled_cup_list) # Printed the shuffle list to show the user where the cup actually was. 
    # Note that there is no need for a final return, as we already have the output we want and there will be no more assigning values. 
        
    
# The original list - 
cup_list = ['','O','']

# The mixed list - 
shuffled_cup_list = shuffler(cup_list)

# The guessing input - 
guess = guessing_input()

# The outcome - 
game_outcome(shuffled_cup_list, guess)