"""
f(x) = x^3-x^2-2
f(1)=-2  < 0
f(२) = 2>0
x0 = 1.5

x1 = x0 - f(x0)/f'(x0)
"""

def f(x):
    return x**3 -x**2 -2
def df(x):
    return 3*x**2 - 2*x

a = float(input("Initial guess = "))
n = int(input("Number Iteration = "))
k = 1
while(k<=n):
    r = a-f(a)/df(a)
    print(f'roots r {r} at iteration {k}')
    k = k+1
    a = r
