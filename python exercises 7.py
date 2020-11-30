#7 Write a Python program to guess a number between 1 to 9.
#Note : User is prompted to enter a guess.
#If the user guesses wrong then the prompt appears
#again until the guess is correct, on successful guess,
#user will get a "Well guessed!" message, and the program will exit.

number = 8

message = input("Guess a number between 1 - 9 : ")
message = int(message)

if message >= 10:
    print("\n This number is too high!")

else:
    print ("Thank you for this number")
