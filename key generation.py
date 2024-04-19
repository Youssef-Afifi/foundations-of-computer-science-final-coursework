import random

# Function to test if a number is prime using Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r*d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to calculate the greatest common divisor of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the modular multiplicative inverse of a mod m
def mod_inv(a, m):
    m0, x0, y0 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, y0 = y0 - q * x0, x0
    return y0 if y0 > 0 else y0 + m0

# Function to generate a random prime number
def rand_prime(bits):
    if bits == 8:
        min_bits = 4
        max_bits = 5
    elif bits == 16:
        min_bits = 8
        max_bits = 9
    else:
        raise ValueError("Invalid number of bits. Must be 8 or 16.")

    prime = random.getrandbits(random.randint(min_bits, max_bits))
    while not is_prime(prime):
        prime = random.getrandbits(random.randint(min_bits, max_bits))
    return prime

# Function to generate a prime number distinct from p
def generate_q(p, bits):
    q = rand_prime(bits)
    while p == q:
        q = rand_prime(bits)
    return q

# Function to generate a distinct public exponent e
def generate_e(eul, p, q):
    e = random.randint(2, eul - 1)
    while gcd(e, eul) != 1 or e == p or e == q:
        e = random.randint(2, eul - 1)
    return e

# Adjust the calculation of the private exponent d to ensure it's not equal to e
def generate_d(e, eul):
    d = mod_inv(e, eul)
    while d == e:
        d = mod_inv(e, eul)
    return d

# Ask the user for the number of bits
bits = int(input("Enter bits for the program 8 or 16: "))

p = rand_prime(bits)
q = generate_q(p, bits)

n = p * q
eul = (p - 1) * (q - 1)

e = generate_e(eul, p, q)
d = generate_d(e, eul)

m = int(input("Please enter a number to encrypt: "))
C = pow(m, e, n)
M = pow(C, d, n)

print("Encrypted:", C)
print("The N is:", n)
print("Public key:", e)
print("Private key:", d)
print("p is:", p)
print("q is:", q)
print("Phi(n) is:", eul)
