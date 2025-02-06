def funk(a, b):
    c = ""
    d = a
    if a < 0:
        a = -a
        e = "-"
    elif a == 0:
        c = "0"
    else:
        e = ""
    while a > 0:
        f = int(a % 10) 
        c = chr(ord('0') + f) + c
        a //= 10
    if d < 0:
        c = e + c
    g = -1
    if '.' in str(d):
        g = str(d).find('.')
    h = ""
    if g != -1:
      i = g + 1
      while i < len(str(d)):
        h += str(d)[i]
        i += 1
    j = ""
    k = b
    if b < 0:
        b = -b
        l = "-"
    elif b == 0:
        j = "0"
    else:
        l = ""
    while b > 0:
        m = int(b % 10) 
        j = chr(ord('0') + m) + j
        b //= 10
    if k < 0:
        j = l + j
    if len(h) >= 2 and h[:2] == j:
        return True
    else:
        return False

a = float(input())
b = int(input())

print(funk(a,b))