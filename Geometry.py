#  File: Geometry.py

#  Description: Creates a advanced geometry class with various functions and tests whether many shapes fit inside of other shapes or not (ex: cylinder inside sphere)

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Partner Name: Saivachan Ponnapalli

#  Partner UT EID: sp48347

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 09/12/2022

#  Date Last Modified: 09/16/2022

import sys

import math


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return "(" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(float(self.z)) + ")"

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.hypot(abs(self.x - other.x), abs(self.y - other.y), abs(self.z - other.z))

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False


class Sphere(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.center = Point(x, y, z)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return "Center: (" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(
            float(self.z)) + "), Radius: " + str(float(self.radius))

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        # The area of a sphere is 4 pi r^2
        return 4 * math.pi * pow(self.radius, 2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        # The volume of a sphere is 4/3 pi r^3
        return (4 / 3) * math.pi * pow(self.radius, 3)

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        # This determines whether a point is within a sphere based on the distance of the point from the center. If the distance is greater than the radius, it is outside
        distance = math.hypot(self.x - p.x, self.y - p.y, self.z - p.z)
        if distance <= self.radius:
            return True
        else:
            return False

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        # The distance from the center of the bigger sphere to the center of the smaller sphere is calculated. If that distance + radius of the smaller sphere is less than the radius of the bigger sphere, then the sphere is within a sphere
        if (self.center.distance(other.center) + other.radius) < self.radius:
            return True
        else:
            return False

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        # The 8 edges of a cube are calculated based on the side. Adding and subtracting half of the side gives xyz coordinates
        half_side = a_cube.side / 2

        x_right = a_cube.x + half_side
        x_left = a_cube.x - half_side
        y_right = a_cube.y + half_side
        y_left = a_cube.y - half_side
        z_right = a_cube.z + half_side
        z_left = a_cube.z - half_side

        # point objects are made based on the edges
        point_1 = Point(x_right, y_right, z_right)
        point_2 = Point(x_left, y_left, z_left)
        point_3 = Point(x_right, y_right, z_left)
        point_4 = Point(x_left, y_left, z_right)
        point_5 = Point(x_right, y_left, z_left)
        point_6 = Point(x_left, y_right, z_right)
        point_7 = Point(x_right, y_left, z_right)
        point_8 = Point(x_left, y_right, z_left)

        # The distance from the center of the sphere to each of the points is calculated. The cube is in the circle if distance is less than the radius of the circle
        if self.center.distance(point_1) < self.radius and self.center.distance(
                point_2) < self.radius and self.center.distance(point_3) < self.radius and self.center.distance(
            point_4) < self.radius and self.center.distance(point_5) < self.radius and self.center.distance(
            point_6) < self.radius and self.center.distance(point_7) < self.radius and self.center.distance(
            point_8) < self.radius:
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        # The diagonal of the cylinder is calculated
        diagonal = math.hypot(a_cyl.height / 2, a_cyl.radius)
        distance_circle_cyl = self.center.distance(a_cyl)
        # It is inside the sphere if the distance from the center of the sphere and the center of the cylinder + radius of the cylinder is less than the radius of the sphere
        if (diagonal + distance_circle_cyl < self.radius):
            return True
        else:
            return False

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        # A sphere intersects with other sphere when the distance between the two radii are not greater than both radii added together and the function is_inside_sphere returns false
        distance_two_spheres = self.center.distance(other.center)
        if (self.is_inside_sphere(other)) == False and distance_two_spheres < self.radius + other.radius:
            return True
        else:
            return False

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        # The cube intersects the sphere when is_inside_cube returns false and the distance between the center of the circle and center of the cube is less than the radius and 1/2 side added together
        distance_cube_sphere = self.center.distance(a_cube)
        if (self.is_inside_cube(a_cube) == False) and distance_cube_sphere < self.radius + (a_cube.side / 2):
            return True
        else:
            return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    # Test Failed: 'Cube' object has no attribute 'center'
    def circumscribe_cube(self):
        return Cube(self.x, self.y, self.z, self.radius * 2 / math.sqrt(3))


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = x
        self.y = y
        self.z = z
        self.side = side
        self.center = Point(self.x, self.y, self.z)

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return "Center: (" + str(float(self.x)) + (", ") + str(float(self.y)) + (", ") + str(
            float(self.z)) + "), Side: " + str(float(self.side))

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        # area = 6 side^2
        return pow(self.side, 2) * 6

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        # volume = side^3
        return pow(self.side, 3)

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        # This determines whether a point is within a sube based on the distance of the point from the center. If the distance is greater than the 1/2 side, it is outside
        half_side = (self.side) / 2
        if (abs(p.x - self.x) <= half_side and abs(p.y - self.y) <= half_side and abs(p.z - self.z) <= half_side):
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # If the distance between the center of the cube and the center of the sphere + radius of the sphere is less than 1/2 side of cube, the sphere is inside the cube
        x = a_sphere.x
        y = a_sphere.y
        z = a_sphere.z
        dis_center = self.center.distance(a_sphere.center)
        return dis_center + a_sphere.radius < (self.side) / 2

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        # This calculates the distance between the x, y, and z. If all the distances are less than 1/2 side of the bigger cube, it is inside the cube
        other_half_side = other.side / 2
        half_side = self.side / 2

        x_right = other.x + other_half_side
        x_left = other.x - other_half_side
        y_right = other.y + other_half_side
        y_left = other.y - other_half_side
        z_right = other.z + other_half_side
        z_left = other.z - other_half_side

        # point objects are made based on the edges
        point_1 = Point(x_right, y_right, z_right)
        point_2 = Point(x_left, y_left, z_left)
        point_3 = Point(x_right, y_right, z_left)
        point_4 = Point(x_left, y_left, z_right)
        point_5 = Point(x_right, y_left, z_left)
        point_6 = Point(x_left, y_right, z_right)
        point_7 = Point(x_right, y_left, z_right)
        point_8 = Point(x_left, y_right, z_left)

        new_x = self.x + half_side
        new_y = self.y + half_side
        new_z = self.z + half_side
        point_bigger = Point(new_x, new_y, new_z)

        hypotenuse = self.center.distance(point_bigger)

        if (self.center.distance(point_1) < hypotenuse) and (self.center.distance(point_2) < hypotenuse) and (self.center.distance(point_3) < hypotenuse) and (
                self.center.distance(point_4) < hypotenuse) and (self.center.distance(point_5) < hypotenuse) and (self.center.distance(point_6) < hypotenuse) and (
                self.center.distance(point_7) < hypotenuse) and (self.center.distance(point_8) < hypotenuse):
            return True
        else:
            return False

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        # If the distance between the x, y, z, and the cylinder and the square + radius is less than half the side of the cube, the cylinder is in the cube
        var1 = abs(self.x - a_cyl.x) + a_cyl.radius < self.side / 2
        var2 = abs(self.y - a_cyl.y) + a_cyl.radius < self.side / 2
        var3 = abs(self.z - a_cyl.z) + a_cyl.height / 2 < self.side / 2
        return var1 and var2 and var3

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        # The cubes intersect as long as is_inside_cube returns false and the distance between the center of the two cubes is less than 1/2 of both sides added together
        if not (self.is_inside_cube(other)) and not (other.is_inside_cube(self)):
            x = other.x
            y = other.y
            z = other.z
            sidel = other.side / 2
            if self.is_inside_point(Point(x + sidel, y + sidel, z + sidel)) or self.is_inside_point(
                    Point(x + sidel, y + sidel, z - sidel)) or self.is_inside_point(
                    Point(x + sidel, y - sidel, z + sidel)) or self.is_inside_point(
                    Point(x + sidel, y - sidel, z - sidel)) or self.is_inside_point(
                    Point(x - sidel, y + sidel, z + sidel)) or self.is_inside_point(
                    Point(x - sidel, y + sidel, z - sidel)) or self.is_inside_point(
                    Point(x - sidel, y - sidel, z + sidel)) or self.is_inside_point(
                    Point(x - sidel, y - sidel, z - sidel)):
                return True
        return False

        # determine the volume of intersection if this Cube
        # intersects with another Cube
        # other is a Cube object
        # returns a floating point number
    def intersection_volume(self, other):
        # The volume is determined by seeing where the points overlap in the xyz plane.
        c1_a = (self.x + self.side / 2, self.y + self.side / 2, self.z + self.side / 2)
        c1_b = (self.x - self.side / 2, self.y - self.side / 2, self.z + self.side / 2)
        c2_a = (other.x + other.side / 2, other.y + other.side / 2, other.z + other.side / 2)
        c2_b = (other.x - other.side / 2, other.y - other.side / 2, other.z - other.side / 2)
        max1 = max(min(c2_a[0], c1_a[0]) - max(c2_b[0], c1_b[0]), 0)
        max2 = max(min(c2_a[1], c1_a[1]) - max(c2_b[1], c1_b[1]), 0)
        max3 = max(min(c2_a[2], c1_a[2]) - max(c2_b[2], c1_b[2]), 0)
        return max1 * max2 * max3

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        # A sphere object is returned based on the center of the cube. The radius is set based on half of the side of the cube
        side_half = self.side / 2
        return Sphere(self.x, self.y, self.z, side_half)


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height
        self.center = Point(x, y, z)

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return "Center: (" + str(float(self.x)) + ", " + str(float(self.y)) + ", " + str(
            float(self.z)) + "), Radius: " + str(float(self.radius)) + ", Height: " + str(float(self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        # area = (2 pi height radius) + (2 pi radius^2)
        return (2 * math.pi * self.height * self.radius) + (2 * math.pi * pow(self.radius, 2))

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        # volume = pi r^2 height
        return math.pi * pow(self.radius, 2) * self.height

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        # the point is inside the cyl if the x,y distance for the point is less than the radius of the cylinder and the z distance is less than 1/2 the height of the cyl
        if abs(self.x - p.x) < self.radius and abs(self.y - p.y) < self.radius and abs(self.z - p.z) < (
                self.height / 2):
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # The sphere is inside if the distance of the center of the sphere and cyl of x,y + radius of the sphere is less than the radius of the cyl. Z must be less than half height
        if (abs(self.x - a_sphere.x) + a_sphere.radius) < self.radius and (
                abs(self.y - a_sphere.y) + a_sphere.radius) < self.radius and (
                abs(self.z - a_sphere.z) + a_sphere.radius) < (self.height / 2):
            return True
        else:
            return False

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        # distance of x and y from the center of the cube and the sylinder + half of side must be less than the radius. Z + half of side must be less than the height.
        half_side = a_cube.side / 2
        if (abs(self.x - a_cube.x) + half_side) < self.radius and (
                abs(self.y - a_cube.y) + half_side) < self.radius and (
                abs(self.z - a_cube.z) + half_side) < (self.height / 2):
            return True
        else:
            return False

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        # distance of x and y from the center of the cylinder and the other cylinder + half of side must be less than the radius. Z + half of side must be less than the height.
        if (abs(self.x - other.x) + other.radius) < self.radius and (
                abs(self.y - other.y) + other.radius) < self.radius and (
                abs(self.z - other.z) + (other.height / 2)) < self.height / 2:
            return True
        else:
            return False

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        # The distance between x,y must be less than radius. distance between z must be less than 1/2 height
        return math.dist((self.x, self.y), (other.x, other.y)) <= self.radius + other.radius and abs(
            self.z - other.z) <= (self.height + other.height) / 2


def main():
    # read data from standard input
    data = sys.stdin

    # read the coordinates of the first Point p
    data_1 = str(data.readline().strip())
    data_1 = data_1.split(" ")
    data_12 = list()
    for i in range(0, 3):
        data_12.append(float(data_1[i]))

    # create a Point object
    pointp = Point(data_12[0], data_12[1], data_12[2])

    # read the coordinates of the second Point q
    data_2 = str(data.readline().strip())
    data_2 = data_2.split()
    data_23 = list()
    for i in range(0, 3):
        data_23.append(float(data_2[i]))

    # create a Point object
    pointq = Point(data_23[0], data_23[1], data_23[2])

    # read the coordinates of the center and radius of sphereA
    data_3 = str(data.readline().strip())
    data_3 = data_3.split()
    data_34 = list()
    for i in range(0, 4):
        data_34.append(float(data_3[i]))

    # create a Sphere object
    sphereA = Sphere(data_34[0], data_34[1], data_34[2], data_34[3])

    # read the coordinates of the center and radius of sphereB
    data_4 = str(data.readline().strip())
    data_4 = data_4.split()
    data_45 = list()
    for i in range(0, 4):
        data_45.append(float(data_4[i]))

    # create a Sphere object
    sphereB = Sphere(data_45[0], data_45[1], data_45[2], data_45[3])

    # read the coordinates of the center and side of cubeA
    data_5 = str(data.readline().strip())
    data_5 = data_5.split()
    data_56 = list()
    for i in range(0, 4):
        data_56.append(float(data_5[i]))
