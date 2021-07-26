from datetime import datetime as dt
print(dt.now())          # print time that is on the system

import pytz
tz=pytz.timezone('Singapore')
print(dt.now(tz))       #time at singapore

#print(pytz.all_timezones)        #print all time zones
 

import calendar

print(calendar.weekday(1999,6,8))            #0-6 mon-sun


''' Check for valid date  and find day------------------------'''
import calendar
def get_day(x):
     list_of_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
     return list_of_days[x]
     
def check_leap(y):
     if y%100==0:
          if y%400==0:
               return True
     if y%4==0:
          return True
     return False

def valid_date(dt,m,y,l):
     if dt<1:
          return False
     if l:
          if m==2:
               if dt<30:
                    return True
               else:
                    return False
     else:
          if m==2:
               if dt<29:
                    return True
               else:
                    return False
     if m<8:
          if m%2==1:
               if dt<32:
                    return True
               else:
                    return False
          else:
               if dt<31:
                    return True
               else:
                    return False
     if m>=8:
          if m%2==0:
               if dt<32:
                    return True
               else:
                    return False
          else:
               if dt<31:
                    return True
               else:
                    return False

while(1):
     year=int(input("Enter year after 1967 : "))
     if year<1967:
              print("Enter year in the range")
     else:
          break

while(1):
     month=int(input("Enter month : "))
     if month<1 and month>12:
              print("Enter valid month")
     else:
          break
leap_year=check_leap(year)
while(1):
     date=int(input("Enter date : "))
     if (valid_date(date,month,year,leap_year)==False):
              print("Enter valid date")
     else:
          break

day_index=calendar.weekday(year,month,date)
day=get_day(day_index)
print(date,'/',month,'/',year,'falls on',day)

''' ---------------------------------------------------   '''


          
