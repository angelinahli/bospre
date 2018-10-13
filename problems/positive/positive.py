import sys
import math

def read():
    try: 
        result = raw_input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def get_xy(A, B, C):
    max_x = int(math.ceil((C - B) / A))
    max_y = int(math.ceil((C - A) / B))
    for x in xrange(1, max_x + 1):
        for y in xrange(1, max_y + 1):
            if (A*x) + (B*y) == C:
                return x, y
    return 0, 0

def solve(line):
    A, B, C = map(int, line.split(" "))
    x, y = get_xy(A, B, C)
    print_line = "{A} * {x} + {B} * {y} = {C}\n".format(A=A, B=B, C=C, x=x, y=y)
    sys.stdout.write(print_line)

def run():
    lines = []
    while True:
        new_line = read()
        if new_line == None:
            break
        lines.append(new_line)
    for line in lines:
        solve(line)

run()
