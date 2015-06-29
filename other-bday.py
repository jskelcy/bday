import sys
import datetime

def bday(birthdayArray):
    birth_month = int(birthdayArray[0])
    birth_day = int(birthdayArray[1])
    birth_year = int(birthdayArray[2])
    today = datetime.date.today()

    total_days = 0
    for year in range(birth_year, today.year -1):
        if is_leap_year(year):
            total_days = total_days + 366
        else :
            total_days = total_days + 365

    birthday = datetime.datetime.strptime(str(birth_month) + '/' + str(birth_day) + '/' + str(today.year) , '%m/%d/%Y')
    new_years = datetime.datetime.strptime('1/01/'+ str(today.year) , '%m/%d/%Y')

    if birthday > today:
        #thing
    else:

    print birthday 

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

if __name__ == "__main__":
    birthdayString = sys.argv[1]
    birthdayArray = birthdayString.split('/')
    bday(birthdayArray)
