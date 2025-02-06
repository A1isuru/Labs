from math import gcd

def fraction(a, b, c):
    if b is False:
        b = 0 
    d = int(str(b) + str(c)) 
    g = len(str(c))
    d2 = '9' * g 
    if b != 0:
        j = len(str(b))
        d2 = int(d2 + '0' * j)  
    d -= b
    d1 = a * d2 + d
    d1 //= gcd(d1, d2)
    d2 //= gcd(d1, d2)
    return f"{d1}/{d2}"

a = int(input())
b = int(input())
c = int(input())
print(fraction(a, b, c))
    