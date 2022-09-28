"""Python Program to Display Calendar"""

import calendar, datetime

#this gets the actual date (with date and hour, min , seconds ...)
full_date= datetime.datetime.now()
#we parse it into date format by elem.date()
date = full_date.date()

#once we have the date we get year & month variables
year= date.year
month = date.month

#prmonth prints the month by give it with year
calendar.prmonth(year,month)