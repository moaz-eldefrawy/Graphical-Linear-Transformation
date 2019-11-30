class Inputs:
    def __init__(self, points, rot, scale, shift_x, shift_y):
        self.points = points
        self.rot = rot
        self.scale = scale
        self.shift_x = shift_x
        self.shift_y = shift_y

class Outputs:
    def __init__(self, points):
        self.points = points
