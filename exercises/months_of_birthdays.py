
from collections import Counter, namedtuple
import json

with open ("birthdays.json", "r",encoding='utf-8') as bday_file:
    birthdays_dict=json.load(bday_file)
    dates=[]
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    for date in birthdays_dict.values():
        month=date[-2:]
        dates.append(months[month])

c= Counter(dates)
for element in c:
    print(element)

print(c)










