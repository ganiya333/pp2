from datetime import datetime, timedelta
today= datetime.today()
yesterday= datetime.today() - timedelta(days=1)
tomorrow= datetime.today() + timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)
