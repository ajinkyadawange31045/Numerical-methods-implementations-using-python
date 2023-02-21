"""
    f(x) = x^3-x^2-2
f(1)=-2  < 0
f(२) = 2>0

root lies betn the interval (1,2)

s1 ->  a = 1, b=2
    f(a)=-2, f(b)=4

c = af(a)-bf(a)/(f(b)-f(a))

next interval (1.333,2)


"""

def f(x):
    return x**3-x-2
a = int(input("enter your first initial guess : "))
b = int(input("enter your second initial guess : "))
n = int(input("Number of iteration : "))
if f(a)*f(b)>0:
    print("False method fails")
else:
    k = 1
    while(k<=n):
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
        print(f"Root,{c} at iteration {k}")
        k = k+1
    

