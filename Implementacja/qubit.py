import numpy as np
import math
import random

from complex import Complex, PolarToComplex

def randomQ():
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    while a**2 > 1 - b**2:
        a = random.uniform(-1, 1)
        b = random.uniform(-1, 1)
    alpha = Complex(a, b)
    # print(abs(alpha**2))
    abs_beta = math.sqrt(1 - abs(alpha)**2)
    # print(abs_beta**2)
    c = random.uniform(-1, 1)
    d = abs_beta**2 - c
    while c > 1 - a**2:
        c = random.uniform(-1, 1)
    d = (abs_beta**2 - c**2)**0.5
    beta = Complex(c, d)
    return Qubit(alpha, beta)

def Hadamard():
    return np.array([[Complex(1/np.sqrt(2), 0), Complex(1/np.sqrt(2), 0)],
                    [Complex(1/np.sqrt(2), 0), Complex(-1/np.sqrt(2), 0)]])

def PauliX():
    return np.array([[Complex(0, 0), Complex(1, 0)],
                    [Complex(1, 0), Complex(0, 0)]])

def PauliY():
    return np.array([[Complex(0, 0), Complex(0, -1)],
                    [Complex(0, 1), Complex(0, 0)]])

def PauliZ():
    return np.array([[Complex(1, 0), Complex(0, 0)],
                    [Complex(0, 0), Complex(-1, 0)]])

def Sgate():
    return np.array([[Complex(1, 0), Complex(0, 0)],
                    [Complex(0, 0), Complex(0, 1)]])
def SNgate():
    return np.array([[Complex(1, 0), Complex(0, 0)],
                    [Complex(0, 0), Complex(0, -1)]])

def Tgate():
    return np.array([[Complex(1, 0), Complex(0, 0)],
                    [Complex(0, 0), PolarToComplex(1, -45)]])

def TNgate():
    return np.array([[Complex(1, 0), Complex(0, 0)],
                    [Complex(0, 0), PolarToComplex(1, 45)]])

class Qubit:
    def __init__(self, alpha, beta):
        if 0.999999998 <= abs(alpha)**2 + abs(beta)**2 <= 1.00000001:
            self.alpha = alpha
            self.beta = beta
        else:
            print('Error')

    def __mul__(self, gate):
        alpha = gate[0, 0] * self.alpha + gate[0, 1] * self.beta
        beta = gate[1, 0] * self.alpha + gate[1, 1] * self.beta
        return Qubit(alpha, beta)





# print(0.4677056485736148 + 0.5322943514263851)
a = Complex(1/np.sqrt(2), 0)
# a = Complex(a, 0)
# # print(a**2+a**2)
# # print(a)
q = Qubit(a, a)
# # q1 = Qubit.randomQ()
# q1 = randomQ()
# print(q.alpha)
# print(q.beta)
# print("-----------")
# print(q1.alpha)
# print(q1.beta)

H = Hadamard()
PX = PauliX()
PY = PauliY()
# print(PY)
# print(PY[0, 1])
PZ = PauliZ()
SG = Sgate()
TG = Tgate()
SNG = SNgate()
TNG = TNgate()

new_qH = q * H

new_qX = new_qH * PX
new_qY = new_qX * PY
# print(new_qH.alpha)
# print(new_qH.beta)
# print(new_qX.alpha)
# print(new_qX.beta)
print(new_qY.alpha)
print(new_qY.beta)

# Tg = q * PZ
# print(Tg.alpha)
# print(Tg.beta)

# TNrand = q1 * TNG
# print(TNrand.alpha)
# print(TNrand.beta)

# print(Complex(0, -1) * Complex(1, 0))
