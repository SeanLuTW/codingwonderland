"""
1185. Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

"""
from datetime import datetime,date 

day = 31
month = 8
year = 2019
#idea from discussion 
"""
runtime:16 ms
"""
print (date(year, month, day).strftime("%A"))

"""
runtime:24 ms
"""
from datetime import date 
d = date(year,month,day)
print(d.strftime("%A"))# Formatting datetime

#testfunction
print(datetime.now())
