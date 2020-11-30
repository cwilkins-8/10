#10.8 Cat and Dog

try:
    with open ('cat.txt') as cat:
        cat = cat.read()
        print (cat)

except FileNotFoundError:
    print("File not found")
    
