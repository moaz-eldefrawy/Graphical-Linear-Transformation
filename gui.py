from tkinter import *
import numpy as np
from manimlib.imports import *

#subprocess.run(["python", "-m", "manim", "work.py", "-pl"])
#python -m manim Practice.py -pl


def data():
    a = []
    root = Tk()

    def add_point():
        a.append(np.array([int(x.get()), int(y.get()), 1]))
        #print(a)
        label = Label(root, text=x.get() + " " + y.get())
        label.pack()
        x.delete(0, 'end')
        y.delete(0, 'end')

    x = Entry(root, width=20)
    x.pack()
    y = Entry(root, width=20)
    y.pack()

    add = Button(root, text="Add Point", command=add_point)
    add.pack()
    Button(root, text="Run", command=root.destroy).pack()

    root.mainloop()
    return a
