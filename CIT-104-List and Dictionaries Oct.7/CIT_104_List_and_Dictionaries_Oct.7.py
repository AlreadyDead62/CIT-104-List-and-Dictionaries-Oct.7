"""
Kitsmiller, Jericho
This program is supposed to accept 
a base-32 number as input. Use the extended hexadecimal-style representation
for base 32, where the digits are:
0-9 and A-V
hexadecimal conversion program
Refer to the example on page 135 of text book.
Hand-written lists and dictionaries
"""
# Binary table 5-bits
textToBinTable = {
    '0' : '00000' , '1' : '00001' ,
    '2' : '00010' , '3' : '00011' , 
    '4' : '00100' , '5' : '00101' ,
    '6' : '00110' , '7' : '00111' ,
    '8' : '01000' , '9' : '01001' , 
    'A' : '01010' , 'B' : '01011' ,
    'C' : '01100' , 'D' : '01101' ,
    'E' : '01110' , 'F' : '01111' , 
    'G' : '10000' , 'H' : '10001' ,
    'I' : '10010' , 'J' : '10011' ,
    'K' : '10100' , 'L' : '10101' , 
    'M' : '10110' , 'N' : '10111' ,
    'O' : '11000' , 'P' : '11001' ,
    'Q' : '11010' , 'R' : '11011' , 
    'S' : '11100' , 'T' : '11101' ,
    'U' : '11110' , 'V' : '11111' ,
}

# Octal is 3 bits
textToOctal = {
    '0' : '000' , '1' : '001' ,
    '2' : '010' , '3' : '011' , 
    '4' : '100' , '5' : '101' ,
    '6' : '110' , '7' : '111' ,
}

# Hexadecimal system 4 bits
textToHex = {
    '0' : '0000' , '1' : '0001' ,
    '2' : '0010' , '3' : '0011' , 
    '4' : '0100' , '5' : '0101' ,
    '6' : '0110' , '7' : '0111' ,
    '8' : '1000' , '9' : '1001' , 
    'A' : '1010' , 'B' : '1011' ,
    'C' : '1100' , 'D' : '1101' ,
    'E' : '1110' , 'F' : '1111' , 
}


def binToDec(binNum):
    """Convert an integer composed of binary digits to decimal.
    (Kept from original code but fixed return placement.)
    Example: 101 -> 5
    """
    decNum = 0
    power = 0
    while binNum > 0:
        decNum += 2 ** power * (binNum % 10)
        binNum //= 10
        power += 1
    return decNum


def base32_to_binary(s):
    """Use the existing textToBinTable to convert a base-32 string to a binary string."""
    s = s.strip().upper()
    if not s:
        raise ValueError("Empty input")
    bits = []
    for ch in s:
        if ch not in textToBinTable:
            raise ValueError(f"Invalid character for base-32: '{ch}'")
        bits.append(textToBinTable[ch])
    binary = "".join(bits).lstrip("0")
    return binary or "0"


def main():
    try:
        user_digit = input("Enter the number you are wanting to convert: ").strip().upper()
        # Convert using the existing dictionaries (minimal change to original approach)
        binary_str = base32_to_binary(user_digit)
        decimal_value = int(binary_str, 2)

    except ValueError as ex:
        print("Input error:", ex)
        return
    except KeyboardInterrupt:
        print("\nCancelled.")
        return

    print("Conversions for", user_digit)
    print(" Decimal :", decimal_value)
    print(" Binary  :", binary_str)
    print(" Octal   :", format(decimal_value, "o"))
    print(" Hex     :", format(decimal_value, "X"))


if __name__ == "__main__":
    main()