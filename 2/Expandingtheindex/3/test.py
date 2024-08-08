from sympy import symbols, expand, factor, Eq, solve, diff, integrate, init_printing
from IPython.display import display
# 初期化
init_printing()

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
# 積分する式
expression = 3 * x ** 2

# 積分計算
integral_result = integrate(expression, x)

# 結果の表示
integral_result
display(integral_result)
# 結果の表示
expanded_expr, factored_expr, equation, solutions, derivative, integral
