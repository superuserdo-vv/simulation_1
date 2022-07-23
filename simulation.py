import copy
import random

numList = [1, 1, 1, 1, 10, 10, 10, 100, 100, 1000]
result = {"10%": 0, "20%": 0, "30%": 0, "40%": 0}

def shuffleSimulation():
    copyList = copy.copy(numList)
    randomList = []
    i = 9
    while i >= 0:
        choice = random.randint(0, i)
        randomList.insert(0, copyList[choice])
        del copyList[choice]
        i -= 1
    while 1:
        choice = random.randint(0, len(randomList)-1)
        randomList.insert(0, randomList[choice])
        del randomList[len(randomList)-1]
        if sum(randomList) == 10:
            return "40%"
        elif sum(randomList) == 100:
            return "30%"
        elif sum(randomList) == 1000:
            return "20%"
        elif sum(randomList) == 10000:
            return "10%"

i = 10000
while i > 0:
    result[shuffleSimulation()] += 1
    i -= 1
print(result)