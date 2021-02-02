while True: # This is an infinite loop
  number = int(input("Please type a number between 1 and 10: ")) # Take user input

  if number < 1: # Number is too small
    print("Number provided is less than 1")

  elif number > 10: # Number is too large
    print("Number provided is greater than 10")

  else: # If the input is in a valid range
    print("Number provided is between 1 and 10")
    break # End the loop