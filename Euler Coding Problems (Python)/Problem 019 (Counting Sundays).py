import datetime

def count_sundays_on_first_of_month(start_year, end_year):
    """
    Count the number of Sundays that fall on the first of the month between the given years.
    """
    count = 0

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Create a datetime object for the first day of the month
            date = datetime.date(year, month, 1)

            # Check if the day is a Sunday
            if date.weekday() == 6:
                count += 1

    return count


sundays_count = count_sundays_on_first_of_month(1901, 2000)
print(sundays_count)
