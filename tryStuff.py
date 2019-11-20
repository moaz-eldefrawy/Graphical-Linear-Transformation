import numpy as np

def whatever(*Args):
    for arg in Args:
        print(arg)


array = [1,3,5,315,135,51]
whatever(*array)