# bitmasking.py
"""
Bitmasking utilities.
"""

def is_set(mask, pos):
    return (mask & (1 << pos)) != 0

def set_bit(mask, pos):
    return mask | (1 << pos)

def clear_bit(mask, pos):
    return mask & ~(1 << pos)

def toggle_bit(mask, pos):
    return mask ^ (1 << pos)


if __name__ == "__main__":
    mask = 0
    mask = set_bit(mask, 1)
    print(f"After setting bit 1: {bin(mask)}")
    print(f"Is bit 1 set? {is_set(mask, 1)}")
    mask = toggle_bit(mask, 1)
    print(f"After toggling bit 1: {bin(mask)}")
