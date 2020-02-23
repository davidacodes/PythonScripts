from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

timetype = type(t)
days = t.days
seconds = t.seconds

print(timetype)
print(days)
print(seconds)

hours = t.seconds / 60 /60
print(hours)

eta = timedelta(hours=6)
today = datetime.today()

print(today)
print(eta)

print(today + eta)