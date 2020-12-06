import math
import inspect


inf = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
inf_ = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def conv(mnt):
    mnt_norm = mnt % 1 - mnt // 1 % 2
    sign = 1 if str(mnt_norm)[0] == "-" else 0
    mnt_bin = [sign, 0]
    mnt_norm = abs(mnt_norm)
    if mnt_norm == 1:
        mnt_bin += [1, 1, 1, 1, 1, 1, 1]
    else:
        for i in range(7):
            mnt_bin.append(int(mnt_norm * 2 // 1))
            mnt_norm = mnt_norm * 2 % 1
    return mnt_bin


def in_params(arg):
    if True:
        if arg.replace(".", "", 1).isdigit() or (arg[0] == "-" and arg[1:].replace(".", "", 1).isdigit()):
            arg_bin = conv(float(arg))
        elif arg == "inf" or arg == "+inf":
            arg_bin = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif arg == "-inf":
            arg_bin = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif arg == "qNaN":
            arg_bin = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        else:
            arg_bin = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return arg_bin


def converter(n):
    if n[1]:
        if n[2:11] == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
            res = "inf"
            if n[0]:
                res = "-" + res
        else:
            res = "NaN"
            if not n[0]:
                res = "q" + res
    else:
        if n[2:].count(1) == 9:
            res = 1
        else:
            res = 0
            it = 1
            for m in n[2:]:
                res += m * (0.5 ** it)
                it += 1
        if n[0]:
            res *= -1
        return res


def to_float(args):
    i = 0
    for bits in args:
        args[i] = converter(bits)
        i += 1
    return args


def cos(n):
    n = to_float(n)
    return in_params(str(math.cos(n[0])))


def ln(n):
    n = to_float(n)
    return in_params(str(math.log(n[0], math.e)))


def plus(n, m=0):
    n = to_float(n)
    return in_params(str(n[0] + n[1]))


def div(n, m=0):
    n = to_float(n)
    return in_params(str(n[0] / n[1]))


def mult(n, m=0):
    n = to_float(n)
    return in_params(str(n[0] * n[1]))


x = input("X: ")
y = input("Y: ")
print()

print("Processor work starts...")
a = [mult, in_params(str(7)), div, plus, in_params(str(math.pi)), ln, in_params(x), cos, in_params(y)]
a_str = ['mult', '7', 'div', 'plus', 'pi', 'ln', x, 'cos', y]
print(a_str)
try:
    j = len(a) - 1
    while j >= 0:
        if isinstance(a[j], list):
            buf = a.pop(j)
            a.append(buf)
            buf = a_str.pop(j)
            a_str.append(buf)
            print(f"Push({buf})")
        else:
            arg = []
            func = a.pop(j)
            print(a_str.pop(j), end='(')
            for i in range(len(inspect.getfullargspec(func)[0])):
                if i:
                    print(', ', end=' ')
                arg.append(a.pop())
                print(a_str.pop(), end='')
            print(')')
            a.append(func(arg))
            a_str.append(str(to_float(a[len(a)-1:])[0]))
        j -= 1
        print(a_str)
except ValueError:
    print("\nNumbers printed do not suit the functions domain")
except TypeError:
    print("\nX and Y are numbers, not letters. If you typed + in positive numbers reduce them.")
else:
    print(f"...processor work ends.\n\nResult: {a_str[0]}")
