from GUI import GUI
from Globals import startCells


class Cell(GUI):
    side = GUI.size
    startCells = startCells
    nextGen = startCells[:]

    def __init__(self):
        pass

    # gol rules,
    # live cells: less that two neighbors it dies, as if by loneliness
    # 2-3 neighbors, it lives, and more than 3 neighbors, it dies from overpopulation
    # if the cell is dead, if it has 3 neighbors exactly it will live as if by reproduction
    def checkRules(self, n, cell):
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

    def handleHorizontal(self, cells, i):
        if i == 0:
            return cells
        elif i == len(self.nextGen) - 1:
            return cells

    def handleVertical(self):
        pass

    # game of life engine, calculates next generation from initial
    # using rules, updates the image per-generation.
    # currently skips edges, may update in the future
    def populateGeneration(self):
        arr = self.startCells
        nextGen = self.nextGen
        for i in range(len(nextGen)):
            # handle edges
            nextGen[i] = self.handleHorizontal(arr[i], i)
            """
            if i == 0:
                nextGen[i] = arr[i]
            elif i == len(nextGen) - 1:
                nextGen[i] = arr[i]
            """
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
                    nextGen[i][j] = self.checkRules(neighbors, arr[i][j])

    def mainGen(self):
        L = 0
        while True:
            if L == 100:
                break
            self.populateGeneration()

            # updates image after creating new generation,
            # and puts pixels on the grid
            # window.updateImage()
            # time.sleep(0.25)
            L += 1

    def __str__(self):
        pass
