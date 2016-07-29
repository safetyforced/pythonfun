def zeller_it(month, day, year):
    if month < 3:
        month = month + 12
        year = year - 1

    k = day
    m = month - 2
    d = year % 100
    c = year / 100


    f = k + ((13*m - 1)/5) + d + (d/4) + (c/4) - 2*c
    day_of_week = f % 7
    return day_of_week

def convert(day):
    if day == 1:
        print "Monday"
    elif day == 2:
        print "Tuesday"
    elif day == 3:
        print "Wednesday"
    elif day == 4:
        print "Thursday"
    elif day == 5:
        print "Friday"
    elif day == 6:
        print "Saturday"
    elif day == 7:
        print "Sunday"

convert(zeller_it(7, 15, 2016))
convert(zeller_it(6, 15, 1923))
convert(zeller_it(9, 1, 1847))
convert(zeller_it(3, 17, 2021))
convert(zeller_it(12, 7, 1977))
convert(zeller_it(2, 28, 1901))
convert(zeller_it(6, 17, 1777))
convert(zeller_it(8, 5, 1924))
convert(zeller_it(6, 3, 1754))
