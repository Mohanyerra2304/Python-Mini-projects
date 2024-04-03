from game_data import data
import random
import os

def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"
account_b = random.choice(data)
score = 0
game_should_continue = True
while game_should_continue:
    #generate a random account from the data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
      account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print("vs")
    print(f"Aganist B: {format_data(account_b)}")
    print('-----------------------------------------')
    
    def check_answer(account,a_followers,b_followers):
      if a_followers > b_followers:
        if guess == 'A':
          return True
        else:
          return False
      elif b_followers > a_followers:
        if guess == 'B':
          return True
        else:
          return False
    
    guess = input("who ha more followers? Type 'A' or 'B': ").upper()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
  
    os.system('clear')
    if is_correct:
      score+=1
      print(f"You are correct. Your current score is {score}.") 
    else:
      game_should_continue = False
      print(f"Sorry that was wrong!!!. Final score : {score}.")
      
    