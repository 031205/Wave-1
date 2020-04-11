length = int(input('Input the length of the field in feet:'))
width = int(input('Input the width of the field in feet:'))
area = length*width
acre = float(area/43560)
print('The area of the field is',acre,'acres')