import random
number = random.randint(1,100)
print("Welcome to number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if level == "easy":
  attempts = 10
  print(f"you have {attempts} attempts to guess the number.")
  
elif level == "hard":
  attempts = 5  
  print(f"you have {attempts} attempts to guess the number.")

game_end = True
while(game_end):
  guess = int(input("make a guess: "))
  
  if guess > number:
    print("Too high")
    attempts-=1
    print(f"you have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
      game_end = False
      print("you have run out of guess, you lose!")
      print("The answer was {number}")
  elif guess < number:
    print("Too low")
    attempts-=1
    print(f"you have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
      game_end = False
      print("you have run out of guess, you lose!")
      print("The answer was {number}")
  elif guess == number:
    print(f"You got it! The answer was {number}")
    game_end = False
     
    