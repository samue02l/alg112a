//暴力法
import math
def f(x):
    return x*x - 3*x + 1

for x in range(-100, 100, 1):
    if abs(f(x)) < 0.001:
    print("x=", x, " f(x)=", f(x))
