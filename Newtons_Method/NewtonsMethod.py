from sympy import *

def newtonsMethod(f_str, startPoint):
    #convert function in string from to sympy object
    x = Symbol('x')
    f = sympify(f_str)
    fPrime = f.diff(x)

    xPrev = startPoint
    xNext = 0

    #make f and f  prime functions
    f = lambdify(x, f)
    fPrime = lambdify(x,fPrime)

    while True:
        xNext = xPrev - (f(xPrev)/fPrime(xPrev))
        print(xNext)

        if(getDecDigits(xPrev) == getDecDigits(xNext)):
            return xPrev
            break

        xPrev = xNext
def getDecDigits(n):
    n =  str(round(n,6)).split('.')

    if len(n) != 1:
        return n[1]
    else:
       return 0


if __name__ == "__main__":
    f_str = input("Enter your function in python notation: ")
    startPoint = float(input("Enter your start point: "))
    print(newtonsMethod(f_str, startPoint))
