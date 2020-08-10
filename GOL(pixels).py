import random as r
import tkinter as tk
import time

root = tk.Tk()
root.title("Conway's Game of Life")
size = 500

label1 = tk.Label(root, text="Game of Life, Pixelized")
label1.pack()  # packs in order of compilation, label first, then grid

c = tk.Canvas(root, height=size, width=size, bg='white')
c.pack(fill=tk.BOTH, expand=True)

img = tk.PhotoImage(width=size, height=size)

c.create_image((size/2, size/2), image=img, state='normal')


root.resizable(0, 0)

dim = 500

arr = [[r.randrange(2) for i in range(dim)] for j in range(dim)]

print(arr)


def showGrid():
    grid = [["#000000" if arr[i][j] == 1 else "#ffffff" for i in range(dim)]for j in range(dim)]
    #print(grid, end='\n')
    img.put(grid)
    #for i in range(dim):
    #    for j in range(dim):
    #        img.put(grid[i*j+j], (i, j))
    """
    for i in range(dim):
        for j in range(dim):
            print(arr[i][j], end=' ')
            if arr[i][j] == 1:
                img.put('#000000', (i, j))
            else:
                img.put('#ffffff', (i, j))
        print()
        grid = grid + '\n'
        img.put(grid)

    print()
    return grid
    """


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
    showGrid()
    while True:
        if L == 100:
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

        #arrayLabel.configure(text=showGrid())
        #arrayLabel.update()
        img.blank()
        showGrid()
        c.update()
        time.sleep(0.5)
        L += 1


gol()
root.mainloop()
