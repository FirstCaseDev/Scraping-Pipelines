import datefinder
from datetime import datetime,date,timedelta

url = "https://indiankanoon.org/search/?formInput=doctypes:kolkata%20fromdate:1-1-2021%20todate:%2031-1-2021"
source = url.split("doctypes:")[1].split("%20fromdate:")[0]
#f_date = url.split("fromdate:")[1].split("%20todate")[0]
f_date = "01-01-2021"
t_date = url[::-1].split("02%")[0][::-1]
for i in range(30):
    date = datetime.strptime(f_date,'%d-%m-%Y')
    startdate = date
    nextdate = startdate + timedelta(days=1)
    f_date = date.strftime("%d-%m-%Y")
    t_date = nextdate.strftime("%d-%m-%Y")
    print(f_date)
    print(t_date)  
         
    nextdate = startdate + timedelta(days=2)    
    t_date = nextdate.strftime("%d-%m-%Y")
    f_date = t_date 
