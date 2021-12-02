# Read the input file into two lists containing the commands and the units
f=open('day2_input.txt',"r")
commands = []
units = []
for line in f:
    commands.append(line.split(' ')[0])
    units.append(int(line.split(' ')[1]))

# Set the initial horizontal and depth and aim to 0
horizontal = 0
depth = 0
aim = 0

# Iterate through the commands, updating the aim, horizontal and depth accordingly
for i in range(len(commands)):
    if commands[i] == 'down':
        aim += units[i]
    elif commands[i] == 'up':
        aim -= units[i]
    elif commands[i] == 'forward':
        horizontal += units[i]
        depth += (aim * units[i])

print(horizontal * depth)