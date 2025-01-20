# syntax
# def fun():
#     print("Hello")


def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)
    

 
a = factorial(5)
print(a)    


factorial = 1
e = int(input("Enter a number: "))
for i in range (1,e+1):
    factorial = factorial * i
    
print(f"The factorial of {e} i {factorial}")   
    