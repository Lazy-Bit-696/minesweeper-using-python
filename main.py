import tkinter # imports tkinter module which is used for GUI
import settings # imports settings for windows size
import utils
import cell

root = tkinter.Tk() # creates an instance of class Tk to form GUI window

# all the codes should be between root = tkinter.Tk() and root.mainloop()

root.configure(bg="black") # windows background color
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # windows width and height
root.title("Minesweeper Game") # windows title
root.resizable(False, False) # to make its width and height not resizable

top_frame = tkinter.Frame( # Create an instance of class Frame
    root, # on whom will this override
    bg='black', # frame color
    width=settings.WIDTH, # frame width
    height=utils.height_percentage(25) # frame height
)
top_frame.place(x=0,y=0) # fram starting postiton

left_frame = tkinter.Frame(
    root,
    bg='black',
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)

left_frame.place(
    x=0,
    y=utils.height_percentage(25)
    )

center_frame = tkinter.Frame(
    root,
    bg='black',
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)

center_frame.place(
    x=utils.width_percentage(25),
    y=utils.height_percentage(25)
    )

for row in range(settings.GRID_SIZE):
    for col in range(settings.GRID_SIZE):
        c = cell.Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=col,
            row=row
        )

root.mainloop() # puts everything on the display, and responds to user input until the program terminates