'''
1 for snake
-1 for water
0 for gun

'''


import random

dict = {
    "s":1,
    "w":-1,
    "g":0
}

# direct dict bata random values access garnu mildaina so paila hamiley list so hamiley paila list maw convert garcham
list = list(dict.values())
computer = random.choice(list)

# user ko value
yourStr = input("Enter s for snake, w for water, g for gun: ")

you = dict[yourStr]

# logic

if (you == 1 and computer == -1):
    print("You Win")
elif (you == -1 and computer == 1):
    print(f"Computer is {computer} and you are {you}")
    print("You Lose")
elif(you == computer):
    print("Draw")
else:
    print("DOESNOT MATCHES ANY COMBINATIONS")