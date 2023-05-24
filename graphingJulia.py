from complexNumber import complexNumber
import matplotlib.pyplot as plt
import numpy as np

def main():
     pass


def convergeCheck(z,c, maxIterations):
        for i in range(maxIterations):
            z = (z*z) + c
            if z.distance > 2:
                return False
                break
        return True



if __name__ == "__main__":
        main()