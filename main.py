import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def kernel_density(x, h):
    x.sort()
    t = np.linspace(x[0] - h, x[len(x) - 1] + h,
                    (math.ceil(x[len(x) - 1]) - math.floor(x[0])) * 100)
    Jt = [J(a, h, x) for a in t]
    plt.plot(t, Jt)
    plt.show()


def J(a, h, x):
    den = (len(x) * h)
    s = 0
    for item in x:
        s += w((item - a) / h)
    return s / den


def w(u):
    if abs(u) > 1 / 2:
        return 0
    return 1 + math.cos(2 * math.pi * u)


path = "./assets/grades (1).csv"
df = pd.read_csv(path)


# Q2

# mathGrades = df["math"].tolist()
# kernel_density(mathGrades, 2)
# kernel_density(mathGrades, 5)
# # kernel_density(mathGrades, 7)
# kernel_density(mathGrades, 10)
# kernel_density(mathGrades, 15)
# kernel_density(mathGrades, 20)
# Q4

def kernel_density_mult(xlist, h):
    for x in xlist:
        x.sort()
        t = np.linspace(x[0] - h, x[len(x) - 1] + h,
                        (math.ceil(x[len(x) - 1]) - math.floor(x[0])) * 100)
        Jt = [J(a, h, x) for a in t]
        plt.plot(t, Jt)
    plt.show()
#
#
mathGradesA = df[df["school"] == "A"]["math"].tolist()
mathGradesB = df[df["school"] == "B"]["math"].tolist()
mathGradesC = df[df["school"] == "C"]["math"].tolist()
kernel_density_mult([mathGradesA, mathGradesB, mathGradesC], 10)
#Q5
gymGrades = df["gym"].tolist()
kernel_density(gymGrades, 10)
gymGradesA = df[df["school"] == "A"]["gym"].tolist()
gymGradesB = df[df["school"] == "B"]["gym"].tolist()
gymGradesC = df[df["school"] == "C"]["gym"].tolist()
kernel_density_mult([gymGradesA, gymGradesB, gymGradesC], 10)








res =sc.poisson.isf(0.9, 20)
if sc.poisson.cdf(res,20)>0.1:
    res--
print(res)


