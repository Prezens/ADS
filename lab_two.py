import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

function = lambda x: 8 * x ** 3 - 36 * x ** 2 + 54 * x - 27

a1 = float(input('Введите a границу отрезка: '))
b1 = float(input('Введите b границу отрезка: '))
e = float(input('Введите e заданную точность: '))
dot = None


def bisection_method(a, b, f):
    x = (a + b) / 2

    while np.abs(a - b) >= e:
        x = (a + b) / 2
        if f(a) * f(x) > 0:
            a = x
        elif f(a) * f(x) < 0:
            b = x

    global dot
    dot = (f(x), x)

    return x


X = np.arange(-15.0, 20.0, 1)
section = np.linspace(a1, b1)

solve = bisection_method(a1, b1, function)

solves = fsolve(function, np.arange(a1, b1))
print('Корни уравнения найденные с помощью библиотеки scipy:', solves)

if np.round(function(solve), 3) == 0:
    print('Корень уравнения: %s' % solve)
else:
    print('Корень уравнения на данном отрезке не найден')

plt.plot([x for x in X], [function(x) for x in X])
plt.plot(dot[1], dot[0], color='green', marker='o', linestyle='dashed', markersize=12)
plt.plot(section, function(section))
plt.grid(True)

plt.show()
