import sympy as sp

# Define symbolic variable
x = sp.Symbol('x')

# Define the cost function
C = 5*x**3 - 10*x**2 + 4*x + 3

# Compute first derivative
dC_dx = sp.diff(C, x)

# Solve for x when dC/dx = 0
critical_points = sp.solve(dC_dx, x)

# Compute second derivative
d2C_dx2 = sp.diff(dC_dx, x)

# Evaluate second derivative at critical points
nature = {cp: d2C_dx2.subs(x, cp) for cp in critical_points}

# Print results
print("First Derivative (dC/dx):", dC_dx)
print("Critical Points (where dC/dx = 0):", critical_points)
print("Second Derivative:", d2C_dx2)
print("Nature of Critical Points:", nature)
 
