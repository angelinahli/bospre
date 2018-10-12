import sys

def read():
    try:
        result = raw_input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def print(line):
    sys.stdout.write(line)
