def f(x):
    return x*x*x-x-4
def binary_section(a,b):
    if f(a)*f(b)>0:
        print("the root doesn't lie inside the given values")
    else:
        n = 0
        while n<=15:
            c = (a+b)/2
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
                n = n+1
            print(n)
            print("roots of the given equation is ",c)
                




a = int(input("Enter the initial value : "))
b = int(input("Enter the Final value : "))
binary_section(a, b)