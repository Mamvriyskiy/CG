from math import sin, cos
import numpy as np

def create_picture():
    big_circle = create_circle(20, 20)                              #внешний круг
    small_circle = create_circle(16, 16)                            #средний круг
    smaller_circle = create_circle(2, 2)                            #маленький круг

    first_line = create_right_line(1.52, 12.8, 1.52, 9.6);          #правая верхняя линия
    second_line = create_right_line(-1.52, -12.8, -1.52, -9.6);     #левая нижняя линия
    third_line = create_right_line(1.52, 12.8, -1.52, -9.6);        #праввая нидняя линия
    fourth_line =  create_right_line(-1.52, -12.8, 1.52, 9.6);      #левая вернхняя линия

    first_smaller_circle = create_circle_center(18, 0, 2, 2)
    first_smaller_line = create_lines(-1, 0, 1, 17, 18, 19)

    second_smaller_circle = create_circle_center(-18, 0, 2, 2)
    second_smaller_line = create_lines(-17, -18, -19, 1, 0, -1)

    third_smaller_circle = create_circle_center(0, 18, 2, 2)
    thitd_smaller_line = create_lines(17, 18, 19, -1, 0, 1)

    fourth_smaller_circle = create_circle_center(0, -18, 2, 2)
    fourth_smaller_line = create_lines(1, 0, -1, -17, -18, -19)

    left_foot = create_foot(0, 0, -20, -32, -12, -32)               #левая нога
    right_foot = create_foot(0, 0, 20, -32, 12, -32)                #правая нога

    picture = [big_circle, small_circle, smaller_circle, first_line, second_line, \
            third_line, fourth_line, first_smaller_circle, first_smaller_line, \
            second_smaller_circle, second_smaller_line, third_smaller_circle, \
            thitd_smaller_line, fourth_smaller_circle, fourth_smaller_line,\
                left_foot, right_foot]

    return picture

def create_lines(a, b, c, d, e, f):
    x_list = [e, f, d, e, d, f]
    y_list = [b, c, a, b, c, a]

    return [x_list, y_list]



def create_foot(a_x, a_y, b_x, b_y, c_x, c_y):
    x_list = [a_x, b_x, c_x, a_x]
    y_list = [a_y, b_y, c_y, a_y]
    
    return [x_list, y_list]


def create_circle_center(c_x, c_y, a, b):
    x_list = []
    y_list = []
    angles = np.linspace(0, 360, 360)
    for angle in angles:
        x_list.append(a * cos(np.radians(angle)))
        y_list.append(b * sin(np.radians(angle)))
    
    x_list = [x - c_x for x in x_list]
    y_list = [y - c_y for y in y_list]

    return [x_list, y_list]
    
def create_circle(a, b):
    x_list = []
    y_list = []
    angles = np.linspace(0, 360, 360)
    for angle in angles:
        x_list.append(a * cos(np.radians(angle)))
        y_list.append(b * sin(np.radians(angle)))
    

    return [x_list, y_list]

def create_right_line(a, b, c, d):
    x_list = [a, b]
    y_list = [c, d]

    return [x_list, y_list]

    


