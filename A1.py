import random
playing = True
number= str(random.randint(10, 20))
print("I wil generate a random nuber and you will have to guess it.")
print("the game end when you get 1 hero!")
while playing:
    guess=input("give me your best guess: ")
    if number == guess:
        print("you won the game!")
        print("the number was...", number)
        break
    else:
      print("it seems like your guess was wrong please try again!")