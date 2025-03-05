import sympy as sp

# Define symbols
P, e, N = sp.symbols('P e N')

# Define encryption function
C = P**e % N

# Given values
P_val = 7
e_val = 3
N_val = 33

# Compute ciphertext
C_val = pow(P_val, e_val, N_val)  # Python's efficient modular exponentiation

# Compute modular inverse of P (to decrypt)
P_inverse = sp.mod_inverse(P_val, N_val)

# Decrypt: Multiply ciphertext by modular inverse
decrypted_P = (P_inverse * C_val) % N_val

# Print results
print("Ciphertext C:", C_val)
print("Modular Inverse of P:", P_inverse)
print("Decrypted P:", decrypted_P)
 
