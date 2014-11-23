# Donohue, Mark
# CS110 A53
# Assignment 10


from Manager import*
from Hourly import*

def hourlyOrSalary():
    while hourlyOrSalary:
        try:
            print("Enter 'Hourly' if you are an hourly employee.")
            print("Enter 'Salary' if you are a salary employee.")
            status = input("Enter here: ")
            if status.lower() == "Hourly":
                getHourlyInfo()

            else:
                getSalaryInfo()

        except ValueError:
            print("Make sure to enter 'Hourly' or 'Salary'.")

def getHourlyInfo():

    hours = float(input("Enter the number of hours worked this week: "))
    return hours
    

def main():
    hourlyOrSalary()
    hourly1 = Hourly("Mark Donohue", "12", hours)
    print(hourly1)
    

main()
