import sympy as sp 
from sympy import diff



# Define symbolic variable
x = sp.Symbol('x')

# Define the loss function
L = 3*x**2 + 2*x - 5

# Compute the first derivative (gradient)
gradient = sp.diff(L, x)

# Solve for x when gradient is zero
optimal_solution = sp.solve(gradient, x)

# Compute the second derivative
second_derivative = sp.diff(gradient, x)

# Check if it's a minimum or maximum
critical_point = optimal_solution[0]
nature = "Minimum" if second_derivative.subs(x, critical_point) > 0 else "Maximum"

# Print results
print("Gradient (dL/dx):", gradient)
print("Optimal x:", critical_point)
print("Second Derivative:", second_derivative)
print("Nature of Critical Point:", nature)
