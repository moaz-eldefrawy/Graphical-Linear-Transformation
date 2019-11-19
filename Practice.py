from manimlib.imports import *

import numpy as np


class Shapes(Scene):
    # A few simple shapes
    def construct(self):

        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))

        a = []
        a.append(np.array([0, 0, 0]))
        # a.append(np.array([ [0] , [0] , [0] ]))
        a.append(np.array([1, 0, 0]))
        a.append(np.array([1, 1, 0]))
        a.append(np.array([0, 1, 0]))
        a = np.asarray(a);
        Translation = np.array([[5, 3, 3],
                                [2, 1, 4],
                                [1, 1, 5]])

        T_X_axis_reflection = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 0]])
        T_Y_axis_reflection = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 0]])


        shearValue = 2
        T_shear = np.array([[1, shearValue, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

        shape1 = Polygon(a[0], a[1], a[2], a[3])
        print(shape1.points)
        print(shape1.get_stroke_width())
        shape1.stroke_width = 10
        shape1.set_fill(WHITE, opacity=1)

        self.play(ShowCreation(shape1))
        self.wait(0.5)
        self.play(ApplyMethod(shape1.shift, np.array([0, 2, 0])))
        self.play(ApplyMethod(shape1.shift, np.array([-1, 0, 0])))

        self.play(ApplyMethod(shape1.shift, np.array([0, -2, 0])))

        self.play(ApplyMethod(shape1.shift, np.array([1, 0, 0])))
        self.play(FadeOut(shape1))
        for i in range(len(a)):
            a[i] = TransformMatrix(T_shear, a[i])
        print(a)
        shape2 = Polygon(a[0], a[1], a[2], a[3])
        shape2.set_fill(GREEN, opacity=1)
        shape2.fill_opacity = 1;
        ##print(shape2.points)
        ##self.play(Transform(shape1,shape2))
        ##self.play(ApplyMethod(shape2.shift, np.array([0, 1, 0])))

    ##shape2 =


def TransformMatrix(TransMatrix, z):
    ## (1,3)
    z = z.reshape(3, 1)
    c = np.dot(TransMatrix, z)

    c = c.reshape(1, 3)
    return c


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))