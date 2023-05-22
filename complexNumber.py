import numpy as np

class complexNumber():
    def __init__(self, coefficientArray):
        self.realValue = coefficientArray[0]
        self.imaginaryValue = coefficientArray[1]
        self.valueList = coefficientArray
        self.distance = round(((self.realValue ** 2) + (self.imaginaryValue**2)) ** 0.5,6)
    
    def __add__(self, otherComplex):
        return complexNumber([self.realValue + otherComplex.realValue, self.imaginaryValue + otherComplex.imaginaryValue])
    
    def printComplex(self):
        print(str(self.realValue) + ' + ' + str(self.imaginaryValue) + 'i')

    def __mul__(self, otherComplex):
        return complexNumber([(self.realValue * otherComplex.realValue) - (self.imaginaryValue * otherComplex.imaginaryValue), (self.realValue * otherComplex.imaginaryValue) + (self.imaginaryValue * otherComplex.realValue)])


