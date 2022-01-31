from datetime import datetime

def set_day():
    """
    Get a valid day
    """
    while True:
        day = input("Enter the day: ").strip().replace(" ","")
        try:
            int(day)
        except:
            print("It's not a number!")
        else:
            if not int(day) in range(1,32):
                print("Day out of range!")
                continue
            return day

def set_month():
    """
    Get a valid month
    """
    while True:
        month = input("Enter the month: ").strip().replace(" ","")
        try:
            int(month)
        except:
            print("It's not a number!")
        else:
            if not int(month) in range(1,13):
                print("Month out of range!")
                continue
            return month

def set_year():
    """
    Get a valid year
    """
    while True:
        year = input("Enter the year: ").strip().replace(" ","")
        try:
            int(year)
        except:
            print("It's not a number!")
        else:
            if not int(year) in range(1,10000):
                print("Year out of range!")
                continue
            return year

def change_day_month():
    """
    Option to change date
    """
    decision = 0
    while True:
        decision = input("Wich one would you like to change? 0 = day | 1 = month: ").strip().replace(" ","").lower()
        try:
            int(decision)
        except:
            print("It's not a number!")
            continue
        else:
            if not int(decision) in range(0,2):
                print("Wrong option!")
                continue
            return int(decision)

def check_correct_date_decision(day, month, year):
    """
    checking answer
    """
    while True:
        check = input("Your date is: "+year+"-"+month+"-"+day+".Is your date correct? y/n: ").lower().strip()
        if not check in ["y","n"]:
            print("Worng option!")
            continue
        return check

def set_date():
    """
    Checking date and returning it
    """
    setDate = True
    while True:
        if setDate:
            print("Enter a date.")
            dayInput = setDay()
            monthInput = setMonth()
            yearInput = setYear()
            setDate = False
        try:
            datetime(year=int(yearInput),month=int(monthInput),day=int(dayInput))
        except:
            pass
            print(f"Month and day incompatible! Month: {monthInput} Day: {dayInput}")
            decision = changeDayOrMonth()
            if decision == 0:
                dayInput = setDay()
                continue
            monthInput = setMonth()
        else:
            check = checkCorrectDateDecision(dayInput, monthInput, yearInput)
            if check == "n":
                setDate = True
                continue
            return datetime.strptime(yearInput+"-"+monthInput+"-"+dayInput, '%Y-%m-%d')
