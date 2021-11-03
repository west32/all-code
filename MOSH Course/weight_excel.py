import openpyxl as xl
from openpyxl.chart import BarChart, Reference,LineChart
from datetime import date
from openpyxl.chart.axis import DateAxis

# cll = sheet['a1']
# cllone=sheet.cll(1,1)
work_book=xl.load_workbook("weight2.xlsx")
sheet = work_book['Sheet1']



date_cell = sheet.cell(sheet.max_row + 1, 1)
weight_cell = sheet.cell(sheet.max_row, 2)
today_date=input("eneter today date:")
today_weight= float(input("eneter today weight"))
date_cell.value=today_date
weight_cell.value=today_weight

weights_and_dates= Reference(sheet,
          min_row=2,
          max_row=sheet.max_row,
          min_col=2,
          max_col=2)

chart = LineChart()
chart.title= "Weight drop"
chart.add_data(weights_and_dates)
sheet.add_chart(chart,'d2')



work_book.save("weight3.xlsx")
