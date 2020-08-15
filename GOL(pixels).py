import random as r
import tkinter as tk
import time


# Setting up the tkinter scene, might be a bit messy
root = tk.Tk()
root.title("Conway's Game of Life")
size = 500 # sets the image size (square)

label1 = tk.Label(root, text="Game of Life, Pixelized")
label1.pack()  # packs in order of compilation, label first, then Image

c = tk.Canvas(root, height=size, width=size, bg='white') # canvas created with image size
c.pack(fill=tk.BOTH, expand=True)

img = tk.PhotoImage(width=size, height=size)

c.create_image((size/2, size/2), image=img, state='normal')# image created at center of screen

root.resizable(0, 0)

dim = size

#original generation, randomly generated
arr = [[r.randrange(2) for i in range(dim)] for j in range(dim)]


def showGrid():
    # list comprehension in parallel to initial list (arr),
    # if the cell is alive, its black, white if dead.
    grid = [["#000000" if arr[i][j] == 1 else "#ffffff" for i in range(dim)]for j in range(dim)]
    img.put(grid)


# gol rules,
# live cells: less that two neighbors it dies, as if by loneliness
# 2-3 neighbors, it lives, and more than 3 neighbors, it dies from overpopulation
# if the cell is dead, if it has 3 neighbors exactly it will live as if by reproduction
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

# game of life engine, calculates next generation from initial
# using rules, updates the image per-generation.
# currently skips edges, may update in the future
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


        # updates image after creating new generation,
        # and puts pixels on the grid
        img.blank()
        showGrid()
        c.update()
        #time.sleep(0.25)
        L += 1


gol()
root.mainloop()
