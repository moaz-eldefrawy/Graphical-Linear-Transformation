from tkinter import *
import data
def output(Outputs):
    root = Tk()
    original = Label(root, text="Points:")
    original.grid(row=0, column=0, sticky=E)

    row = 0
    for point in Outputs.points:
        Label(root, text=str(point[0]) + " " + str(point[1])).grid(row=row, column=1)
        row = row + 1

    Button(root, text="Run Animation", command=root.destroy).grid(row=row,column=1)
    root.mainloop()