class Inputs:
    def __init__(self, points, shift_x, shift_y, scale_x, scale_y, ref_y, ref_x, ref_y_x, ref_y_negative_x, rot):
        self.points = points
        self.shift_x = shift_x
        self.shift_y = shift_y

        self.scale_x = scale_x
        self.scale_y = scale_y

        self.ref_y = ref_y
        self.ref_x = ref_x

        self.ref_y_x = ref_y_x
        self.ref_y_negative_x = ref_y_negative_x

        self.rot = rot



class Outputs:
    def __init__(self, points):
        self.points = points
