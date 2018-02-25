from datetime import datetime, timedelta, timezone
# now
now = datetime.now()
print(now)

# datetime to timestamp
specific = datetime(1990, 5, 22, 0, 0, 0)
print(specific)
print(specific.timestamp())

# timestamp to datetime
t = 643302000
print(datetime.fromtimestamp(t))

# timestamp to UTC datetime
print(datetime.utcfromtimestamp(t))

# str to datetime
print(datetime.strptime('2017-5-20 00:00:00', '%Y-%m-%d %H:%M:%S'))

# datetime to str
print(now.strftime('%Y-%m-%d %H:%M:%S'))

# datetime add
print(now + timedelta(hours=10))

# datetime sub
print(now - timedelta(days=1, hours=12))

# timezone
tz_utc_8 = timezone(timedelta(hours=8))
new_now = datetime.now()
print(new_now)
