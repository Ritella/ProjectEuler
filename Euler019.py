# You are given the following information,
# but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

reg_year_days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_days_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# your starting dating is 1 Jan 1900 so begin with that and remove after
month_lengths = []
for year in range(1900, 2001, 1):

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_month = leap_year_days_month
    else:
        days_month = reg_year_days_month

    month_lengths.extend(days_month)

dates = []
for month_length in month_lengths:
    dates.extend([i for i in range(1, month_length + 1)])

# 1900 is not a leap year so to start with 1901, we need
start_idx = sum(reg_year_days_month)

sundays_with_1 = [1 for i in range(start_idx, len(dates)) \
                    if (i + 1) % 7 == 0 and dates[i] == 1]

print(sum(sundays_with_1))


# NOTE: pay attention to month_lengths.extend(days_month) method for
# adding a list to a list
# could also have done calendar_dates += days_month
# importantly, can't use append neatly
# PAY ATTENTION to dates.extend.
# ALSO, extremely important. You cannot just add a range as a list
# Python returns a range, so you need to recast as a list using
# list() or item by item list comprehension
# also, look at how i wrote sundays_with_1 and avoided almost making an
# indexing mistake
