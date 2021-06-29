# calculate the area of a circle
import math
# import the librery math for pi
radius = int(input("insert the value of the circle's radius: "))

area = math.pi*radius**2
length = 2*math.pi*radius

print(f"the area is: {area:.2f}")
# data output with 2 decimals
# f means float
print(f"the length is: {length}")
