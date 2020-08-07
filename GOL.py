import random as r
import tkinter as tk

arr = [[r.randrange(2) for i in range(10)] for j in range(10)]
print(arr)


def checkRules(n, cell=1):
    if cell == 1 and n < 2:
        return 0
    elif cell == 1 and n == 3 or n == 2:
        return 1
    elif cell == 1 and n > 3:
        return 0
    """
    else:
        if n == 3:
            return 1
    """


L = 0

while True:
    if L == 10:
        break
    nextGen = arr[:]
    for i in range(len(nextGen)):
        if i == 0:
            nextGen[i] = arr[i]
        elif i == len(nextGen) - 1:
            nextGen[i] = arr[i]

        for j in range(len(nextGen)):
            if j == 0 or i == 0:
                nextGen[i][j] = arr[i][j]
            elif j == len(nextGen) - 1 or i == len(nextGen) - 1:
                continue
            else:
                x = sum(arr[i - 1][j - 1:j + 1])
                y = sum(arr[i + 1][j - 1:j + 1])
                z = arr[i][j - 1] + arr[i][j + 1]
                neighbors = x + y + z
                nextGen[i][j] = checkRules(neighbors)

    for i in range(10):
        for j in range(10):
            print(arr[i][j], end=' ')
        print()
    print()
    L += 1
