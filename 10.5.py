#10.5

filename = 'program_poll.txt'

print("Enter 'quit' when you are finished.")
while True:
    reason = input("\nWhat do you like about Python? :")
    if reason == 'quit':
        break
    else:
        with open(filename, 'a') as file:
            file.write(reason + "\n")
