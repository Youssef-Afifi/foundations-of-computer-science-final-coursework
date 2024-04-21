import random  
import time
import math

loop_counter_generate_prime = 0  # Counter for loop iterations in generate prime function
loop_counter_find_private_key = 0  # Counter for loop iterations in find private_key function

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(N):  
    global loop_counter_generate_prime
    while True:  
        loop_counter_generate_prime += 1  # Increment the loop counter
        prime_option = random.randint(2, N)  # Generate a random number
        if is_prime(prime_option):   # Check if the generated number is prime
            return prime_option   #  If prime, return the prime number

N = int(input("Enter n (product of two primes): "))  # Input the product of two primes
e = int(input("Enter public key: "))  # Input the public key
c = int(input("Enter cipher: "))
start_time = time.time()*1000  # Record the starting time in milliseconds

p, q = 0, 0  
while p * q != N:  # Repeat until p*q equals N (product of two primes)
    p = generate_prime(N)  # Generate a prime number p
    q = N//p  # Calculate q based on p

phi_n = (p - 1) * (q - 1)  # Calculate Euler's totient function φ(n)

print("p:", p)  # Print the prime number p
print("q:", q)  # Print the prime number q

def find_private_key(e, phi_n):  
    global loop_counter_find_private_key
    for d in range(2, phi_n):  # Iterate over possible values of d
        loop_counter_find_private_key += 1  # Increment the loop counter
        if (e * d) % phi_n == 1:  # Check if (e * d) % phi_n equals 1
            return d  # If found, return the private key d

d = find_private_key(e, phi_n)  # Find the private key d
print("Private key (d):", d)  # Print the private key d
m = pow(c, d, N) #calculate decrypted message
print("the decrypted message: ", m) #print decrypted messsage
end_time = time.time()  # Record the ending time
exec_time = end_time - start_time  # Calculate the execution time
print("Runtime:", "{:.20f}".format(time.time()*1000 - start_time), "milliseconds")  # Print the execution time in milliseconds

print("Loop iterations in generate_prime:", loop_counter_generate_prime)  # Print the total loop iterations in generate_prime function
print("Loop iterations in find_private_key:", loop_counter_find_private_key)  # Print the total loop iterations in find_private_key function
print("Total loop iterations:", loop_counter_generate_prime + loop_counter_find_private_key)  # Print the total loop iterations
