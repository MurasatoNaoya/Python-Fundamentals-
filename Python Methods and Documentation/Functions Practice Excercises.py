# Warmup Section - 

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but return the greater of the two given numbers if one or both are odd. 

def less_of_two_evens(x,y): # Remember that the argument represents the variables that you will be inoutting into the function. 
        if x % 2==0 and y % 2==0: # You have to set the parameter for both of the variables individually. 
            return min(x,y)
        else:
            return max(x,y)

print(less_of_two_evens(3,2))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter. 
def str_index_0_checker(string): # What we can make use of here is the double index [][], which allows us to get the indexes of individual strings, but within a list. 
    wordlist = string.split() # When you are assigning variables, you use the single = sign, but when you want to demonstrate equivalence; you use ==. 
    return wordlist [0][0] == wordlist [1][0] # This means - "Return the boolean of the first index of the first string, being equal to the first index of the second string."


print(str_index_0_checker('Hello World'))
print(str_index_0_checker('Wonderful World'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(x,y):
    if x+y == 20:
        return True
    elif x==20 or y==20:
        return True
    else:
        return False

print(makes_twenty(20,17))
print(makes_twenty(2,78))

# Level 1 questions - 


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def one_four_cap(name):
    index_position = 0
    empty_str = ''
    for _ in name:
        if index_position ==0 or index_position == 3:
             empty_str += _.upper()
        else:
             empty_str += _
        index_position += 1
    return empty_str
    
print(one_four_cap('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed.

def yodafication(string):
    world_list = string.split()
    return world_list[::-1]

print(yodafication ('Hello there, my name is Andrew')) 


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200. 

def almost_there(num):
    if 110 >= num >= 90:
        return True
    elif 210 >= num >= 190:
        return True
    else:
        pass 

print(almost_there(204))


# Level 2 questions - 

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def three_three_checker(array):
    for _ in range(0, len(array)-1): # Also bear in mind that the range() function creates a list on numbers within the said range. 
                                    # But the range PARAMETER in a LOOP just gives the program a range of iteration, an inequality for how far the next element can be picked. 
                                    # In this case, you must have the for loop stop iterating one before the last element, otherwise the last element would be array[i] and i+1 would be nothingness.
                                    # This causing an error, as there is no next element to take in consideration.  
        
        
        print(array[_]) # It is very important to note that you can use index brackets to specify what element you are mentioning in your for loop, with regards to your string. 
                        # You can addition and subtraciton to move along the elements you specify. For example, array[_] in your first iteration would be the first element within the array you provide. 
        if array[_] == 3 and array[_+1] == 3: # Remember this isn't about indexing, there are no numbers, it is pulling the element in the array depending on what no. of iteration cycle. 
            return True
    
    return False
        
print(three_three_checker([1,4,3,3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def triple(string):
    empty_string = ''
    for letter in string:
        empty_string += letter*3
    return empty_string

print(triple('Hello World!')) # ! and signs count as iterable objects, and thus will be multiplied by 3. 


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'. 

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21: # Note that when you are defining an arugment in your function, you don't need the [] of a list, for you are only defining variables. 
        return sum([a,b,c])
    elif sum([a,b,c]) > 21 and 11 in [a,b,c]: # Remember that 'in' is used to demonstrate the presence of something. 
        return sum([a,b,c]) - 10
    elif sum([a,b,c]) > 21:
        return 'BUST'

print(blackjack(5,6,7)) # Once again no need to specify a list in your input with [], you are only defining the variables, they are made into a list within the function. 
                        # This is because the argument is specified as 3 individual argurments. 


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9. 
# (Every 6 will be followed by at least one 9). Return 0 for no numbers.

def six_to_nine(num_array): # A while loop a boolean format is necessary, because of there being two prolonged conditions. 
    array_total = 0  
    add = True              # Addition will be paused when a 6 is encountered and will only resume when a 9 is encountered. 
    for _ in num_array:     # An empty string append solution would not be viable due to there being no way for the PROLONGED condition to be accounted for. 
        while add:          # You can use an 'if' statement to ensure there would be no addition of the 6, once the 6 has been encountered. 
            if _ !=6:       # But there is no other way then boolean logic to ensure that further addition does not happen post the 6, until a 9 is encountered. 
                array_total += _ # Booleans are ideal for such a scenario. 
                break
            else:
                add = False
        while not add:
            if _ !=9:
                break
            else: 
                add = True
    return array_total

print(six_to_nine([1,2,5,6,9,23,4]))         


# Challenging problems - 
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(num_list):
    for _ in range(0,len(num_list)-2): # You need to use the range of len()-2, or the '_+1' and/or '_+2' value might be nothingness, leading to an error. 
        if num_list[_] == 0 and num_list[_+1] == 0 and num_list[_+2] == 7: # Consecutive nature. 
            return True
        
    return False

print(spy_game([3,5,8,9,0,0,0,0,7,3,5,0,7,8,9]))

# Now this is acceptable if the question wanted the 007 right next to each other, but the quesiton specifies that any spacing is fine, as long as the order is consecutively 007. 
# Meaning that - [0,4,3,0,8,7] is just as valid as [0,0,7]. 
# An adjusted program accounting for this goes as such -

def spy_game_2(nums):
    pop_list = [0,0,7,'x']
    for _ in nums:
        if _ == pop_list[0]: # The pop method allows us to account for patterns that are non-consecutive, also long as they fulfill the requirements of the 'popping'. 
            pop_list.pop(0)
    
    return len(pop_list) == 1 # 'x' would be the only remaining element, therefore len() = 1. 
    # Or, return pop_list = ['x']. pop_list would still be classified as a list, even if it only contains one string which is 'x'. 

print(spy_game_2([1,0,2,4,0,5,7])) # You have to use square brackets to specify a list, because the function argument has no specified individual list elements. 
print(spy_game_2([1,5,3,7,2,0,3,7,0]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number, 0 and 1 will not be counted as primes. 
def prime_counter(num):
    prime_list = [2] # This is the list of prime numbers that we will be appending to. 
    x = 3 # This would be the first prime number that we would account for. 
    # Check for 0 or 1 - 
    if num <2:
        return 0 # For there at no prime numbers that are less than 2, as 0 and 1 not distinctly prime.     Also bear in mind going forward that 2 is already accounted for, so x = 3. 
    # A number that is 2 or greater - 
    while x <= num:          # You only want to be checking for prime numbers up until the number inputted, the while loop ensures this parameter. 
        for _ in prime_list: # In this case your _ value would be all of the values for each iteration starting at 3, ending but not including x within intervals of 2. In a sense, all of the non primes. 
            if x % _ ==0:    # Bear in mind that when defining a range in a for loop, you use commas not colons. (3,x,2), not to be confused with indexing where it would be (3:x:2). 
                x += 2       # Also bear in mind that it doesn't really mater what _ is, as long as you divide it by x; because it is only a means of checking for prime numbers.        
                break # If this condition is met, the for loop would then be broken out of, but so long as the while loop is valid, the for loop will persist anyway;  but this time with x+2n. 
            else:
                prime_list.append(x)
                x +=2
    print(prime_list)
    return len(prime_list)







                        
                            
    