from manimlib.imports import *
import numpy as np
import input_gui
import output_gui
import data
import math


T_final_matrix = np.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]], dtype="float64")
class Shapes(Scene):
    # A few simple shapes
    def construct(self):

        grid = NumberPlane()
        self.play(
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        ##inputData = gui.data()



        inputData = input_gui.inputs()
        inputPoints = inputData.points
        rot = inputData.rot
        shift_x = inputData.shift_x - inputPoints[0][0]
        shift_y = inputData.shift_y - inputPoints[0][1]
        scale_x = inputData.scale_x
        scale_y = inputData.scale_y
        print(shift_x)
        print(shift_y)

        inputPoints = np.asarray(inputPoints)

        cos = math.cos(math.radians(rot))
        sin = math.sin(math.radians(rot))
        T_rotation = np.array([[cos, sin, 0],
                                [-sin, cos, 0],
                                [0, 0, 1]], dtype="float64")

        T_X_axis_reflection = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 1]])

        T_Y_axis_reflection = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 1]])

        T_Y_equal_X_reflection = np.array([[0, 1, 0],
                                            [1, 0, 0],
                                            [0, 0, 1]])

        T_Y_equal_negative_X_reflection = np.array([[0, -1, 0],
                                                    [-1, 0, 0],
                                                    [0, 0, 1]])
        T_shifting = np.array([[1, 0, shift_x],
                               [0, 1, shift_y],
                               [0, 0, 1]])
        T_scaling = np.array([[scale_x, 0, 0],
                               [0, scale_y, 0],
                               [0, 0, 1]])
        shearValue = 2
        T_shear = np.array([[1, shearValue, 0],
                            [0, 1, 0],
                            [0, 0, 1]])







        ##self.play(ShowCreation(shape1))
        ##shape3 = shape1
        unitScale = 2
        ##shape3.scale(2)

        ##self.play(ApplyMethod(shape1.shift, np.array([1, 1, 0])))
        ##self.play(ShowCreation(shape3))
        ## shape1.scale(3)
        ## shape1.stroke_width = 10
        ## shape1.set_fill(WHITE, opacity=1)


        ##self.play(ApplyMethod(shape1.shift, np.array([0, 2, 0])))

        ## self.play(FadeOut(shape1))
        factor = 3
        ##  self.play(FadeInFromLarge(shape1, scale_factor=factor))

        #          ------- SHIFTING / TRANSLATION  ------------------
        shape1 = Polygon(*inputPoints)
        if(shift_x !=0 and shift_y != 0):
            inputPoints = shift(self, T_shifting, inputPoints, shape1)
        #  --------------SCALING ----------------------
        if scale_x and scale_y:
            inputPoints = scale(self, T_scaling, inputPoints, shape1)
        #          ------- REFLECTIONS ------------------
        reflections = [inputData.ref_y, inputData.ref_x, inputData.ref_y_x, inputData.ref_y_negative_x]
        print("Reflections:")
        print(reflections)
        T_reflections = [T_Y_axis_reflection, T_X_axis_reflection, T_Y_equal_X_reflection, T_Y_equal_negative_X_reflection]
        inputPoints = reflect(self, reflections,T_reflections,inputPoints , shape1)


        #  --------------ROTATION ----------------------
        if (rot != 0):
            inputPoints2 = inputPoints.astype("float64")
            shape1 = Polygon(*inputPoints)
            self.add(shape1)
            shape1.set_fill(BLUE, opacity=1)
            self.wait(2)
            shift_x = -1 * inputPoints[0][0]
            shift_y = -1 * inputPoints[0][1]
            T_shifting = np.array([[1, 0, shift_x],
                                   [0, 1, shift_y],
                                   [0, 0, 1]])
            inputPoints = shift(self, T_shifting, inputPoints, shape1)

            for i in range(len(inputPoints)):
                inputPoints[i] = TransformMatrix(T_rotation, inputPoints[i]);

            shape2 = Polygon(*inputPoints)
            shape2.set_fill(YELLOW, opacity=1)
            self.play(Transform(shape1, shape2))
            self.wait(1)
            ##self.play(FadeOut(shape1))
            np.around(inputPoints, decimals=3, out=None)

            shift_x = -1 * shift_x
            shift_y = -1 * shift_y
            T_shifting = np.array([[1, 0, shift_x],
                                   [0, 1, shift_y],
                                   [0, 0, 1]])
            inputPoints = shift(self, T_shifting, inputPoints, shape1)
            self.wait(1)
            print(inputPoints)
            multiply_final_matrix(T_rotation)

        output_gui.outputs(data.Outputs(inputPoints, T_final_matrix))


