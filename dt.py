from datetime import date, datetime
import locale


dt_now = datetime.now()
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
print(dt_now.strftime('%A %d %B %Y'))

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)