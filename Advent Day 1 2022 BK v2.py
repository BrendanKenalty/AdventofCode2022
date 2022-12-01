
import numpy as np

#Wooks

f = open("ElfDay1v2.txt", "r")
#inputs = f.read()
raw = [j for j in f.read().splitlines()]

print(raw)
print("------raw------")
#broke all terms into strings

# %% Part 1

elfTracker = {}
elfNum = 0
calTracker = 0
#loop through and make array, whith index and total cal between " " spaces as breaks

for j in raw:
    if j=='':
        #this assigns total cal to string when hit break,then resets and starts again
        elfTracker[elfNum] = calTracker
        elfNum += 1
        calTracker = 0
    else:
        # if no " " blank, it loops and adds the calories for that elf...increase var each time through loop
        calTracker += int(j)
        
print(calTracker,"------CalT------")

print('Part 1 Answer: ')
print('The elf with the most calories is elf number: ' + str(max(elfTracker)))
print('They have ' + str(max(elfTracker.values())) + ' calories')

