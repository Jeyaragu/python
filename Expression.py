import math

# Area of triangle
height = 1
base = 2
triangle = (base * height)/2

# Area of Trapezium
a = 1
b = 2
h = 10
trapezium = ((a+b)*h)/2

# Area of circle 
r = 5
circle = math.pi * r**2

# Conver km to miles
kms = 10
kmToMiles = kms * 0.621371

# Displacement
u = 2 # Initial velocity
v = 10 # Final velocity
a = 10 # Acceleration
d = ((v**2)- (u**2))/(2*a)

# Area of Rectangle
length = int(input('Enter Length:'))
breath = int(input('Enter Breath:'))
rectAngle = length * breath
print('Area of Rectangle:',rectAngle)