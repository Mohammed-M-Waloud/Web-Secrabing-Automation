import random

lines = open("Visa.txt", 'r').read().splitlines()
line = str(random.choice(lines)).split('|')
print(line)