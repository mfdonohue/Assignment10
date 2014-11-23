# Donohue, Mark
# CS110 A 53
# Assignment 10

class Employee:

    # Initialize data attributes
    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber

    def setEmployeeName(self, employeeName):
        self.__employeeName = employeeName

    def getEmployeeName(self):
        return self.__employeeName

    def setEmployeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber

    def getEmployeeNumber(self):
        return self.__employeeNumber

    def __str__(self):
        return "Employee Name: " + self.__employeeName + \
               "\nEmployee Number: " + str(self.__employeeNumber)
