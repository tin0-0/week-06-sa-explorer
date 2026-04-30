from datetime import datetime, timedelta

now = datetime.now()
print(type(now))

print(now.year, now.month, now.day)

print(now.hour, now.minute, now.second)

birthday = datetime(2000, 1, 15)
print(birthday)
print(now.strftime("%d %B %Y"))

# %d = day of month (01-31)
# %m = month (01-12)
# %B = full month name (January-December)
# %b = abbreviated month name (Jan-Dec)
# %Y = year (4 digits) (2026)
# %y = year (2 digits) (26)
# %H = hour 24-hour (00-23)
# %I = hour 12-hour (01-12)
# %M = minute (00-59)
# %S = second (00-59)
# %A = full weekday name (Monday-Sunday)
# %a = abbreviated weekday name (Mon-Sun)

print(now.strftime("Today is %A the %dth"))

today = datetime.now()
nextweek = today + timedelta(days=7)
yesterday = today - timedelta(days=1)
in_an_hour = today + timedelta(hours=1)


# print(in_an_hour)
# print(nextweek)
# print(yesterday)

print(f"Today:      {today.strftime('%d %B %Y')}")
print(f"Next week:  {nextweek.strftime('%d %B %Y')}")
print(f"Yesterday:  {yesterday.strftime('%d %B %Y')}")
print(f"In an hour: {in_an_hour.strftime('%d %B %Y %H:%M:%S')}")

freedom_day = datetime(2026, 4, 27)
diff = freedom_day - today
print(f"Days until freedom Day:{diff.seconds}")