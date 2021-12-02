f=open('day2_input.txt',"r")
commands = []
units = []

for line in f:
    commands.append(line.split(' ')[0])
    units.append(int(line.split(' ')[1]))

# print(commands)
# print(units)

horizontal = 0
depth = 0

for i in range(len(commands)):
    if commands[i] == 'forward':
        horizontal += units[i]
    elif commands[i] == 'down':
        depth += units[i]
    elif commands[i] == 'up':
        depth -= units[i]

print(str(horizontal * depth))