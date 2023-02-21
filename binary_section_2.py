def binary_section(func,a,b,error_accept):
    def f(x):
        x = eval(func)
        return x
    
    error = abs(b-a)
    
    n = 0
    while error_accept < error:
        c = (a+b)/2
        if f(a)*f(b)>=0:
            print("no roots are present so bisection method will not work")
            quit()
        elif f(a)*f(c)<0:
            b = c   
            error = abs(b-a)
        elif f(b)*f(c)<0:
            a = c
            error = abs(b-a)
        else:
            print("something went wrong")
            quit()
        n += 1
        print(n)
        print(f'the lower boundary a is {a} and the upper boundary b is  {b}')
    print("_______________________________________________________________")
    print(f'the error is {error}')
    print(f'the lower boundary a is {a} and the upper boundary b is  {b}')

# a = int(input("Enter the initial value : "))
# b = int(input("Enter the Final value : "))
# error_accept = (input("Enter the error value: "))
# binary_section("x**3-x-4", 0, 1, error_accept)            
binary_section("x**3-x-4", 1, 2, 0.001)            
