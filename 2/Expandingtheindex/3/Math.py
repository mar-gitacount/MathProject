from fractions import Fraction

def FractionMake(numerator, denominator):
    return Fraction(numerator, denominator)

# 計算
question2 = ((FractionMake(FractionMake(1, 4), 25) * 
             FractionMake(FractionMake(1, 3), 25)) / 
             FractionMake(FractionMake(1, 12),25))

print(question2)
