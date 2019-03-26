"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
d = 7
m = 1
y = 1900
c = 0
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while y <= 2000:
    if y >= 1901 and d == 1:
        c += 1
    #Upsate of the date
    days_in_month = months[m - 1] + (((y % 4 == 0) if y % 100 else (y % 400 == 0)) if m == 2 else 0)
    d += 7
    if d > days_in_month:
        d = d - days_in_month
        m += 1
        if m > 12:
            m = 1
            y += 1

print(c)
