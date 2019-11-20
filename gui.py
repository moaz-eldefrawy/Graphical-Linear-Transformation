from tkinter import *
import numpy as np
from manimlib.imports import *
import inputs

#subprocess.run(["python", "-m", "manim", "work.py", "-pl"])
'''
python -m manim Practice.py -pl
'''


def data():
    print("###################Input Status######################")
    a = [[0,1,0],[1,0,1],[2,4,5]]
    point_labels = []
    entry_list = []
    entry_values = [0,0,0,0]

    def add_point():
        a.append(np.array([int(x_in.get()), int(y_in.get()), 1]))
        print(a)
        point_labels.append(Label(root, text=x_in.get() + " " + y_in.get()))
        point_labels[len(point_labels)-1].grid(row=7+len(a), column=1)
        x_in.delete(0, 'end')
        y_in.delete(0, 'end')

    def clear_points():
        n = len(point_labels)
        for i in range(0, n):
            point_labels[i].destroy()
        a.clear()

    def end():
        for entry in entry_list:
            if len(entry.get()) == 0:
                entry_values.append(0)
                print("Empty")
            else:
                entry_values.append(int(entry.get()))
                print(entry.get())
        root.destroy()

    root = Tk()
    x_in_label = Label(text="X").grid(row=0, column=0, sticky=E)
    y_in_label = Label(text="Y").grid(row=0, column=2, sticky=E)
    x_in = Entry(root, width=5)
    x_in.grid(row=0, column=1, padx=(5,5), pady=(5,5))
    y_in = Entry(root, width=5)
    y_in.grid(row=0,column=3, padx=(5,5), pady=(5,5))

    add = Button(root, text="Add Point", command=add_point)
    add.grid(row=1, column=1)
    clear = Button(root, text="Clear", command=clear_points)
    clear.grid(row=1, column=3)

    rot_in_label = Label(text="Rotation").grid(row=2, column=0, sticky=E)
    rot_in = Entry(root, width=5)
    entry_list.append(rot_in)
    rot_in.grid(row=2, column=1, padx=(5,5), pady=(5,5))

    scale_in_label = Label(text="Scale").grid(row=2, column=2, sticky=E)
    scale_in = Entry(root, width=5)
    entry_list.append(scale_in)
    scale_in.grid(row=2, column=3, padx=(5, 5), pady=(5, 5))

    shift_x_in_label = Label(text="Shift X").grid(row=3, column=0, sticky=E)
    shift_x_in = Entry(root, width=5)
    entry_list.append(shift_x_in)
    shift_x_in.grid(row=3, column=1, padx=(5, 5), pady=(5, 5))
    shift_y_in_label = Label(text="Shift Y").grid(row=3, column=2, sticky=E)
    shift_y_in = Entry(root, width=5)
    entry_list.append(shift_y_in)
    shift_y_in.grid(row=3, column=3, padx=(5, 5), pady=(5, 5))

    Button(root, text="Run", command=end).grid(row = 6,column = 1)

    Label(text="Points:").grid(row=7, column=0)


    root.mainloop()
    print("#####################################################")


    return inputs.Inputs(a,
                         entry_values[0],
                         entry_values[1],
                         entry_values[2],
                         entry_values[3])
