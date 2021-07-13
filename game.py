print("Rock, Paper, Scissors, Shoot!")

# ASK FOR A USER INPUT
# VALIDATE USE INPUT
# GENERATE A COMPUTER CHOICE
# DETERMINE THE WINNER


x = input("Please choose one of 'rock', 'paper', 'scissors'")
print(x)

x = x.lower()
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

#Winning game

if (x == c):
    print("It's a TIE")
elif (x =="rock" and c =="scissors"):
    print("You Won! Good job! Computer Loses")
elif (x =="scissors" and c =="paper"):
    print("You Won! Good job! Computer Loses")
elif (x =="paper" and c =="rock"):
    print("You Won! Good job! Computer Loses")
elif (x =="scissors" and c =="rock"):
    print("You Lose! Dun dun dun! Computer Won")
elif (x =="paper" and c =="scissors"):
    print("You Lose! Dun dun dun! Computer Won")
elif (x =="rock" and c =="paper"):
    print("You Lose! Dun dun dun! Computer Won")