def TransformMatrix(TransMatrix, point):
    point = point.reshape(3, 1)
    # c = np.dot(TransMatrix, point)
    point = point.astype("float64")
    c = np.array([[0],
                  [0],
                  [0]], dtype="float64")
    for i in range(3):
        for j in range(3):
            c[i] = c[i] + (TransMatrix[i][j] * point[j])

    c = c.reshape(1, 3)
    c = np.around(c, decimals=3, out=None)
    return c

'''def TransformMatrix_float(TransMatrix, point):
    point = point.reshape(3, 1)
    #c = np.dot(TransMatrix, point)
    point = point.astype("float64")
    c = np.array([[0],
                 [0],
                 [0]],  dtype="float64")
    for i in range(3):
        for j in range(3):
            c[i] = c[i] + (TransMatrix[i][j] * point[j])

    c = c.reshape(1, 3)
    c = np.around(c, decimals=3, out=None)
    return c


def rotation_trans(TransMatrix, point):
    point = point.reshape(3, 1)
    point = point.astype("float64")
    # c = np.dot(TransMatrix, point)
    c = np.array([[0],
                  [0],
                  [0]], dtype="float64")
    for i in range(3):
        for j in range(3):
            c[i] = c[i] + (TransMatrix[i][j] * point[j])

    c = c.reshape(1, 3)
    c = np.around(c, decimals=3, out=None)
    return c


'''
def reflect(self, reflections, T_reflections, inputPoints, shape1):
    for i in range(4):
        if (reflections[i] != 0):
            for j in range(len(inputPoints)):
                inputPoints[j] = TransformMatrix(T_reflections[i], inputPoints[j])
            multiply_final_matrix(T_reflections[i])
            shape2 = Polygon(*inputPoints)
            shape2.set_fill(GREEN, opacity=1)
            shape2.fill_opacity = 1
            self.play(Transform(shape1, shape2))
            self.wait(1)

    self.play(FadeOut(shape1))
    return inputPoints


def shift (self, T_shifting, inputPoints, shape1):
    shape1.set_fill(RED, opacity=1)
    inputPoints = inputPoints.astype("float64")
    for i in range(len(inputPoints)):
        inputPoints[i] = TransformMatrix(T_shifting, inputPoints[i])

    shape2 = Polygon(*inputPoints)
    shape2.set_fill(RED, opacity=1)
    self.play(Transform(shape1, shape2))
    self.wait(1.5)
    multiply_final_matrix(T_shifting)
    return inputPoints


def scale(self, T_scaling, inputPoints, shape1):
    shape1.set_fill(PINK, opacity=1)
    shift_x = -1* inputPoints[0][0]
    shift_y = -1* inputPoints[0][1]
    T_shifting = np.array([[1, 0, shift_x],
                           [0, 1, shift_y],
                           [0, 0, 1]])

    inputPoints = shift(self, T_shifting, inputPoints, shape1)

    for i in range(len(inputPoints)):
        inputPoints[i] = TransformMatrix(T_scaling, inputPoints[i])

    multiply_final_matrix(T_scaling)

    shape2 = Polygon(*inputPoints)
    shape2.set_fill(PINK, opacity=1)
    self.play(Transform(shape1, shape2))
    self.wait(2)
    T_shifting = np.array([[1, 0, -1 * shift_x],
                           [0, 1, -1 * shift_y],
                           [0, 0, 1]])
    inputPoints = shift(self, T_shifting, inputPoints, shape1)
    return inputPoints

def multiply_final_matrix (T_Matrix):
    global T_final_matrix
    ans = np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]], dtype="float64")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ans[i][j] += T_Matrix[i][k] * T_final_matrix[k][j]
    ans = np.around(ans, decimals=3, out=None)

    T_final_matrix = ans
