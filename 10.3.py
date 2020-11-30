#10.3 Guest: Write a program that prompts the user for their name. When they
#respond, write their name to a file called guest.txt.

#name = input("What is your name? : ")


#with open('guest.txt', 'a') as file:
    #file.write(name)

filename ='guest.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat is your name? : ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file:
            file.write(name + "\n")
    print("Hi " + name +" you have been added to the guest book!")
    
