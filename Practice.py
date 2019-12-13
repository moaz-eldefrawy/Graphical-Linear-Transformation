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

        rot = inputData.rot
        shift_x = inputData.shift_x
        shift_y = inputData.shift_y
        scale_x = inputData.scale_x
        scale_y = inputData.scale_y


        inputPoints = np.asarray(inputPoints);






        cos = math.cos(math.radians(rot))
        sin = math.sin(math.radians(rot))
        T_rotation = np.array([[cos, sin, 0],
                               [-1*sin, cos, 0],
                               [0, 0, 1]])

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
        shape1 = Polygon(*inputPoints)
        #          ------- SHIFTING / TRANSLATION  ------------------
        inputPoints = shift(self, T_shifting, inputPoints)
        '''for i in range(len(inputPoints)):
            inputPoints[i] += np.array([0, 1, 0]) * shift_y

        shape2 = Polygon(*inputPoints)
        self.play(Transform(shape1, shape2))

        for i in range(len(inputPoints)):
            inputPoints[i] += np.array([1,0,0]) * shift_x

        shape2 = Polygon(*inputPoints)
        self.play(Transform(shape1, shape2))'''

        #          ------- REFLECTIONS ------------------
        reflections = [inputData.ref_y, inputData.ref_x, inputData.ref_y_x, inputData.ref_y_negative_x]
        print("Reflections:")
        print(reflections)
        T_reflections = [T_Y_axis_reflection, T_X_axis_reflection, T_Y_equal_X_reflection, T_Y_equal_negative_X_reflection]
        inputPoints = reflect(self, reflections,T_reflections,inputPoints)

        #  --------------SCALING ----------------------
        if scale_x and scale_y:
            inputPoints = scale(self, T_scaling, inputPoints)

        output_gui.outputs(data.Outputs(inputPoints), inputPoints)


def TransformMatrix(TransMatrix, point):
    point = point.reshape(3, 1)
    #c = np.dot(TransMatrix, point)
    c = np.array([[0],
                 [0],
                 [0]])
    for i in range(3):
        for j in range(3):
            c[i] += TransMatrix[i][j] * point[j]

    c = c.reshape(1, 3)
    return c


def reflect(self, reflections, T_reflections, inputPoints):
    shape1 = Polygon(*inputPoints)
    for i in range(4):
        if reflections[i] != 0:
            for j in range(len(inputPoints)):
                inputPoints[j] = TransformMatrix(T_reflections[i], inputPoints[j])
            shape2 = Polygon(*inputPoints)
            shape2.set_fill(GREEN, opacity=1)
            shape2.fill_opacity = 1
            self.play(Transform(shape1, shape2))
            self.wait(2)
    return inputPoints


def shift (self, T_shifting, inputPoints):
    shape1 = Polygon(*inputPoints)
    for i in range(len(inputPoints)):
        inputPoints[i] = TransformMatrix(T_shifting, inputPoints[i])

    shape2 = Polygon(*inputPoints)
    self.play(Transform(shape1, shape2))
    self.wait(2)
    return inputPoints


def scale (self, T_scaling, inputPoints):
    shape1 = Polygon(*inputPoints)
    shift_x = -1* inputPoints[0][0]
    shift_y = -1* inputPoints[0][1]
    T_shifting = np.array([[1, 0, shift_x],
                           [0, 1, shift_y],
                           [0, 0, 1]])

    inputPoints = shift(self, T_shifting, inputPoints)

    for i in range(len(inputPoints)):
        inputPoints[i] = TransformMatrix(T_scaling, inputPoints[i])

    shape2 = Polygon(*inputPoints)
    self.play(Transform(shape1, shape2))
    self.wait(2)

    T_shifting = np.array([[1, 0, -1 * shift_x],
                           [0, 1, -1 * shift_y],
                           [0, 0, 1]])
    inputPoints = shift(self, T_shifting, inputPoints)
    return inputPoints
