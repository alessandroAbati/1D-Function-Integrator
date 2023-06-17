#PYTHON FUNCTION INTEGRATOR
'''
Simple pyhton class of Integrator which numerically integrates a given function f(x). 
'''

import numpy as np
import math

class Integrator:
    def __init__(self, f, xMin, xMax, N):
        self.f = f #function to integrate
        self.xMin = xMin #minimum value
        self.xMax = xMax #mazimum value
        self.N = N #number of intervals for integration
        self.Dx = (self.xMax-self.xMin)/self.N #step of integration
        self.result = 0 #result of the integration
            
    def integrate(self):
        for i in range(self.N-1):
            x = self.xMin + i*self.Dx #definition of x_i for each step of the integration
            self.result += self.f(x)*self.Dx #update the result
        
    def show(self):
        print(round(self.result,5))

def f(x): #definition of function to integrate
    return (x**2)*np.exp(-x)*np.sin(x)

def main():
    examp = Integrator(f,1,3,200000)
    examp.integrate()
    examp.show()

if __name__=="__main__":
    main()