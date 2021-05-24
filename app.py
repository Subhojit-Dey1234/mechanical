
"""
    In the Code I have assumbed Circle with Radius R is within the rectangle

"""
import math
from area import intersectionArea
# taking the number of circles.
n =int(input("Enter the Number of circles"))

list_circles = []
# circle_inside = []
# circle_outside = []
# circle_intersecting = []

area = 0.0
#taking the inputs for the center of the circle
for i in range(0,n):
    x,y ,r = input('Enter the center of the circle ( in x,y and the radius) :').split()
    list_circles += [[float(x) , float(y) , float(r)]]

#Taking the input for the circle with Radius R
x , y = input('Enter the center of the circle with Radius R ( in x,y ) :').split()
circle = [float(x),float(y)]
R = float(input('Enter the Radius of the circle'))


for x in list_circles:
    dist = math.sqrt((x[0]-circle[0])**2 + (x[1]-circle[1])**2)
    if dist >= abs(R + x[2]):
        pass
    else:
        if dist <= abs(R-x[2]):
            area += math.pi * x[2] * x[2]
        else:
            area += intersectionArea(x[0],x[1],circle[0],circle[1],x[2],R)

print("The Area of the circle included", area)