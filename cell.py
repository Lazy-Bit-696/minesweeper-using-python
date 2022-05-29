import random
import tkinter
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    # magic method
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
    # create button
    def create_btn_object(self, frame):
        btn = tkinter.Button(
            frame,
            text="{}, {}".format(self.x,self.y)
        )
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click
        self.cell_btn_object = btn

    # left click action
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    # right click action
    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    #randomize mine
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True