import re
import datetime

format1 = "71/70/2020"      #mm/dd/yyyy
format2 = "2001/13/06"      #yyyy/mm/dd
format3 = "06-Dec-2001"     #dd-mm-yyyy
format4 = "11001"           #yyddd
format5 = "12 06 2001"      #mm dd yyyy
m = re.search('(\d{1,2}?|\d{4})(/|-| )(\d{1,2}?|\S{3})(/|-| )(\d{4}|\d{1,2})|(\d{5})', format1)

monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

date = 0
month = 0
year = 0
juliandate = 0
calendardate = ""

if m.group(1):
    if int(m.group(1)) > 31:
        year = m.group(1)
        if m.group(3) and m.group(5) and int(m.group(3)) <= 12 and int(m.group(3)) >= 0 and int(m.group(5)) >= 0 and int(m.group(5)) <= 31:
            month = m.group(3)
            date = m.group(5)
        else:
            print("Format Error!")
    else:
        month = m.group(1)
        if m.group(3) not in monthlist:
            date = m.group(3)
if m.group(3):
    if m.group(3) in monthlist:
        month = m.group(3)
        date = m.group(1)
if m.group(5):
    if int(m.group(5)) > 31:
        year = m.group(5)
if m.group(6):
    juliandate = int(m.group(6))
    calendardate = str(datetime.datetime.strptime(str(juliandate), '%y%j').date())
    calendardate = calendardate.split("-")
    year = calendardate[0]
    month = calendardate[1]
    date = calendardate[2]

print("The year of this date is \t" + year)
print("The month of this date is \t" + month)
print("The date of this date is \t" + date)