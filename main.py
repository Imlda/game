import random

list = ["Rock", "Paper", "Scissors"]
user = input("Choose Rock, Paper, or Scissors: ")
com = random.choice(list)
 
print("You chose: ", user)
print("Computer chose: ", com)

if user == com:
    print("It's a tie!")
elif user == "Rock" and com == "Scissors":
    print("You win!")
elif user == "Paper" and com == "Rock":
    print("You win!")
elif user == "Scissors" and com == "Paper":
    print("You win!")
else:
    print("Computer wins!")