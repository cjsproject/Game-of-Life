from source.GUI import GUI
from source.Globals import startCells
from source.Rules import checkRules


class Automata:
    window = GUI()
    side = GUI.size
    nextGen = startCells[:]

    def __init__(self):
        self.mainGen()

    # gol rules,
    # live cells: less that two neighbors it dies, as if by loneliness
    # 2-3 neighbors, it lives, and more than 3 neighbors, it dies from overpopulation
    # if the cell is dead, if it has 3 neighbors exactly it will live as if by reproduction

    def handleHorizontal(self, cells, i):
        if i == 0:
            return cells
        elif i == len(self.nextGen) - 1:
            return cells

    def handleVertical(self, cell, i, j):
        # handle edges
        if j == 0 or i == 0:
            return cell
        elif j == len(self.nextGen) - 1 or i == len(self.nextGen) - 1:
            return cell

    # game of life engine, calculates next generation from initial
    # using rules, updates the image per-generation.
    # currently skips edges, may update in the future
    def populateGeneration(self):
        arr = startCells
        nextGen = self.nextGen
        for i in range(len(nextGen)):
            for j in range(len(nextGen)):
                # handle edges
                if j == 0 or i == 0:
                    nextGen[i][j] = arr[i][j]
                elif j == len(nextGen) - 1 or i == len(nextGen) - 1:
                    continue
                # count neighbors
                else:
                    x = sum(arr[i - 1][j - 1:j + 1])
                    y = sum(arr[i + 1][j - 1:j + 1])
                    z = arr[i][j - 1] + arr[i][j + 1]
                    neighbors = x + y + z
                    nextGen[i][j] = checkRules(neighbors, arr[i][j])




    def mainGen(self):
        L = 0
        while True:
            if L == 100:
                break
            self.populateGeneration()
            self.window.updateImage()
            L += 1
            # updates image after creating new generation,
            # and puts pixels on the grid
            # window.updateImage()
            # time.sleep(0.25)

    def __str__(self):
        pass
