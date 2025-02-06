import math
p = int(input("p = "))
t = int(input("t = "))
r = int(input("r = "))
s = ((p**(2-t)+1)/(3-abs(p+2*r+(r*t)))) + ((p+(2*r)+(r*t))**(2-p))
print("anser:", s)