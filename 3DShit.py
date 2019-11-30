from manimlib.imports import *
import os
import pyclbr
from tkinter import *
##import numpy as np
n = 0


def get_cube(b1,b2,b3,b4,h1,h2,h3,h4, **kwargs):
    # base
    s1 = Line(h1,h2, **kwargs)
    s2 = Line(h2,h3, **kwargs)
    s3 = Line(h3,h4, **kwargs)
    s4 = Line(h4,h1, **kwargs)

    # top
    s5 = Line(b1, b2, **kwargs)
    s6 = Line(b2, b3, **kwargs)
    s7 = Line(b3, b4, **kwargs)
    s8 = Line(b4, b1, **kwargs)

    # connectors
    s9 = Line(b1,h1, **kwargs)
    s10 = Line(b2,h2, **kwargs)
    s11 = Line(b3, h3, **kwargs)
    s12 = Line(b4,h4, **kwargs)

    return Group(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)

def get_pyramid(p1,p2,p3,p4,p5, **kwargs):
    #base
    s1 = Line(p1, p2, **kwargs)
    s2 = Line(p2, p3, **kwargs)
    s3 = Line(p3, p4, **kwargs)
    s4 = Line(p4, p1, **kwargs)

    # top
    s5 = Line(p1, p5, **kwargs)
    s6 = Line(p2, p5, **kwargs)
    s7 = Line(p3, p5, **kwargs)
    s8 = Line(p4, p5, **kwargs)

    return [s1, s2, s3, s4, s5, s6, s7, s8]


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
        ##cube = Cube()
       ## prism = Prism()
        ##print("Print prism:")
       ## print(prism)

       ## prism = get_cube(1.5, color="#ff0000", stroke_width=10)
      ##  print("printing:")
       ## print(type(prism))
      ##  prism.shift(5 * np.array([0,0,1]))
      ##  for i in (len(prism)):
        ##    prism += np.array([0,0,5])
       ## self.play(ShowCreation(prism))
      ##  self.play(ReplacementTransform(sphere, cube))
       ## self.play(ReplacementTransform(cube, prism))
        self.wait(2)

        for i in range(-10, 10):
            Y_Axis = Line(np.array([i, 10, 0]), np.array([i, -10, 0]))
            X_Axis = Line(np.array([10, i, 0]), np.array([-10, i, 0]))
            X_Axis.set_color(GREEN)
            Y_Axis.set_color(GREEN)
            self.add(Y_Axis)
            self.add(X_Axis)

        Y_Axis = Line(np.array([0, 10, 0]), np.array([0, -10, 0]))
        Y_Axis.set_fill(RED, opacity=0.5)
        Y_Axis.stroke_width = 10;
        X_Axis = Line(np.array([10, 0, 0]), np.array([-10, 0, 0]))
        X_Axis.set_fill(RED)
        X_Axis.stroke_width = 10;
        self.add(Y_Axis)
        self.add(X_Axis)

        Z_Axis = Line(np.array([0, 0, -10]), np.array([0, 0, 10]))
        Z_Axis.set_color(WHITE)
        self.add(Z_Axis)


        ##self.set_camera_orientation(phi= , gamma=0)
        '''
        a = [np.array([1,1,0]), np.array([1,1,1]), np.array([1,1,0]),
             np.array([1,2,0]), np.array([1,2,1]), np.array([1,2,0]),
             np.array([2,2,0]),  np.array([2,2,1]),  np.array([2,2,0]),
             np.array([2,1,0]), np.array([2,1,1]),## np.array([2,1,0]),
             np.array([1, 1, 1]), np.array([1, 2, 1]), np.array([2, 2, 1]),  np.array([2, 1, 1]),
             np.array([2, 1, 0])]
        '''
        b = [np.array([1,1,0]) ,np.array([1,2,0]),np.array([2,2,0]),np.array([2,1,0]),np.array([1.5,1.5,3])]

        for x in range(-10, 10):
            for y in range(-10, 10):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))





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


       ## self.setup_axes
        a = get_pyramid(*b)
        for i in range(len(a)):
            self.play(ShowCreation(a[i], run_time=0.5))

        print(b)
        for i in range(len(b)):
            b[i] = TransformMatrix(T_Y_axis_reflection, b[i])

        print(b)
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
        self.wait(1)

        self.move_camera(phi=70 * DEGREES, theta=-270 * DEGREES)
        self.wait(0.5)


        z = get_pyramid(*b)
        for i in range(len(z)):
            self.play(Transform(a[i],z[i]), run_time=0.5)


        
        self.move_camera(phi=85 * DEGREES, theta=-270 * DEGREES)
        self.wait(2)


    ##shape2 =



def TransformMatrix(TransMatrix, point):
    ## (1,3)
    point = point.reshape(3, 1)
    c = np.dot(TransMatrix, point)

    c = c.reshape(1, 3)
    return c[0]
