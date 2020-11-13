import math
import random

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for dvsr in range(3, sqr, 2):
        if n % dvsr == 0:
            return False
    return True

test_n = random.choice(range(0,1000))
print("The test integer is:", test_n)
if is_prime(test_n):
    print("Test integer is prime")
else:
    print("Test integer is NOT prime")

