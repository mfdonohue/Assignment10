# Donohue, Mark
# CS110 A53
# Assignment 10

from Manager import*
from Hourly import*

def getSalaryInfo():
    goAgain = 'y'
    while goAgain == 'y':
        try:
            salary = float(input("Enter your salary: "))
            salaryEmployee = Salary("David Hamel", "16", salary)
            print(salaryEmployee)
            goAgain = 'n'

        except ValueError:
            print("You didn't enter a valid number.")

        except:
            print("An error occurred.")
            goAgain = 'n'

def getManager():

    BONUS = .1
    goAgain = 'y'
    while goAgain == 'y':
        try:
            salary = float(input("Enter your salary: "))
            bonus = salary * BONUS
            managerSalary = Manager("Mannan Kasliwal", "29", salary, bonus)
            print(managerSalary)
            goAgain = 'n'

        except ValueError:
            print("You didn't enter a valid number.")

        except:
            print("An error occurred.")
            goAgain = 'n'

def getHourlyInfo(hours):
    goAgain = 'y'
    while goAgain == 'y':
        try:       
            hourlyEmployee = Hourly("Mark Donohue", "12", hours)
            print(hourlyEmployee)
            print("Your pay is", hourlyEmployee.calculatePay(hours))
            goAgain = 'n'

        except:
            print("An error occurred.")
            goAgain = 'n'

def hourlyOrSalary():
    
    try:
        goAgain = 'y'
        while goAgain == 'y':
            try:
                hours = float(input("How many hours do you work in a week? "))
                goAgain = 'n'

            except ValueError:
                print("You entered incorrect data.")

            except:
                print("An error occurred.")
                goAgain = 'n'
                
            status = input("Enter 'Hourly' or 'Salary' here: ")

            if status.lower() == "hourly":
                getHourlyInfo(hours)
                goAgain = 'n'

            elif status.lower() == "salary":
                ifManager = input("Are you a manager? ('yes'/'no'): ")
                if ifManager.lower() == "yes":
                    getManager()
                    goAgain = 'n'

                elif ifManager.lower() == "no":
                    getSalaryInfo()
                    goAgain = 'n'

                else:
                    print("You entered invalid input.")
                    goAgain =  'y'

            else:
                print("That was an invalid input.")
                goAgain = 'y'

    except:
        print("An error occurred.")

def main():
    hourlyOrSalary()

main()
