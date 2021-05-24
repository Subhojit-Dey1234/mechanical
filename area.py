import math


def intersectionArea(a,b,x,y,r,R):
    dist = math.sqrt((x-a)**2 + (y-b)**2)
    x = (r**2 - R**2 + dist**2)/(2*dist)
    y = math.sqrt(r**2 - x**2)
    z = x **2
    return r * math.asin(y / r) + b * math.asin(y / R) - y * (x + math.sqrt(z + R -r))