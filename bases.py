#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

#1. take each digit
#2. find the position of each digit
#3. multiply the digit with the base raised to the power of the position
#4. add all these^ results

# given a string, I need to break apart the digit string into individual digits or characters
# .split() will help!
#right to left, rightmost is 0, reverse digits? .reverse()
# get a for loop and get each digit position
# counter

def encode36(num):

    digit = 9

    if num > digit:
        return string.ascii_lowercase[num-digit-1]
    else:
        return num



# decode("101", 2) => 5
def decode(digits, base):
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    power = 0
    result = 0

    for digit in digits[::-1]:
        digit = int(digit, base) # convert any HEX digits to number value
        result += int(digit)*(base**power)
        power += 1
    
    return result
    
    

# encode(5, 2) => 101
def encode(number, base):
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
 
    final_digits = ""

    while number != 0:
        number, remainder = divmod(number, base)
        final_digits += str(encode36(remainder))
    return final_digits[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    base10Result = decode(digits, base1)
    finalResult = encode(base10Result, base2)
    return finalResult


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
