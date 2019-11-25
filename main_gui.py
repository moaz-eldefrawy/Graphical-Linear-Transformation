import subprocess
from tkinter import *

root = Tk()


def run():
    subprocess.run(["python", "-m", "manim", "Practice.py", "Shapes", "-pl"])


run = Button(root, text="Run", command=run)
run.pack()



root.mainloop()