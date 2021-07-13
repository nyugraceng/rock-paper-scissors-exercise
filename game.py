print("Rock, Paper, Scissors, Shoot!")

# ASK FOR A USER INPUT
# VALIDATE USE INPUT
# GENERATE A COMPUTER CHOICE
# DETERMINE THE WINNER

x = input("Please choose one of 'rock', 'paper', 'scissors'")
print(x)

if (x == "rock") or (x == "paper") or (x =="scissors"):
    print("VALID")  
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

#from class stackoverflow source

import random

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))


print("USER CHOSE: ", x)

valid_options = ["rock", "paper", "scissors"] #list

c = random.choice(valid_options)

print(random.choice(valid_options))

print("COMPUTER CHOSE: ",c)









