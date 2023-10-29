from datetime import date,datetime,timedelta
date1=date(2023,12,1)
date2=date(2023,12,31)
diff=date2-date1
print(diff.days*24*3600+ diff.seconds)
