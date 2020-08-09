import random as r
import tkinter as tk
import time

root = tk.Tk()
root.title("Memory Maze")

label1 = tk.Label(root, text="game of Life")
label1.pack()  # packs in order of compilation, label first, then grid

c = tk.Canvas(root, height=350, width=350, bg='white')
c.pack(fill=tk.BOTH, expand=True)

root.resizable(0, 0)

dim = 50

arr = [[r.randrange(2) for i in range(dim)] for j in range(dim)]

print(arr)


def showGrid():
    grid = ''
    for i in range(dim):
        for j in range(dim):
            print(arr[i][j], end=' ')
            grid = grid + str(arr[i][j]) + ' '
        print()
        grid = grid + '\n'
    print()
    return grid


def checkRules(n, cell=1):
    if cell == 1 and n < 2:
        return 0
    elif cell == 1 and (n == 3 or n == 2):
        return 1
    elif cell == 1 and n > 3:
        return 0
    elif cell == 0 and n == 3:
        return 1
    else:
        return cell


def gol():
    L = 0
    arrayLabel = tk.Label(c, text=showGrid())
    arrayLabel.pack()
    while True:
        if L == 1000:
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
                    nextGen[i][j] = checkRules(neighbors, arr[i][j])

        arrayLabel.configure(text=showGrid())
        arrayLabel.update()
        time.sleep(0.5)
        L += 1


gol()
root.mainloop()
