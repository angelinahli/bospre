import sys
import math 

def read():
    result = None
    try: 
        result = raw_input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def parse(line):
    return map(float, line.split(" "))

def get_distance_origin(length, d1, d2):
    if d1 == 0 or d2 == 0:
        return 0
    y1 = d1
    x1 = 0
    
    y2 = ((y1*y1)+(d2*d2)-(length*length))/(2*y1) 
    x2 = math.sqrt((d2*d2)- (y2*y2))
    
    slope = (y2 - y1)/x2
    invslope = -1/slope
    
    xi = -(y1) * (slope / (slope*slope + 1))
    yi = invslope * xi

    dist = math.sqrt((xi*xi) + (yi*yi))
    return dist

def check_touch(rad, length, d1, d2):
    dist = get_distance_origin(length, d1, d2)
    return "TOUCH" if dist <= rad else "NO-TOUCH"

def get_float(num):
    return format(num, '.3f')

def run():
    while True:
        line = read()
        if line == None:
            break
        rad, length, d1, d2 = parse(line)
        touch = check_touch(rad, length, d1, d2)
        print_line = "{r} {l} {d1} {d2} {touch}\n".format(
            r=get_float(rad), l=get_float(length), d1=get_float(d1), d2=get_float(d2), touch=touch)
        sys.stdout.write(print_line)

run()
