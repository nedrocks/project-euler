"""Sums digits in 2^1000"""

from python_util.algo import arith

if __name__ == '__main__':
    print sum([str(a) for a in arith.list_pow(2, 1000)])