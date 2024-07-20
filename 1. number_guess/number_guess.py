import random

min_value = 1

while True:

  print("Welcome to Number Guess Game!")

  while True:
    max_value = input("Please set the maximum number: ")
    if max_value.isdigit():
      if int(max_value) <= min_value:
        print("Please input a number larger than one.")
      else:
        max_value = int(max_value)
        break
    else:
      print('Please enter a number.')

  clue = random.randint(1,max_value)
  guess = 0

  while True:
    while True:
      player_number = input(f'Please guess a number between {min_value} - {max_value}:')
      if player_number.isdigit():
        player_number = int(player_number)
        break
      else:
        print("Please enter a number.")

    if player_number == clue:
      guess += 1
      print("Congrat!")
      if guess == 1:
        print(f'You have got it in {guess} guess!')
        break
      else:
        print(f'You have got it in {guess} guesses!')
        break
    elif clue > player_number > min_value:
      print("Good try!")
      min_value = player_number
      guess += 1
    elif max_value > player_number > clue:
      print("Good try!")
      max_value = player_number
      guess += 1
    else:
      print("Please enter a valid number.")
  
  print("Do you want to play again?")
  play_again = input("Please enter 'yes' or 'no': ")
  if play_again.lower() == 'no':
    print("Thank you for playing!")
    break
  elif play_again.lower() == 'yes':
    min_value = 1
  else:
    print("Please enter 'yes' or 'no'.")

