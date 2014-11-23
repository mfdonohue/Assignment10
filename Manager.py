# Donohue, Mark
# CS110 A 53
# Assignment 10

from Salary import*

class Manager(Salary):

    def __init__(self, employeeName, employeeNumber, salary, bonus):
        Salary.__init__(self, employeeName, employeeNumber, salary)
        self.__bonus = bonus

    def setBonus(self, bonus):
        self.__bonus = bonus

    def getBonus(self):
        return self.__bonus

    def __str__(self):
        return "Bonus: " + str(self.__bonus) + \
               "\n" + Salary.__str__(self)
