bday=input("When is your birthday?(YYYY-MM-DD): ")
import time
from datetime import datetime
def birthday_to_time(bday):
    bday=bday.split("-")
    year=int(bday[0])
    month=int(bday[1])
    day=int(bday[2])
    birthday=datetime(year,month,day,0,0).timestamp()
    now=time.time()
    seconds=int(now-birthday)
    minutes=seconds//60
    hours=minutes//60
    days=hours//24
    months=days//30
    age={"months":months,"days":days,"hours":hours,"minutes":minutes}
    return age

print(birthday_to_time(bday))