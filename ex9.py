import math

def isPitag(a, b, c):
    if a<b and b<c and a**2 + b**2 == c**2:
        return True
    else:
        return False

for a in range(1, 1000):
    for b in range (a, 1000):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(f"a: {a}  b: {b}  c:{int(c)}")
            print(a*b*c)