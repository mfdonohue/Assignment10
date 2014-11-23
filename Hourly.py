# Donohue, Mark
# CS110 A 53
# Assignment 10

from Employee import*

HOURLY_WAGE = 10.00
TIME_AND_HALF = 15.00

class Hourly(Employee):

    def __init__(self, employeeName, employeeNumber, hours):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__hours = hours

    def setHours(self, hours):
        self.__hours = hours

    def getHours(self):
        return self.__hours

    def calculatePay(self, hours):
        if self.__hours <= 40:
            pay = self.__hours * HOURLY_WAGE
        else:
            pay = self.__hours * TIME_AND_HALF
        return pay

    def __str__(self):
        return "Hours worked this week: " + str(self.__hours) + \
               "\n" + Employee.__str__(self)
