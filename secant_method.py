x1 = int(input("enter the value of X0 : "))
x2 = int(input("enter the value of X1 : "))
error = float(input("enter the value of error : "))

num_iter = int(input("Define maximum number of iterations required : "))

def funct(x):
    f_x = x**3 -x**2 + x -5
    return f_x
    
for i in range(0,num_iter,1):
    fx1 = funct(x1)
    fx2 = funct(x2)
    print(f"{i}, x value is {x2} = {fx2}")
    
    if abs(fx2) < error:
        break
    x3 = (x1*fx2 - x2*fx1)/(fx2-fx1)
    x1 = x2
    x2 = x3

print(f"your zero is located at: [{x2},{fx2}] ")