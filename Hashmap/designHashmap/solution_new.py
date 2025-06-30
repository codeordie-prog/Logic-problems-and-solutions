from typing import Any, Optional, List
from math import sqrt
from solution import HashMap


def is_prime(n: int)->bool:
    if n <= 1: 
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
        
    return True
    

def main():
    primes_hashmap = HashMap()
    n = 100


    for i in range(1, n+1):
        if is_prime(i):
            primes_hashmap[i] = True

    for k in primes_hashmap:
        print(k, end=" ")

if __name__ == "__main__":
    main()