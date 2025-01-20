def greatestNumber(a,b,c):
    if (a > b and a > c):
        return (f"{a} is the greatest number")
    elif (b > a and b > c):
        return (f"{b} is the greatest number")
    elif (c > a and c > b):
        return (f"{c} is the greatest number")
    else:
        return ("All numbers are equal or different")
        
a = greatestNumber(10,20,30)

print(a)



def celcius_to_fahrenheit(celcius):
    celcius = celcius * 1.8 + 32
    return celcius

a =round(celcius_to_fahrenheit(188),2)

print(a)



# dont want newline then use end=" "
print("Hello ", end=" ")
print("World")
print("Hello")


# recursive function to find sum of first natural number


# numb = int(input("Enter a number: "))
# total = 0

# def sumOfNumb(numb):
#     if (numb == 0):
#         return 0
#     else:
#         return numb + sumOfNumb(numb-1)
        
    
    
# sum = sumOfNumb(10)       

# print(sum)

#  for global variable

total = 0

def sumOfNumb(numb):
    global total
    if (numb == 0):
        return 0
    else:
        total += sumOfNumb(numb-1)
        return total
        
    
    
sum = sumOfNumb(10)       

print(sum)