import math
import matplotlib.pyplot as plt
import numpy as np

function = lambda x: 8 * x ** 3 - 36 * x ** 2 + 54 * x - 27

a1 = float(input('Введите a границу отрезка: '))
b1 = float(input('Введите b границу отрезка: '))
e = 0.001
dot = None


def bisection_method(a, b, f):
    x = (a + b) / 2

    while math.fabs(f(x)) >= e:
        x = (a + b) / 2
        print('%.6f' % f(x))
        if f(a) * f(x) < 0:
            a, b = a, x
        else:
            a, b = x, b

    global dot
    dot = (f(x), x)

    return (a + b) / 2


X = np.arange(-15.0, 20.0, 0.1)
print([function(x) for x in X])
plt.plot([x for x in X], [function(x) for x in X])
plt.grid(True)

print('Корень уравнения: %s' % bisection_method(a1, b1, function))
plt.plot(dot[1], dot[0], color='green', marker='o', linestyle='dashed', markersize=12)
plt.show()
