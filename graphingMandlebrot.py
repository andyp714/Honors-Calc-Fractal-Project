from complexNumber import complexNumber
import matplotlib.pyplot as plt
import numpy as np

def main():
    a = complexNumber([1,2])
    b = complexNumber([-2,2])
    c = a*a
    print(c.valueList)
    c.printComplex()

if __name__ == "__main__":
        main()