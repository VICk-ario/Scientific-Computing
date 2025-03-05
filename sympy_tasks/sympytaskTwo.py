import sympy as sp

# Define matrix A
A = sp.Matrix([[2, 1], [1, 3]])

# Compute determinant of A
det_A = A.det()

# Define the eigenvalues symbolically
lambda_symbol = sp.Symbol('λ')

# Compute characteristic polynomial det(A - λI)
char_eq = (A - lambda_symbol*sp.eye(2)).det()

# Solve for eigenvalues
eigenvalues = sp.solve(char_eq, lambda_symbol)

# Verify that the eigenvalues satisfy the characteristic equation
verification = [char_eq.subs(lambda_symbol, ev) for ev in eigenvalues]

# Print results
print("Determinant of A:", det_A)
print("Characteristic Equation:", char_eq)
print("Eigenvalues:", eigenvalues)
print("Verification (should be zero):", verification)
 
