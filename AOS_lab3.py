import math
import inspect

x = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
y = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]

inf = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
inf_ = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def cos(n):
    return math.cos(n[0])


def ln(n):
    return math.log(n[0], math.e)


def plus(n, m=0):
    res = [0] * 11
    if n[0][0] ^ n[1][0]:
        print('yes')
        return minus(n)
    buf1 = 0
    for k in range(10, 1, -1):
        res[k] = (n[0][k] + n[1][k]) % 2
        buf1 = (n[0][k] + n[1][k]) / 2
    res[0] = n[0][0]
    if buf1:
        ############
        for h in range(10, 1, -1):
            res[h] = (res[h] + 1) % 2
        res[0] = (res[0] + 1) % 2
        res = plus([[(res[0] + 1) % 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], res])
   #########################
    return res


def abs_equals_or_larger(n, m=0):
    for l in range(2, 10):
        if n[0][l] > n[1][l]:
            return True
        if n[0][l] < n[1][l]:
            return False
    return True


def abs_equals(n, m=0):
    for m in range(2, 10):
        if n[0][m] != n[1][m]:
            return False
    return True


# plus([x, y])
def minus(n, m=0):
    res = [0] * 11
    if not abs_equals_or_larger(n):
        n.reverse()
        return minus(n)
    for p in range(10, 1, -1):
        if n[0][p] < n[1][p]:
            n[0][p-1] -= 1
            n[0][p] += 2
        res[p] = n[0][p] - n[1][p]
    if n[0][1] == -1:
        "Some error occurred"
    res[0] = n[0][0]
    return res


def div(n, m=0):
    return n[0] / n[1]


def mult(n, m=0):
    if n[1] == -1:
        n[0][0] = (n[0][0] + 1) % 2
        return n[0]
    return 0


def converter(n):
    if n[1]:
        pass
    else:
        res = int(''.join([str(elem) for elem in n[2:11]]), 2)
        if n[0]:
            res += -1
        return res


print(converter(x))

x = 5
y = 9
a = [mult, 7, div, plus, math.pi, ln, x, cos, y]
j = len(a) - 1
while j >= 0:
    if isinstance(a[j], bytes) or isinstance(a[j], float) or isinstance(a[j], int):
        buf = a.pop(j)
        a.append(buf)
    else:
        arg = []
        func = a.pop(j)
        for i in range(len(inspect.getfullargspec(func)[0])):
            arg.append(a.pop())
        a.append(func(arg))
    j -= 1

print(a[0])
