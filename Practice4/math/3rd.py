import math 

s = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = (s * pow(l, 2)) / (4 * math.tan(math.pi/s))
print(f"The area of the polygon is: {round(area)}")