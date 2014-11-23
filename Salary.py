# Donohue, Mark
# CS110 A 53
# Assignment 10

from Employee import*

class Salary(Employee):

    def __init__(self, employeeName, employeeNumber, salary):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__salary = salary

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def __str__(self):
        return "Salary: " + str(self.__salary) + \
               "\n" + Employee.__str__(self)
