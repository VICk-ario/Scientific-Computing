import sympy as sp

# Define symbol s
s = sp.Symbol('s')

# Define the transfer function H(s)
H = 1 / (s**2 + 3*s + 2)

# Factor the denominator
factored_denominator = sp.factor(s**2 + 3*s + 2)

# Compute inverse Laplace Transform
t = sp.Symbol('t', real=True, positive=True)
h_t = sp.inverse_laplace_transform(H, s, t)

# Find the poles (solve denominator = 0)
poles = sp.solve(s**2 + 3*s + 2, s)

# Print results
print("Factored Denominator:", factored_denominator)
print("Inverse Laplace Transform h(t):", h_t)
print("Poles of the System:", poles)
 
