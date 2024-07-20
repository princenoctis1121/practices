master_pw = input("What is the master password?")
pw_data = {}

  
def AddPassword():
  while True:
    pw_name = input("Enter password name:")
    if pw_name == None :
      print("Password name cannot be empty.")
    else:
      break
  while True:
    pw = input("Please enter your password:")
    if pw == None:
      print("Password cannot be empty.")
    else:
      break
  pw_data[pw_name] = pw

def ViewPassword():
  while True:
    pw_attempt = input("Enter master password:")
    if pw_attempt != master_pw :
      print("Master password incorrect.")
    else:
      break
  
  while True:
    ask_name = input("Enter the password name to see the password:")
    if pw_data[ask_name] != None:
      print("Password is: ", pw_data[ask_name])
      view_cont = input("Do you wanna check other password? (yes/no)")
      if view_cont == "yes":
        continue
      else:
        break
    elif ask_name == "q":
      print("Bye")
      break
    else:
      print("Please enter a correct name.")


while True:
  mode = input("Which mode do you want to access to?(add/view)")
  if mode == "add":
    AddPassword()

  elif mode == "view":
    ViewPassword()

  elif mode == "q":
    print("See you.")
    break