from complexNumber import complexNumber
import matplotlib.pyplot as plt
import numpy as np

def main():
    maxIterations = 20
    pixelDensity = 40
    realValues = np.linspace(-5,5, 10 * pixelDensity)
    imaginaryValues =  np.linspace(-5,5, 10 * pixelDensity)

    print(convergeCheck(complexNumber([0,0]), complexNumber([0,0]), 100))


    realPoints = []
    imagPoints = []
    for i in realValues:
          for j in imaginaryValues:
            z = complexNumber([0,0])
            c = complexNumber([i,j])
            if convergeCheck(z,c, maxIterations) == True:
                realPoints.append(i)
                imagPoints.append(j)

    plt.scatter(realPoints,imagPoints)
    plt.show()
              

           
    


def convergeCheck(z,c, maxIterations):
        for i in range(maxIterations):
            z = (z*z) + c
            if z.distance > 10:
                return False
                break
        return True




if __name__ == "__main__":
        main()