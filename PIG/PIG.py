import random
import sys

win_score = 1
round_score = 0
round_count = 1
player_number = 1

def InitGame():
  global win_score, player_number
  while True:
    start_btn = input("Enter p to start the game and q to quit: ")
    if start_btn == "q":
      sys.exit("Thanks for playing.")  
    elif start_btn == "p":
      break
    else:
      print("Please enter a correct command.")
  
  while True:
    player_number = input("How many players (2-4)?: ")
    if player_number.isdigit():
      player_number = int(player_number)
      if 2 <= player_number <= 4:
        break
      else:
        print("player number must be between 2-4.")
    else:
      print("Invalid input.")

  while True:
    win_score = input("How many score to win?")
    if win_score.isdigit():
      win_score = int(win_score)
      break
    else:
      print("Please enter an integer.")
  


def GameLogic():
  
  global round_score, player_total_score, win_score

  while max(player_total_score) < win_score:
    
    for  player_index in range(player_number):
      round_score = 0

      print(f"Round {round_count} for player {player_index + 1}")
      print(f"Player {player_index + 1} now have {player_total_score[player_index]} score.")
      
      while True:
        play_btn = input(f"Player {player_index + 1} enter p to roll the dice or w to withdraw.")
        if play_btn == "p":
          dice = random.randint(1,6)
          print(f"Your dice is {dice}")
          if dice == 1:
            round_score = 0
            print("Round end. No score is recorded for this round.")
            break
          else:
            round_score += dice
            print(f"Player {player_index + 1} now have {round_score} score.")
        elif play_btn == "w":
          player_total_score[player_index] += round_score
          print(f"Round end. Player {player_index + 1} got {round_score} for this round.")
          print(f"Player {player_index + 1} totally have {player_total_score[player_index]}.")
          round_score = 0
          break
        else:
          sys.exit("Thanks for playing.")

def GameResult():
  global player_total_score, win_score
  
  if min(player_total_score) >= win_score:
    print("It is a tie.")
  else:
    for winner_index in range(player_number):
      if player_total_score[winner_index] >= win_score:
        print("Player", winner_index + 1,"is the winner.")
      else:
        winner_index + 1

while True:
  InitGame()
  player_total_score = [0 for i in range(player_number)]
  GameLogic()
  GameResult()
  print("Game end.")
  play_again = input("Do you want to play again? (yes/no)")
  if play_again == "no":
    print("Thanks for playing.")
    break
  else:
    continue


