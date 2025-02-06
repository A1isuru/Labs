import math
x = int(input("x = "))
y = int(input("y = "))

num = ((math.sin(x) + math.cos(y)) / (math.cos(x) - math.sin(y)))*math.tan(x*y)
num_1 = (1+(1/x**2))-12*(x**2)*y
print("первая фопмула: ",num," вторая формула:",num_1)