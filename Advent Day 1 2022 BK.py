
import numpy as np

#fPath = "../aoc-2022-Src/"
# f = open(fPath+"d1DemoInputs.txt", "r")

f = open("elfinput.txt", "r")
inputs = f.read()

# %% Part 1

elves = inputs.split('\n\n')
elves = [elf.splitlines() for elf in elves]

calories = []
for elf in elves:
    cals = [int(cal) for cal in elf]
    calories.append(cals)
        
totalCals = [np.sum(cals) for cals in calories]
maxCals = np.max(totalCals)

print("Max calories:", maxCals)

# Part 2

totalCals.sort()
print(totalCals[-3:], "Sum top 3", np.sum(totalCals[-3:]))