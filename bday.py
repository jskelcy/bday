import sys
from datetime import date

def bday(birthday):
    birth_year = int(birthday[2])

    whole_years = get_whole_years(birth_year)
    partial_years = get_partial_years(birthday)
    print whole_years + partial_years

def get_whole_years(birth_year):
    # your first whole calendar year is your second year of life
    this_year = int(date.today().year)
    # how many calendar years have you been alive
    calendar_age = (this_year - birth_year) - 1
    # what was the first full calendar year you were alive
    first_whole_year = this_year - calendar_age

    total_days = 0
    for year in range(first_whole_year, this_year):
        if is_leap_year(year):
            total_days = total_days + 366
        else :
            total_days = total_days + 365

    return total_days

def is_leap_year(year):
    if (year % 100) == 0:
            # century years that are divs by 400 are leap years
            if (year % 400) == 0:
                return True
    elif (year % 4) == 0:
        # normal years that are divs by 4 are leap years
        return True
    else:
        # da rest of da years
        return False

def get_partial_years(birthday):
    #the month mapping is zero indexed
    birth_month = int(birthday[0]) -1
    birth_day = int(birthday[1])
    birth_year = int(birthday[2])

    month_to_day_map = [
        31,
        29 if is_leap_year(birth_year) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

    #get partial month
    partial_birth_month = (month_to_day_map[birth_month] - birth_day) + 1 
    partial_current_month = int(date.today().day)



    #for the year you are born you need to count days in that year after
    #the day you were born
    birth_year_months = 0
    for current_month in range((birth_month + 1), 12):
        birth_year_months = birth_year_months + month_to_day_map[current_month]

    #for the current year you need to count number of days in the year so far
    current_year_months = 0
    for current_month in range(0, (date.today().month - 1)):
        current_year_months = current_year_months + month_to_day_map[current_month]

    #because you are alive today
    return partial_birth_month + partial_current_month + birth_year_months + current_year_months


if __name__ == "__main__":
    birthdayString = sys.argv[1]
    birthdayArray = birthdayString.split('/')
    bday(birthdayArray)
