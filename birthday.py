import sys
import math

def read():
    try:
        result = raw_input.rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def birthday():
    n, A, B, C, D, = read().split(" ")
    r = ceil(math.sqrt(2*n))
    print(n, A, B, C, D, r)

if __name__ == "__main__":
    birthday()
