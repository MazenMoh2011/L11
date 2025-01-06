import random
option=["rock", "paper", "scissors"]
user_choice= input("choose rock, paper of scissors: ")
computer_choice= random.choice(option)
print("you choose: ", user_choice)
print("computer chose: ", computer_choice)
if user_choice==computer_choice:
    print("It's a tie!")
elif user_choice=="rock"and computer_choice=="scissors":
    print("rock smash scissors, you win!!")
elif user_choice=="paper"and computer_choice=="rock":
    print("paper covers rock, you win!!")
elif user_choice=="scissors"and computer_choice=="paper":
    print("scissors cut paper, you win!!")
else:
    print("you lost!...")