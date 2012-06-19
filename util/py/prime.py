"""Utility module for primes."""

import math

def prime_generator():
    """Generator for prime numbers.

    Yields:
        Prime numbers in incremental order calculated using the sieve of
        ertosthenes.
    """
    primes = list()
    next_prime = 2
    while True:
        primes.append(next_prime)
        yield next_prime
        is_next_prime = False
        while not is_next_prime:
            if next_prime == 2:
                next_prime = 3
            else:
                next_prime += 2
            next_prime_sqrt = math.sqrt(next_prime)
            for p in primes:
                if p > math.floor(next_prime_sqrt):
                    is_next_prime = True
                    break
                elif not next_prime % p:
                    # Not prime
                    break
