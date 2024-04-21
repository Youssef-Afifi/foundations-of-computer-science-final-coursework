import math  # Import the math module for mathematical functions
import time  # Import the time module for time-related functions

# Counter for factorization function
factorization_count = 0

# Counter for extended gcd function
extended_gcd_count = 0

def extended_gcd(a, b):
    global extended_gcd_count
    extended_gcd_count += 1
    x, y = 1, 0  # Initialize coefficients
    while b:
        q, a, b = a // b, b, a % b  # Calculate quotient and remainder
        x, y = y, x - q * y  # Update x and y values
    while x < 0:
        x += phi_n  # Make sure x is positive
    if y < 0:
        y += a  # Make sure y is positive
    return a, x, y  # Return gcd and coefficients

# Function to calculate the modular inverse
def mod_inverse(e, n):
    gcd, x, y = extended_gcd(e, n)  # Find gcd and coefficients using extended gcd
    if gcd != 1:  # If gcd is not 1, modular inverse does not exist
        raise ValueError('Modular inverse does not exist ')
    return x % n  # Return the modular inverse

# Function to perform factorization
def factorization(n):
    global factorization_count
    for i in range(2, int(math.sqrt(n)) + 1):  # Iterate through numbers from 2 to n squared 
        factorization_count += 1
        if n % i == 0:  # If i divides n without remainder
            p = i  # Assign i as p
            q = n // p  # Assign n/i as q
            return p, q  # Return factors
    return None  # If no factors found

# Input from user
n = int(input("Enter the number to factorize: "))  # Input number to factorize
e = int(input("Enter e: "))  # Input public exponent e
c=int((input("please input ciphertext:  ")))
# Function to calculate the extended gcd
start_time = time.time()*1000  # Record the starting time


p, q = factorization(n)  # Perform factorization to get prime factors
phi_n = (q - 1) * (p - 1)  # Calculate Euler's totient function phi(n)
d = mod_inverse(e, phi_n)  # Calculate the private key d
m = pow(c,d,n) #calculate decrypted message
end_time = (time.time()*1000) - start_time  # Record the ending time
 # Calculate execution time

print("message: ",m) # print decrypted message
print("p =", p, "q =", q)  # Print factors p and q
print("d:", d)  # Print the private key d
print(f"Time taken: {end_time:.20f} seconds")  # Print execution time with 20 decimal places
print("Factorization function loop count:", factorization_count)  # Print factorization loop count
print("Extended gcd function loop count:", extended_gcd_count)  # Print extended gcd loop count
