import datetime
my_time=datetime.time(2,30)
print(my_time)
print(my_time.hour)
today=datetime.date.today()
print(today)
print(today.ctime())
from datetime import datetime
mydatetime=datetime(2025,9,10,21,56,32,99)
print(mydatetime)
mydatetime=mydatetime.replace(year=2026)
print(mydatetime)
#Difference between dates
from datetime import date
date1=date(2022,8,26)
date2=date(2025,8,26)
result=date2-date1
print(result.days)
#Difference between times
from datetime import datetime
date1=datetime(2022,8,26,20,38,0)
date2=datetime(2025,8,26,19,24,10)
result=date2-date1
print(result)