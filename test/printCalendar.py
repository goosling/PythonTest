__author__ = 'joe'
#encoding:utf-8


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_num_of_days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def get_total_num_of_day(year, month):
    days = 0
    for y in range(1800, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365
    for m in range(1, month):
        days += get_num_of_days_in_month(year, m)

    return days

def get_start_day(year, month):
    return (3+get_total_num_of_day(year, month)) % 7

print get_start_day(2033, 12)
