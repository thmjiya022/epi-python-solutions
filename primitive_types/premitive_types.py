
def count_bits(x):
    """Counts the number of bits set to 1 in an integer."""
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

def parity(x):
    """Computes the parity of a binary word."""
    result = 0
    while x:
        result ^= 1
        x &= x - 1 
    return result
