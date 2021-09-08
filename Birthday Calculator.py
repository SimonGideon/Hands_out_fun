import datetime

import django_db.settings
import odbc

current_date = datetime.date.today().strftime('%y-%m-%d')
current_date_1st = current_date.split('-')

b_date = input('Enter birthday in yy-mm-dd format:')
name = input('Name of Birthday Legend?')
b_date = b.date.split('-')

if current_date_1st[1] == b.date[1] and current_date_1st[2]==b.date[2]:
