from complexNumber import complexNumber
import matplotlib.pyplot as plt
import numpy as np

def main():
    maxIterations = 20
    pixelDensity = 300
    xmin = -2
    xmax = 1.5
    ymin = -1.5
    ymax = 1.5
    realValues = np.linspace(xmin,xmax, int(abs(xmax-xmin)) * pixelDensity)
    imaginaryValues =  np.linspace(ymin,ymax, int(abs(ymax-ymin)) * pixelDensity)

    realPoints = []
    imagPoints = []
    for i in realValues:
          for j in imaginaryValues:
            z = complexNumber([0,0])
            c = complexNumber([i,j])
            if convergeCheck(z,c, maxIterations) == True:
                realPoints.append(i)
                imagPoints.append(j)

    plt.scatter(realPoints,imagPoints, color='black', marker=',', s=1)
    plt.tight_layout()
    plt.show()
              

           
    


def convergeCheck(z,c, maxIterations):
        for i in range(maxIterations):
            z = (z*z) + c
            if z.distance > 2:
                return False
                break
        return True




if __name__ == "__main__":
        main()