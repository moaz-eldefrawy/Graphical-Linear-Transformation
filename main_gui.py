import math
import subprocess
from tkinter import *

import numpy as np

root = Tk()


def run():
    subprocess.run(["python", "-m", "manim", "Practice.py", "Shapes", "-pl"])


run = Button(root, text="Run", command=run)
run.pack()



root.mainloop()

'''rot = 30
T_final_matrix = np.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])
cos = math.cos(math.radians(rot))
sin = math.sin(math.radians(rot))
T_rotation = np.array([[cos, sin, 0],
                                [-sin, cos, 0],
                                [0, 0, 0]],dtype="float64")
T_final_matrix = np.dot(T_rotation,T_final_matrix)
print(T_final_matrix)'''