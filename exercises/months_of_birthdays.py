from bokeh.plotting import figure,show,output_file
from collections import Counter
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
x_categories=[month for month in months.values()]
print (birthdays_dict)
y=[]




c= Counter(dates)
x=[month for month in c]
print(x)

for month in x:
        y.append(c[month])
print(y)
print(c)
#
output_file("plot.html")


f= figure(x_range=x_categories)

f.vbar(x=x,top=y,width=0.5)

# show(f)








