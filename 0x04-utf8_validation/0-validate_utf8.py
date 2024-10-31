#!/usr/bin/python3
""" Module to validate UTF-8 encoding. """

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding. Parameters: data (list): A list of integers representing bytes of data. Returns: bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        binary_repr = format(num, '#010b')[-8:]

        if num_bytes == 0:
            if binary_repr.startswith('0'):
                continue
            elif binary_repr.startswith('110'):
                num_bytes = 1
            elif binary_repr.startswith('1110'):
                num_bytes = 2
            elif binary_repr.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            if not binary_repr.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0

