from tkinter import *
import data


def outputs(output_data):
    root = Tk()
    final_points = Label(root, text="Points:")
    final_points.grid(row=0, column=0, sticky=W)

    final_matrix = Label(root, text="Matrix:")
    final_matrix.grid(row=0, column=3, sticky=E)

    row = 1
    for point in output_data.points:
        Label(root, text=str(point[0]) + " " + str(point[1])).grid(row=row, column=0)
        row = row + 1

    # Printing the final matrix
    row = 1
    for i in range(3):
        for j in range(3):
            Label(root, text=str(output_data.T_final_matrix[i][j]) + " ").grid(row=row, column=j + 3)
        row = row + 1

    Button(root, text="Run Animation", command=root.destroy).grid(row=row, column=1)
    root.mainloop()
