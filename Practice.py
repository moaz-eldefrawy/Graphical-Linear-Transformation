from manimlib.imports import *
from tkinter import *
import numpy as np
import input_gui
import output_gui
import data
import os
import pyclbr
import math



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

        print(inputData.ref_x)
        rot = inputData.rot
        shift_x = inputData.shift_x
        shift_y = inputData.shift_y




        inputPoints = np.asarray(inputPoints);


        someTransformation = np.array([[2, 1, 1],
                                       [-1, -1, 3],
                                       [1, 1, -1]])

        T_X_axis_reflection = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 1]])


        cos = math.cos(math.radians(rot))
        sin = math.sin(math.radians(rot))
        T_rotation = np.array([[cos, sin, 0],
                               [-1*sin, cos, 0],
                               [0, 0, 1]])

        T_Y_axis_reflection = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 1]])


        T_origin_reflection = np.array([[-1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 1]])

        T_Y_equal_negative_X_reflection = np.array([[0, -1, 0],
                                        [-1, 0, 0],
                                        [0, 0, 1]])

        T_Y_equal_X_reflection = np.array([[0, 1, 0],
                                            [1, 0, 0],
                                            [0, 0, 1]])

        T_Y_equal_negative_X_reflection = np.array([[0, -1, 0],
                                                    [-1, 0, 0],
                                                    [0, 0, 1]])

        shearValue = 2
        T_shear = np.array([[1, shearValue, 0],
                            [0, 1, 0],
                            [0, 0, 1]])
        shape1 = Polygon(*inputPoints)


        #          ------- SHIFTING / TRANSLATION  ------------------
        for i in range(len(inputPoints)):
            inputPoints[i] += np.array([0,1,0]) * shift_y

        shape2 = Polygon(*inputPoints)
        self.play(Transform(shape1, shape2))

        for i in range(len(inputPoints)):
            inputPoints[i] += np.array([1,0,0]) * shift_x

        shape2 = Polygon(*inputPoints)
        self.play(Transform(shape1, shape2))






        ##self.play(ShowCreation(shape1))
        ##shape3 = shape1
        unitScale = 2
        ##shape3.scale(2)

        ##self.play(ApplyMethod(shape1.shift, np.array([1, 1, 0])))
        ##self.play(ShowCreation(shape3))
        self.wait(1)
        ## shape1.scale(3)
        ## shape1.stroke_width = 10
        ## shape1.set_fill(WHITE, opacity=1)


        ##self.play(ApplyMethod(shape1.shift, np.array([0, 2, 0])))

        ## self.play(FadeOut(shape1))
        factor = 3

      ##  self.play(FadeInFromLarge(shape1, scale_factor=factor))
        reflections = [inputData.ref_y, inputData.ref_x, inputData.ref_y_x, inputData.ref_y_negative_x]
        print("Reflections:")
        print(reflections)
        T_reflections = [T_Y_axis_reflection, T_X_axis_reflection, T_Y_equal_X_reflection, T_Y_equal_negative_X_reflection]
        for i in range(4):
            if reflections[i] != 0:
                for j in range(len(inputPoints)):
                    inputPoints[j] = TransformMatrix(T_reflections[i], inputPoints[j])
                shape2 = Polygon(*inputPoints)
                shape2.set_fill(GREEN, opacity=1)
                shape2.fill_opacity = 1
                self.play(Transform(shape1, shape2))
                self.wait(2)

        output_gui.outputs(data.Outputs(inputPoints), inputPoints)







def TransformMatrix(TransMatrix, point):
    point = point.reshape(3, 1)
    c = np.dot(TransMatrix, point)

    c = c.reshape(1, 3)
    return c


