# Read the input file into two lists containing the commands and the units
f=open('day2_input.txt',"r")
commands = []
units = []
for line in f:
    commands.append(line.split(' ')[0])
    units.append(int(line.split(' ')[1]))

# Set the initial horizontal and depth to 0
horizontal = 0
depth = 0

# Iterate through the commands, updating the horizontal and depth accordingly
for i in range(len(commands)):
    if commands[i] == 'forward':
        horizontal += units[i]
    elif commands[i] == 'down':
        depth += units[i]
    elif commands[i] == 'up':
        depth -= units[i]

print(str(horizontal * depth))