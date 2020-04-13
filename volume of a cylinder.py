import math
radius = int(input('Input the radius of the cylinder:'))
height = int(input('Input the height of the cylinder:'))
pi = math.pi
circularbase = pi*radius*radius
volume = circularbase*height
volume2 = round(volume,1)
print('The volume of the cylinder is',volume2)
