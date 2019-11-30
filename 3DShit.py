from manimlib.imports import *
import os
import pyclbr
from tkinter import *
##import numpy as np
n = 0




class Shapes(ThreeDScene):
    # A few simple shapes

    def construct(self):
        ##print(CONFIG)
        CONFIG = {"plane_kwargs": {
            "x_line_frequency": 2,
            "y_line_frequency": 2
        },
            "camera_class": ThreeDCamera,
            "ambient_camera_rotation": None,
            "default_angled_camera_orientation_kwargs": {
                "phi": 90 * DEGREES,
                "theta": -135 * DEGREES,
            }
        }
        ## 1.5 PI = 90
        ## PI for Vertical and Gamma Horizontal
        self.set_camera_orientation(phi=70 * DEGREES, theta=-90 * DEGREES)

        ##sphere = self.get_sphere()
        cube = Cube()
        prism = Prism()
        self.play(ShowCreation(cube))
      ##  self.play(ReplacementTransform(sphere, cube))
        self.play(ReplacementTransform(cube, prism))
        self.wait(2)

        for i in range(-10, 10):
            Y_Axis = Line(np.array([i, 10, 0]), np.array([i, -10, 0]))
            X_Axis = Line(np.array([10, i, 0]), np.array([-10, i, 0]))
            X_Axis.set_color(GREEN)
            Y_Axis.set_color(GREEN)
            self.add(Y_Axis)
            self.add(X_Axis)

        Z_Axis = Line(np.array([0, 0, -10]), np.array([0, 0, 10]))
        Z_Axis.set_color(WHITE)
       ## Z_Axis.color = #ff000:
        self.add(Z_Axis)


        ##self.set_camera_orientation(phi= , gamma=0)
        a = [np.array([1,1,0]), np.array([1,1,1]), np.array([1,1,0]),
             np.array([1,2,0]), np.array([1,2,1]), np.array([1,2,0]),
             np.array([2,2,0]),  np.array([2,2,1]),  np.array([2,2,0]),
             np.array([2,1,0]), np.array([2,1,1]),## np.array([2,1,0]),
             np.array([1, 1, 1]), np.array([1, 2, 1]), np.array([2, 2, 1]),  np.array([2, 1, 1]),
             np.array([2, 1, 0])]

        for x in range(-10, 10):
            for y in range(-10, 10):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))



        a = np.asarray(a);


        someTransformation = np.array([[2, 1, 1],
                                [-1, -1, 3],
                                [1, 1, -1]])


        T_X_axis_reflection = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 1]])
        T_Y_axis_reflection = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 1]])

        T_Z_axis_reflection = np.array([[1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, -1]])

        T_origin_reflection = np.array([[-1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, -1]])
        shearValue = 2
        T_shear = np.array([[1, shearValue, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

        Y_Axis = Line(np.array([0, 10, 0]), np.array([0, -10, 0]))
        Y_Axis.set_fill(RED, opacity=0.5)
        Y_Axis.stroke_width = 10;
        X_Axis = Line(np.array([10, 0, 0]), np.array([-10, 0, 0]))
        X_Axis.set_fill(RED)
        X_Axis.stroke_width = 10;
        self.add(Y_Axis)
        self.add(X_Axis)
       ## self.setup_axes
        shape1 = Polygon(*a)


        self.play(ShowCreation(shape1))
        self.wait(1)

        ##shape3 = shape1
        unitScale = 2
        ##shape3.scale(2)

        ##self.play(ApplyMethod(shape1.shift, np.array([1, 1, 0])))
        ##self.play(ShowCreation(shape3))
       ## shape1.scale(3)
       ## shape1.stroke_width = 10
       ## shape1.set_fill(WHITE, opacity=1)
        ##shape1.rotate(45 * DEGREES)


        ##self.play(ApplyMethod(shape1.shift, np.array([0, 2, 0])))



       ## self.play(FadeOut(shape1))
        factor = 3
      ##  self.play(FadeInFromLarge(shape1, scale_factor=factor))
        for i in range(len(a)):
            a[i] = TransformMatrix(T_Y_axis_reflection, a[i])
        print(a)
        shape2 = Polygon(*a)
        shape2.set_fill(GREEN, opacity=1)
        shape2.fill_opacity = 1;
        ##print(shape2.points)
        self.play(Transform(shape1,shape2))
        ##self.play(ApplyMethod(shape2.shift, np.array([0, 1, 0])))

        self.wait(2)
        self.move_camera(phi=70 * DEGREES, theta=-270 * DEGREES)
        self.wait(0.5)
        '''
        self.move_camera(phi=85 * DEGREES, theta=-270 * DEGREES)
        self.wait(2)
        self.move_camera(phi=80 * DEGREES, theta=-135 * DEGREES, run_time=1)
        self.wait(2)
        '''
    ##shape2 =



def TransformMatrix(TransMatrix, point):
    ## (1,3)
    point = point.reshape(3, 1)
    c = np.dot(TransMatrix, point)

    c = c.reshape(1, 3)
    return c
