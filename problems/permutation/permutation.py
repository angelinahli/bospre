import sys



def read():
    try: 
        result = raw_input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def permutation(l1, l2):
    if len(l1) is not len(l2):
        return False # IMPOSSIBLE
    d1 = countChars(l1)
    d2 = countChars(l2)
    charMap = [-1 for x in range(len(l1))]
    for k1 in d1:
        if k1 not in d2:
            return False #IMPOSSIBLE
        else:
            if len(d1[k1]) is not len(d2[k1]):
                return False #IMPOSSIBLE
            else: 
                for i in d1[k1]:
                    charMap[i-1] = d2[k1].pop()
    return charMap
    

#{'c': [1, 2, 3]}
def countChars(l):
    charDict = {}
    for i in range(len(l)):
        c = l[i]
        if(c not in charDict):
            charDict[c] = [i+1]
        else:
            charDict[c].append(i+1)
    return charDict

while True:
    name = read()
    if name == None:   
        break
    line1 = read()
    line2 = read()
    cMap = permutation(line1, line2)
    sys.stdout.write(name+"\n")
    if not cMap:
        sys.stdout.write("impossible"+"\n")
    else:
        for i in range(len(cMap)):
            sys.stdout.write(line1[i] + ": " + str(i+1) + " -> " + str(cMap[i])+ "\n") 
