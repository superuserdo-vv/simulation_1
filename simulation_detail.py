import copy
import random

numList = [1, 1, 1, 1, 10, 10, 10, 100, 100, 1000]

copyList = copy.copy(numList)
randomList = []
i = 9
while i >= 0:
    choice = random.randint(0, i)
    randomList.insert(0, copyList[choice])
    del copyList[choice]
    i -= 1
while 1:
    print(randomList)
    choice = random.randint(0, len(randomList)-1)
    randomList.insert(0, randomList[choice])
    del randomList[len(randomList)-1]
    if sum(randomList) == 10:
        print(randomList)
        break
    elif sum(randomList) == 100:
        print(randomList)
        break
    elif sum(randomList) == 1000:
        print(randomList)
        break
    elif sum(randomList) == 10000:
        print(randomList)
        break

