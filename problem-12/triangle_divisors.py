"""Finds the first triangle number with over 500 divisors."""

from python_util.numbers import prime

def triangle_number_generator():
    """Generates triangle numbers.

    Yields:
        Triangle numbers.
    """
    value = 0
    next_addend = 1
    while True:
        value += next_addend
        next_addend += 1
        yield value

def main():
    for triangle_number in triangle_number_generator():
        divisors = prime.num_divisors(triangle_number)
        if divisors >= 500:
            print triangle_number
            break

if __name__ == '__main__':
    main()