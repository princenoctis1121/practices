import random

COLOURS = ["G", "B", "R", "P", "Y", "W"]
TRIES = 10
CODE_LENGTH = 4

#Generate code (Code is the clue of game)
def GenerateCode():
  code = []

  for i in range(CODE_LENGTH):
    colour = random.choice(COLOURS)
    code.append(colour)
  
  return code

#function for decoder(player to guess the colour)
def Decoder():
  while True:
    decode = input("Decode: ").upper().split(" ")

    if len(decode) != CODE_LENGTH:
      print(f"The code should be {CODE_LENGTH} digit of colour!")
      continue

    for i in decode:
      if i not in COLOURS:
        print("Invalid colour.")
        break
    
    else:
      break
  
  return decode

def CheckCode(decode, real_code):
  colour_count = {}
  correct_pos = 0
  incorrect_pos = 0

  for colour in real_code:
    if colour not in colour_count:
      colour_count[colour] = 0
    colour_count[colour] += 1

  #check correct position
  for decode_colour, code_colour in zip(decode, real_code):
    if decode_colour == code_colour:
      correct_pos += 1
      #substract the code after check
      colour_count[decode_colour] -= 1
  
  #Check if colour correct but position not correct
  for decode_colour, code_colour in zip(decode, real_code):
    if decode_colour in colour_count and colour_count[decode_colour] > 0:
      incorrect_pos += 1
      #substract the code after check
      colour_count[decode_colour] -= 1
  
  return correct_pos, incorrect_pos

def Game():
  code = GenerateCode()
  print(code)
  for attempts in range(1, TRIES + 1):
    decoder = Decoder()
    correct_pos, incorrect_pos = CheckCode(decoder, code)

    if correct_pos == CODE_LENGTH:
      print(f"You decode it in {attempts} turns!")
      break

    print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")

  else:
    print("You run out of tries.")


if __name__ == "__main__":
  Game()
