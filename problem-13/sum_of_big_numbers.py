"""Finds the first 10 digits of the sum of 150 digit numbers."""

def main():
    with open('problem-13/numbers.txt', 'r') as num_file:
        number_string = num_file.read()
        number_string = number_string.replace('\n', '')
    numbers = [int(number_string[i:i+50])
               for i in xrange(0, len(number_string), 50)]
    print str(sum(numbers))[:10]

if __name__ == '__main__':
    main()