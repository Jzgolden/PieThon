
from datetime import date
from datetime import time
from datetime import datetime

today = date.today()

print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)

# ----------------------------------------

a = time()
print(a)

b = time(11, 23, 45)
print(b)

c = time(hour = 11, minute = 23, second = 45)
print(c)

d = time(9, 43, 5, 334556)
print(d.minute)

e = date 

# ----------------------------------------

a = datetime(2023, 6, 29, 10, 4, 55, 234532)
print(a)


t1 = date(2018, 7, 12)
t2 = date(year = 2017, month = 8, day = 21)

t3 = t2 - t1
print("t3 = ", t3)

t4 = datetime(2018, 6, 19, 10, 15, 23)
t5 = datetime(year = 2020, month = 5, day = 1, hour = 9, minute = 55, second = 9)

t6 = t5 - t4
print("t6 total seconds = ", t6.total_seconds())

print(t6 - t3)

# ----------------------------------------

import pytz

local = datetime.now()
print("Local: ", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY: ", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_Ch = pytz.timezone('America/Chicago')
datetime_Ch = datetime.now(tz_Ch)
print("MN: ", datetime_Ch.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London: ", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# ----------------------------------------
