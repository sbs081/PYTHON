'''
Created on 2009-9-9

@author: selfimpr
'''
leap_year_month_days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, \
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
general_year_month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, \
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def days(date):
    date = date.split("/")
    year = int(date[2])
    month = int(date[0])
    day = int(date[1])
    previous_leap_years = year / 4 * 4
    departed_general_years = year % 4 - 1
    departed_months = range(1, month)
    departed_days = 0
    if not year % 4:
        previous_leap_years -= 4
        departed_days = sum([leap_year_month_days[m] \
                         for m in  departed_months], day)
    else:
        departed_days = sum([general_year_month_days[m] \
                         for m in  departed_months], day)
    return previous_leap_years * 365 + 2008 / 4\
            + departed_general_years * 365 + departed_days

def minus(date1, date2):
    return abs(days(date1) - days(date2))

