import tkinter

root = tkinter.Tk()

btn = tkinter.Button(
    root,
    text="lol"
)

btn.place(x=0,y=0)

def click_actions(event):
    print("click")
    btn.configure(text="cli")

btn.bind('<Button-1>', click_actions) 

root.mainloop()