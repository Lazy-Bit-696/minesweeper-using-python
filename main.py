import tkinter # imports tkinter module which is used for GUI

root = tkinter.Tk() # creates an instance of class Tk to form GUI window

# all the codes should be between root = tkinter.Tk() and root.mainloop()

root.configure(bg="black") # windows background color
root.geometry('800x400') # windows width and height
root.title("Minesweeper Game") # windows title
root.resizable(False, False) # to make its width and height not resizable

top_frame = tkinter.Frame( # Create an instance of class Frame
    root, # on whom will this override
    bg='red', # frame color
    width=800, # frame width
    height=100 # frame height
)
top_frame.place(x=0,y=0) # fram starting postiton

left_frame = tkinter.Frame(
    root,
    bg='blue',
    width=200,
    height=300
)

left_frame.place(x=0,y=100)

root.mainloop() # puts everything on the display, and responds to user input until the program terminates