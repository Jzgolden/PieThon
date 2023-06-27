# Create list of choice
# Make AI pick random choice
# Ask user to input choice
# Conditional statements:
# If same print tie, else print winner
# If end, print final scores

import random
choice = ["Rock", "Paper", "scissors"]
player = False
aiScore = 0
userScore = 0

while True:
  player = input("Do you choose Rock, Paper or Scissors? ").upper()
  ai = random.choice(choice).upper()
  ## Conditions of Rock, Paper, Scissors 
  if player == ai:
    print("Tie!")
  elif player == "ROCK":
    if ai == "PAPER":
      print("You lose!", ai, "covers", player)
      aiScore+=1
    else:
      print("You win!", player, "smashes", ai)
      userScore+=1
  elif player == "PAPER":
    if ai == "SCISSORS":
      print("You lose!", ai, "cut", player)
      aiScore+=1
    else:
      print("You win!", player, "covers", ai)
      userScore+=1
  elif player == "SCISSORS":
    if ai == "ROCK":
      print("You lose ", ai, "smashes ", player)
      aiScore+=1
    else:
      print("You win! ", player, "cut", ai)
      userScore+=1
  elif player == "END":
    print("Final Scores: ")
    print("AI: ", aiScore)
    print("User: ", userScore)