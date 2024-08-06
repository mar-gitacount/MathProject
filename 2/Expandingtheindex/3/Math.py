from fractions import Fraction

# 分数に変換する。
# 第一引数に分子、第二引数に分母をいれる
def FractionMake(molecule,denominator):
    fraction_result = Fraction(1,molecule**denominator)
    return fraction_result



testresult = FractionMake(9,3)
result = Fraction((3**2)**-3)
fraction_result = Fraction(1, 9 ** 3)
quesion1 = (FractionMake(9,3)*(3 ** 3)/(FractionMake(9,2)))
print(quesion1)
