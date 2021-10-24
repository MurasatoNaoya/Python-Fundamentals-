# The datetime module is quite self explanatory, it is a module for measuring time and date...

import datetime

# You can define instances of time using the .time method. 
# You define each step from hour, minute(s), second(s) to even microsecond(s). 
my_time = datetime.time(2,20)

print(my_time)

print(my_time.minute)

print(my_time.hour)

print(my_time.microsecond) # If yoou don't define one of the steps, then the output will be 0 as expected. 

# You can check for the type of the my_time variable you defined using the datetime module, showing we have a time object.  
print(type(my_time))

# Currently all we have is time information, we could also add date information also using a date object or a datetime object.

# You can define the date by year, month and day; or use the today method to get the current date. Following EU standard. 
today = datetime.date.today()

print(today)

# The outputs of the today method are also attributes, meaning you can call them individually. 

print(today.year)

print(today.month)

print(today.day)

# Python also allows you to call on something called 'ctime' a specific format of outputting datetime information. 
# The format being - day (name), month, date (number), time (n:n:n), year. 

print(today.ctime()) # The output will not have a set time, due to us not defining it, we can later. 

# If you want to have a variable that accounts for both time and date, then you have to import an object called datetime. 
# This is not the module that you are working with, but an imported object of the same name. 

from datetime import datetime

my_datetime = datetime(2021,12,25,0,0,1)

print(my_datetime)

# If you made a mistake and want ed to change one of your attributes, you can use the replace method. 

print(my_datetime.replace(year=2022)) # This does not happen in place, meaning it doesn't alter the original variable. 

# You can reassign the variable to do so. 

my_new_datetime = my_datetime.replace(year=2022) 
print( my_new_datetime)

# A common use case of datetime or date objects is simple arithmatic. 
# Finding out how long people were on your website for example. 

# Firstly, for date objects. 

from datetime import date 
first_date = date.today()
second_date = date(2019,8,21) 

date_diff = first_date - second_date

print(date_diff) 

# You use arithmetic on the dates, you have to be dealing with a DATE OBJECT, not by using a datrtime object with a date method. 

# However, you can also use arithmetic for datetime objects also. 

first_datetime = datetime.today()
second_datetime = datetime(2019,8,21,12,0)

datetime_diff = first_datetime - second_datetime

print(datetime_diff) # You will  get two outputs out now, total days, but also your time in the order of hours, minutes and seconds (and smaller increments of seconds.)

# There are more methods you can apply to this, like the total_seconds method for example. 

print(datetime_diff.total_seconds())

# The simple seconds methods will show you specifically how many seconds they are different, not accouting for hours or minutes. 

print(datetime_diff.seconds) # Be careful not to use brackets for 'seconds'. It is an ATTRIBUTE, not a METHOD FUNCTION CALL like total_seconds. 

