from datetime import datetime
from datetime import date

today = datetime.today()
type(today)
print(today)

todaydate = date.today()
type(todaydate)
print(todaydate)

todaydate.month
todaydate.day
todaydate.year

christmas = date(2020, 12, 25)
print((christmas - todaydate).days)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " days until Christmas!")
else:
    print("It's Christmas!")