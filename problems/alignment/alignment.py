import sys

def read():
    try:
        result = raw_input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

s1 = "TGAGAGTACGCTATGCTC"
s2 = "TGGAGTACCTATGTC"

#(score, s1, s2)
def findAlign(score, s1, s2, i1, i2, a, b, c):
    if i1 >= len(s1) and i2 >= len(s2):
        return (score, s1, s2)
    elif i1 >= len(s1):
        return findAlign(score, s1+"-", s2, i1+1, i2+1, a, b, c)
    elif i2 >= len(s2):
        return findAlign(score, s1, s2+"-", i1+1, i2+1, a, b, c)
    elif s1[i1] != s2[i2]:
        s1_ = s1[:i1] + '-' + s1[i1:]
        s2_ = s2[:i2] + '-' + s2[i2:]
        if(s1[i1] in s2):
            one_ = findAlign(score -b, s1_, s2, i1+1, i2+1, a, b, c)
        else:
            one_ = (float('-inf'), "", "")
        if(s2[i2] in s1): 
           two_ = findAlign(score -b, s1, s2_, i1+1, i2+1, a, b, c)
        else:
            two_ = (float('-inf'), "", "")
        ign_ = findAlign(score -c, s1, s2, i1+1, i2+1, a, b, c)
        if one_[0] >= two_[0] and one_[0] >= ign_[0]:
            return one_
        elif two_[0] > one_[0] and two_[0] >= ign_[0]:
            return two_
        else:
            return ign_
    else:
        return findAlign(score+a, s1, s2, i1+1, i2+1, a, b, c)

print(findAlign(0, s1, s2, 0, 0, 1.0, 0.7, 0.9))
while True:
    name = read()
    if name == None:
        break
    vals = read()
    inputs = vals.split()
    sys.stdout.write(name)
    for _ in range(int(inputs[0])):
        string1 = read()
        string2 = read()
        print(string1, string2)
        result = findAlign(0.0, string1, string2, 0, 0, float(inputs[1]), float(inputs[2]), float(inputs[3]))
        sys.stdout.write("\n" + result[1])
        sys.stdout.write("\n" + result[2])
    
