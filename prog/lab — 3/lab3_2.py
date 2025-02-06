import math
x = int(input())
y = int(input())
z = int(input())
mas = [x,y,z]
u = ((max(mas)**2)-((2**x)*min(mas)))/((2 * math.sin(x) * math.cos(x))+max(mas)/min(mas))
print(u)
