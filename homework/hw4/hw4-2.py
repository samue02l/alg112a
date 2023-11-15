//迭代法
def f1(x):
    return (x*x + 1) / 3

def f2(x):
    return 1 / (2 * x) + 3

def f3(x):
    return 3 - (1 / x - 1)

x1 = x2 = x3 = 1

for i in range(20):
    x1 = f1(x1)
    x2 = f2(x2)
    x3 = f3(x3)

    print('x1:', x1, 'x2:', x2, 'x3:', x3)
