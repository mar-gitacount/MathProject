import sympy as sp

# logmeshod
# "The first argument of the log method is the argument 
# (the number or expression whose logarithm is being taken), and the second argument is the base."

# 1. log_2(3) = a, log_3(7) = b とするとき、log_42(56) を a, b で表す。
a = sp.symbols('a')
b = sp.symbols('b')

log_2_3 = sp.log(3, 2)
log_3_7 = sp.log(7, 3)

testlog = sp.log(8,2)
print(testlog)

# a*b = log2_7になる。

# log_2(3) = a より a = log(3, 2)
# log_3(7) = b より b = log(7, 3)
# log_42(56) を a, b で表す
log_42_56 = sp.log(56, 42)

# 変数 a, b を使って表現
log_42_56_in_ab = log_42_56.subs({sp.log(3, 2): a, sp.log(7, 3): b})
print(f"log_42(56) = {log_42_56_in_ab}")

# 2. log_10(6) = 0.7782, log_10(12) = 1.0792 とするとき、log_10(2), log_10(3) の値を求める。
log_10_6 = 0.7782
log_10_12 = 1.0792

# log_10(6) = log_10(2 * 3) = log_10(2) + log_10(3)
# log_10(12) = log_10(3 * 4) = log_10(3) + log_10(4)
log_10_2, log_10_3 = sp.symbols('log_10_2 log_10_3')

# 方程式を解く
eq1 = sp.Eq(log_10_6, log_10_2 + log_10_3)
eq2 = sp.Eq(log_10_12, log_10_2 + sp.log(4, 10))

solutions = sp.solve((eq1, eq2), (log_10_2, log_10_3))
print(f"log_10(2) = {solutions[log_10_2]}")
print(f"log_10(3) = {solutions[log_10_3]}")
