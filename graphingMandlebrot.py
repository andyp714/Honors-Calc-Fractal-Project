from complexNumber import complexNumber
import matplotlib.pyplot as plt
import numpy as np

def main():
    maxIterations = 100
    pixelDensity = 1
    realValues = np.linspace(-5,5, 10 * pixelDensity)
    imaginaryValues =  np.linspace(-5,5, 10 * pixelDensity)


    realPoints = []
    imagPoints = []
    for i in realValues:
          for j in imaginaryValues:
            converge = True
            z = complexNumber([0,0])
            c = complexNumber([i,j])
            for k in range(maxIterations):
                z = mandleFunc(z,c)
                if z.distance > 10:
                    converge = False
                    print('broke')
                    break
            if converge == True:
                print(i,j)
                realPoints.append(i)
                imagPoints.append(j)

    plt.scatter(realPoints,imagPoints)
    plt.show()
              

           
    


def convergeCheck(z,c):
        return (z*z) + c



if __name__ == "__main__":
        main()