from datetime import datetime, timedelta, date

#1 Task
now= datetime.now()
new_date=now-timedelta(days=5)
print("Current:", now)
print("Minus 5 days:", new_date)

#2 task
today = date.today()
yesterday= today-timedelta(days=1)
tomorrow =today+timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3 
dt = datetime.now()
dt_no_micro = dt.replace(microsecond=0)
print("With microseconds:", dt)
print("Without microseconds:", dt_no_micro)

#4
d1 = datetime(2026, 2, 20, 10, 0, 0)
d2 = datetime(2026, 2, 24, 15, 30, 0)
diff_seconds = (d2 - d1).total_seconds()
print("Difference in seconds:", diff_seconds)