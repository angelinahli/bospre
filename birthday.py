import sys
import math

def read():
    try:
        result = raw_input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def x(x_prev, index, n, A, B, C, D):
    if index == 0:
        return D
    return ( (A * (x_prev ** 2) ) + (B * x_prev) + C ) % n

def birthday(input_string):
    n, A, B, C, D, = map(int, input_string.split(" "))
    r = math.ceil(math.sqrt(2*n))
    
    seq = [ x(None, 0, n, A, B, C, D) ] # first element
    found_cycle = False
    index = 1
    i = None
    m = None
    while not found_cycle:
        x_prev = seq[-1]
        new_x = x(x_prev, index, n, A, B, C, D)
        if new_x in seq:
            i = seq.index(new_x)
            m = index - i
            found_cycle = True
        seq.append(new_x)
        index += 1

    return n, A, B, C, D, i, m, r

def run():
    all_lines = []
    col_len = 0
    get_len = lambda x: len(str(x))
    while True:
        line = read()
        print "line is:", line
        if line == None:
            break
        data = birthday(line)
        largest_w = max(map(get_len, data))
        col_len = max(col_len, largest_w + 1)
        all_lines.append(birthday(line))
    
    n_cols = 8
    for line in all_lines:
        line_print = []
        for cell in line:
            num_spaces = col_len - get_len(cell)
            cell_print = (" " * num_spaces) + str(cell)
            line_print.append(cell_print)
        sys.stdout.write( "".join(line_print) )

if __name__ == "__main__":
    pass
