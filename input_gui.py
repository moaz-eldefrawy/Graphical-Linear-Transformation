from tkinter import *
from manimlib.imports import *
import data

'''
python -m manim Practice.py -pl
'''

a = []


def inputs():

    point_labels = []
    entry_list = []
    entry_values = []

    def add_point():
        a.append(np.array([int(x.get()), int(y.get()), 1]))
        point_labels.append(Label(root, text=x.get() + " " + y.get()))
        point_labels[len(point_labels)-1].grid(row=10+len(a), column=1)
        x.delete(0, 'end')
        y.delete(0, 'end')

    def clear_points():
        n = len(point_labels)
        for i in range(0, n):
            point_labels[i].destroy()
        a.clear()

    def end():
        for entry in entry_list:
            print(entry.get())
            if len(entry.get()) != 0:
                entry_values.append(int(entry.get()))
            else:
                entry_values.append(0)

        root.destroy()

    def add_default():
        clear_points()
        global a
        a = [[1, 1, 1], [2, 3, 1], [4, -1, 1]];
        point_labels.append(Label(root, text="1 1"))
        point_labels[len(point_labels) - 1].grid(row=11, column=1)
        point_labels.append(Label(root, text="2 3"))
        point_labels[len(point_labels) - 1].grid(row=12, column=1)
        point_labels.append(Label(root, text="4 -1"))
        point_labels[len(point_labels) - 1].grid(row=13, column=1)
        x.delete(0, 'end')
        y.delete(0, 'end')

    root = Tk()
    root.resizable(0, 0)

    x_label = Label(text="X").grid(row=0, column=0, sticky=E)
    y_label = Label(text="Y").grid(row=0, column=2, sticky=E)
    x = Entry(root, width=5)
    x.grid(row=0, column=1, padx=(5, 5), pady=(5, 5))
    y = Entry(root, width=5)
    y.grid(row=0, column=3, padx=(5, 5), pady=(5, 5))

    add = Button(root, text="Add Point", command=add_point)
    add.grid(row=1, column=1)
    clear = Button(root, text="Clear", command=clear_points)
    clear.grid(row=1, column=3)

    shift_x_label = Label(text="Shift X").grid(row=2, column=0, sticky=E)
    shift_x = Entry(root, width=5)
    entry_list.append(shift_x)

    shift_x.grid(row=2, column=1, padx=(5, 5), pady=(5, 5))
    shift_y_label = Label(text="Shift Y").grid(row=2, column=2, sticky=E)
    shift_y = Entry(root, width=5)
    entry_list.append(shift_y)
    shift_y.grid(row=2, column=3, padx=(5, 5), pady=(5, 5))

    scale_x_label = Label(text="Scale X").grid(row=3, column=0, sticky=E)
    scale_x = Entry(root, width=5)
    entry_list.append(scale_x)
    scale_x.grid(row=3, column=1, padx=(5, 5), pady=(5, 5))

    scale_y_label = Label(text="Scale Y").grid(row=3, column=2, sticky=E)
    scale_y = Entry(root, width=5)
    entry_list.append(scale_y)
    scale_y.grid(row=3, column=3, padx=(5, 5), pady=(5, 5))

    reflection_label = Label(text="Reflection:").grid(row=4, column=0, sticky=E)

    y_ref_label = Label(text="Y").grid(row=5, column=0, sticky=E)
    y_ref = Entry(root, width=3)
    entry_list.append(y_ref)
    y_ref.grid(row=5, column=1, padx=(5, 5), pady=(5, 5))

    x_ref_label = Label(text="X").grid(row=5, column=2, sticky=E)
    x_ref = Entry(root, width=3)
    entry_list.append(x_ref)
    x_ref.grid(row=5, column=3, padx=(5, 5), pady=(5, 5))

    y_x_ref_label = Label(text="Y = X").grid(row=6, column=0, sticky=E)
    y_x_ref = Entry(root, width=3)
    entry_list.append(y_x_ref)
    y_x_ref.grid(row=6, column=1, padx=(5, 5), pady=(5, 5))

    y_negative_x_ref_label = Label(text="Y = -X").grid(row=6, column=2, sticky=E)
    y_negative_x_ref = Entry(root, width=3)
    entry_list.append(y_negative_x_ref)
    y_negative_x_ref.grid(row=6, column=3, padx=(5, 5), pady=(5, 5))

    rot_label = Label(text="Rotation").grid(row=7, column=1, sticky=E)
    rot = Entry(root, width=3)
    entry_list.append(rot)
    rot.grid(row=7, column=2, padx=(5, 5), pady=(5, 5))

    Button(root, text="Run", command=end).grid(row = 8,column = 1)

    default = Button(root, text="Enter some default values", command=add_default)
    default.grid(row=10, column=1)

    Label(text="Points:").grid(row=9, column=0)

    root.mainloop()

    print("###################Input Status######################")
    print(a)
    print(entry_values)
    print("#####################################################")

    return data.Inputs(  a,
                         entry_values[0],
                         entry_values[1],
                         entry_values[2],
                         entry_values[3],
                         entry_values[4],
                         entry_values[5],
                         entry_values[6],
                         entry_values[7],
                         entry_values[8],
                         )

