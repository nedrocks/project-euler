
DAY_LENGTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def _is_leap_year(year):
    return not year % 4 and (year % 100 or not year % 400)

def _get_month_length(year, month):
    if month == 1:
        return DAY_LENGTH[1] + (1 if _is_leap_year(year) else 0)
    return DAY_LENGTH[month]

def main():
    year = 1901
    month = 0
    # 0 is Monday
    day = 1
    count = 0
    while year < 2001:
        while month < 12:
            day += _get_month_length(year, month)
            day %= 7
            if day == 6:
                count += 1
            month += 1
        month = 0
        year += 1
    print count

if __name__ == '__main__':
    main()