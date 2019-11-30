from manimlib.imports import *
from tkinter import *
import numpy as np
#from tuts import *
import gui
import inputs
import os
import pyclbr
import gui

n = 0

class Shapes(Scene):
    # A few simple shapes

    def construct(self):
        strings = []
        a = gui.data().points
        l = len(a)


        for x in range(-10, 10):
            for y in range(-10, 10):
                self.add(Dot(np.array([x, y, 2]), color=DARK_GREY))




        a = np.asarray(a);


        print(strings)
        someTransformation = np.array([[2, 1, 1],
                                [-1, -1, 3],
                                [1, 1, -1]])

        T_X_axis_reflection = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 0]])
        T_Y_axis_reflection = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 0]])

        T_origin_reflection = np.array([[-1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 0]])
        shearValue = 2
        T_shear = np.array([[1, shearValue, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

        Y_Axis = Line(np.array([0, 10, 0]), np.array([0, -10, 0]))
        X_Axis = Line(np.array([10, 0, 0]), np.array([-10, 0, 0]))
        self.add(Y_Axis)
        self.add(X_Axis)
       ## self.setup_axes
        shape1 = Polygon(*a)


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
        ##shape1.rotate(45 * DEGREES)


        ##self.play(ApplyMethod(shape1.shift, np.array([0, 2, 0])))



       ## self.play(FadeOut(shape1))
        factor = 3
      ##  self.play(FadeInFromLarge(shape1, scale_factor=factor))
        for i in range(len(a)):
            a[i] = TransformMatrix(T_origin_reflection, a[i])
        print(a)
        shape2 = Polygon(*a)
        shape2.set_fill(GREEN, opacity=1)
        shape2.fill_opacity = 1;
        ##print(shape2.points)
        self.play(Transform(shape1,shape2))
        ##self.play(ApplyMethod(shape2.shift, np.array([0, 1, 0])))
        self.wait(5)
    ##shape2 =


def TransformMatrix(TransMatrix, point):
    ## (1,3)
    point = point.reshape(3, 1)
    c = np.dot(TransMatrix, point)

    c = c.reshape(1, 3)
    return c
