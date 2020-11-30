#10.1 Files

with open ('learning_python.txt') as file:
    file = file.read()
print(file)
  
with open ('learning_python.txt') as file:
    for line in file:
        print(line.rstrip())

with open ('learning_python.txt') as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())


#10.2

file ='learning_python.txt'

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))
