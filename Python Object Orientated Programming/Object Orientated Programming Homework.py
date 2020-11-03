# 1st Question - Create a 'Line' class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line():
    def __init__(self, coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return  ((x1-x2)**2 + (y1-y2)**2)**0.5
    def gradient(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return (y1-y2)/(x1-x2)

line1 = Line(coor1 = (5,4), coor2 = (2,7))
print(line1.distance())
print(line1.gradient())

# 2nd Question- Create a 'Cylinder' class, along with methods that describe its dimensions. 

class Cylinder():
    def __init__(self, height=1, radius=1): # You can set defualt values if you want. 
        self.height = height
        self.radius = radius

    def volume(self):
        pi = 3.14
      
        return (pi*self.radius**2)*(self.height)
    
    def surface_area(self):
        pi = 3.14
        face = pi*self.radius**2
        return (2*face) + (2*pi*self.radius*self.height)

cylinder1 = Cylinder(10,2)
print(cylinder1.surface_area()) # Also bear in mind that because you are calling methods here, you have to (); otherwise you will just see the data location. 
print(cylinder1.volume())


# Challenge question - 
# For this challenge, create a bank account class that has two attributes:

#  - owner
#  - balance

# And two methods:

#  - deposit
#  - withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner 
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return 'You have deposited £{} to your balance, your new balance is now £{}.'.format(amount, self.balance)

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            return 'You have withdrawn £{} from your balance, your new balance is £{}.'.format(amount, self.balance)
        else: 
            return 'You have insufficent funds to withdraw £{}, you cannot be overdrawn, your current balance is only £{}.'.format(amount, self.balance)

my_account = BankAccount('Andrew McWilliam',1000)
print(my_account.deposit(500))
print(my_account.withdraw(800))
print(my_account.withdraw(100000))