# задание 1
import math
l, r, eps, = 0.0, 1.0, 0.0001
def f(x):
    return math.e**x - math.e**-x - 2
res = 0
while r-l > eps:
    if f(l) * f(r) > 0:
        print('Нет корней на этом отрезке')
        break
    b = l + (r-l) / 2
    if f(b) * f(l) < 0: # проверка на каком участке есть корень
        r = b
    else:
        l = b
    res = b
print(res)

# задание 2

import math
l, r, eps = 0.0, 1.0, 0.0001
def f(x):
    return math.e**x - math.e**-x - 2
step = 0
x = 0
while True:
    x = l - f(l) * (r - l) / (f(r) - f(l)) # формула для определения нового приближения корня
    step += 1
    if abs(f(x)) < eps:
        break
    if f(l) * f(x) < 0:
        r = x
    else:
        l = x
    if step > 1000:
        break
print(x)