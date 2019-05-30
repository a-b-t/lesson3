from datetime import date, datetime, timedelta
import locale


dt_now = datetime.now()
delta = timedelta(days=1)
yesterday = dt_now - delta
one_month_ago = dt_now.replace(month=dt_now.month-1)
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
print(f"Сегодня {dt_now.strftime('%A %d %B %Y')}")
print(f"Вчера {yesterday.strftime('%A %d %B %Y')}")
print(f"Месяц назад {one_month_ago.strftime('%A %d %B %Y')}")



date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)