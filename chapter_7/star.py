n =  int(input("Enter a number: "))

# for i in range (1,n):
#     print("*"*i)
    
for i in range (1,n+1):
       print(" "* (n-i),end="") 
       print( "*"*(2*i-1),end="")
       print("\n")
       