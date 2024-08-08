from sympy import symbols, expand, factor, Eq, solve, diff, integrate

# 変数の定義
x, y = symbols('x y')

# 式の操作
expr = (x + y) ** 2
expanded_expr = expand(expr)
factored_expr = factor(expanded_expr)

# 方程式の解法
equation = Eq(x ** 2 + 2 * x + 1, 0)
solutions = solve(equation, x)

# 微分と積分
f = x ** 2 + x
derivative = diff(f, x)
integral = integrate(f, (x, 0, 1))

# 結果の表示
print(f"展開: {expanded_expr}")
print(f"因数分解: {factored_expr}")
print(f"方程式の解: {solutions}")
print(f"微分: {derivative}")
print(f"積分: {integral}")
