import tkinter as tk
from Globals import side, startCells

class GUI:
    # Setting up the tkinter scene, might be a bit messy
    root = tk.Tk()
    size = side  # sets the image size (square)

    c = tk.Canvas(root, height=size, width=size, bg='white')
    img = tk.PhotoImage(width=size, height=size)
    arr = startCells

    def __init__(self):
        root = self.root
        size = self.size
        c = self.c

        root.title("Conway's Game of Life")

        self.setStage(root, size, c)
        self.showGrid()
        self.runMainLoop()

    def setStage(self, root, size, c):
        tk.Label(root, text="Game of Life, Pixelized").pack()  # packs in order of compilation, label first, then Image
        c.pack(fill=tk.BOTH, expand=True)  # canvas created with image size
        c.create_image((size / 2, size / 2), image=self.img, state='normal')  # image created at center of screen
        root.resizable(0, 0)

    def showGrid(self):
        # list comprehension in parallel to initial list (arr),
        # if the cell is alive, its black, white if dead.
        grid = [["#000000" if self.arr[i][j] == 1 else "#ffffff" for i in range(self.size)] for j in range(self.size)]
        self.img.put(grid)

    def updateImage(self):
        self.img.blank()
        self.showGrid()
        self.c.update()

    def runMainLoop(self):
        self.root.mainloop()


GUI()
