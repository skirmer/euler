# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import numpy as np
import pandas as pd

# Set up months
months = pd.DataFrame({'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 'days': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]})

# Set up years
years = np.arange(1900,2001)
leaps = pd.DataFrame({'year':years})

# leaps including century edge cases
leaps['leap'] = np.where(((leaps['year'] % 4 == 0) & (leaps['year'] % 100 != 0)) | ((leaps['year'] % 100 == 0) & (leaps['year'] % 400 == 0) & (leaps['year'] % 4 == 0)), True, False)

# Expand out our months to years and add the leaps
expand_months=pd.DataFrame()
for index, row in leaps.iterrows():
    thisyr = months.copy()
    thisyr['year'] = row['year']
    thisyr['leap'] = row['leap']
    expand_months = expand_months.append(thisyr,ignore_index=True)

mask = (expand_months.leap == True) & (expand_months.month == 'Feb')
expand_months.loc[mask, 'days'] = 29

# Now we have the calendar laid out in dataframe.
# what's next?
# first day of first month is Monday
# sixth day of first month is Sunday

week1 = np.arange(1,8)
