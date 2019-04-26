age=int(input("What is your age?: "))
def age_to_time(year):
    days=(year*365)+(year/4)#to account for leap years
    hours=days*24
    minutes=hours*60
    seconds=minutes*60
    times ={"days":days, "hours":hours,"minutes":minutes,"seconds":seconds}
    return times

print(age_to_time(age))