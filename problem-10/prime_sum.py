"""Sums all primes under 2e6 (see http://projecteuler.net/problem=10)"""

from util.py import prime

_MAX = 2000000

def main():
    total = 0
    for next in prime.prime_generator():
        if next > _MAX:
            break
        total += next
    print total

if __name__ == '__main__':
    main()