import subprocess
from tkinter import *

root = Tk()


def Run():
    subprocess.run(["python", "-m", "manim", "Practice.py", "-pl"])


run = Button(root, text="Run", command=Run)
run.pack()



root.mainloop()