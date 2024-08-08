from fractions import Fraction
import math
from sympy import symbols, sqrt
def FractionMake(numerator, denominator):
    # 分子=numerator 分母=denominator
    return Fraction(numerator, denominator)

question1 = 3 ** (-6+3+4)
question2 = 25 ** Fraction(FractionMake(1,4) + FractionMake(1,3) - FractionMake(1,12))
question3 = 3 ** Fraction(1,2)

heihouonn = math.sqrt(3)
print(heihouonn * heihouonn)
# ここで数式を設定する？
# print(question1)
# print(question2)
# print(question3)