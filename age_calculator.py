from datetime import datetime

def age_calculate(birthdate):
    now = datetime.now()
    #age = today date - birth date
    age = now - birthdate
    
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    hours = age.seconds // 3600
    minutes = (age.seconds % 3600) // 60
    seconds = age.seconds % 60
    
    return years, months, days, hours, minutes, seconds

birthdate = datetime(2001, 04, 8)
years, months, days, hours, minutes, seconds = age_calculate(birthdate)
print(f"Age: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
