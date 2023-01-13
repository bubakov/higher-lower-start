import random
import art
import game_data
from replit import clear

# TO DO 
# Pretty format data
def format_data(account):
  """Format the account data into printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Use if statement to check if user is correct."""
  # if a_followers is greater then b and guess is a, return True
  # if b_followers is greater than a and guess is b, return True
  # oposite it returns False
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
  
# Display art
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(game_data.data)

# Repeat game
while game_should_continue:
# Generate random data from game_data
  account_a = account_b
  account_b = random.choice(game_data.data)  
  while account_a == account_b:
    account_b = random.choice(game_data.data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(art.vs)
  print(f"Against B: {format_data(account_b)}.")
  
  # Ask User
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is wrong.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  # Clear screen
  clear()
  print(art.logo)
  
  # Feedback to user. # Track score.
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")    
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")





