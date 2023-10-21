def intToBin(num: int) -> str:
    if num < 0:
        num += 2**16

    binary_str = bin(num)[2:]

    binary_str = binary_str.zfill(16)
    return binary_str