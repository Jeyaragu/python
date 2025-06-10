import math
# a, b and c are called coefficients
a = 1
b = -5
c = 6
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
# x1 and x2 are roots. Basically the possible value
x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print(x1)
print(x2)