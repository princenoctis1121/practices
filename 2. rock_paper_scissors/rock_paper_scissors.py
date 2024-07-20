import random

game = ["rock", "paper", "scissors"]
play = True
input_valid = True

while play:
  while input_valid:
    player = input("Please choose rock, paper or scissors: ")
    if player == "rock" or "paper" or "scissors":
      input_valid = False
    else:
      print("Please choose a valid option.")

  while True:
    
    cpu = random.choice(game)   
    
    if cpu == "rock":
      print("CPU choose rock.")
      if player == "scissors":
        print("You lose!")
        break
      elif player == "paper":
        print("You win!")
        break
      else:
        print("Tie!")
        play = True
        input_valid = True
    
    elif cpu == "paper":
      print("CPU choose paper.")
      if player == "rock":
        print("You lose!")
        break
      elif player == "scissors":
        print("You win!")
        break
      else:
        print("Tie!")
        play = True
        input_valid = True
    
    elif cpu == "scissors":
      print("CPU choose scissors.")
      if player == "paper":
        print("You lose!")
        break
      elif player == "rock":
        print("You win!")
        break
      else:
        print("Tie!")
        play = True
        input_valid = True
  
  play_again = input("Do you wanna play again?(yes/No)")
  if play_again == "yes":
    play = True
    input_valid = True
  else:
    print("Thanks for playing.")
    play = False
    break
 