import numpy as np

def pascal_triangle(n):
    triangle = np.zeros((n, n), dtype=int)
    for i in range(n):
        triangle[i, 0] = 1
        for j in range(1, i+1):
            triangle[i, j] = triangle[i-1, j-1] + triangle[i-1, j]
    return triangle

def pascal_pyramid(n):
    pyramid = []
    for i in range(1, n+1):
        triangle = pascal_triangle(i)
        pyramid.append(triangle)
    return pyramid

def print_pyramid(pyramid):
    for level, triangle in enumerate(pyramid):
        print(f"Level {level + 1}:")
        for row in triangle:
            print(" ".join(map(str, row)).rstrip("0").rstrip())
        print("\n")

# ピラミッドのレベル数
n_levels = 5

# ピラミッドを生成
pyramid = pascal_pyramid(n_levels)

# ピラミッドを表示
print_pyramid(pyramid)
