import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1
dx_squared = math.pow(dx, 2)
dy_squared = math.pow(dy, 2)
sum_squares = dx_squared + dy_squared
d = math.sqrt(sum_squares)

print("Distance: ", round(d, 2))

# Reflection:
# I applied the Euclidean distance formula in Python.
# I also learned how to use sqrt() and pow() from the math library.
#Finally, I tested my code in VS Code and saved it in GitHub.
