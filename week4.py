greeting = "Hello-World" # Setting up a string to iterate through

for character in greeting: # Iterate over the string one letter at a time
    if "-" in character: # if the current character is a hyphen
        print("Hyphen detected, ending loop!")
        break # End the loop
    else:
        print(character) # Print the current character