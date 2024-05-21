#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers, where each integer
        represents a byte (0-255).

    Returns:
        bool: True if the data set is a valid UTF-8 encoding, otherwise False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the MSB and the bits after the MSB
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Mask to get the relevant bits
        mask = 1 << 7

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # UTF-8 character must be between 2 and 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the no. of bytes remaining in the current UTF-8 character
        num_bytes -= 1

    # All characters must be completely processed
    return num_bytes == 0
