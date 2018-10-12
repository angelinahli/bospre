import re

all_lines = """+
| hello    | a  | b|
z |h||
+
|hi!!!|||a|
+""".split("\n")

table = []
maxlen = 0

for line in all_lines:
    if line[0] == "+":
        table.append([])
    else:
        line = line[1:] if line[0] == "|" else line
        cell_vals = re.split(" *\| *", line)
        cell_vals = [val.strip() for val in cell_vals]
        table[-1].append(cell_vals)
        maxlen = max(maxlen, len(cell_vals))

print table

def column_empty(table, ind):
    for largerow in table:
        for subrow in largerow:
            if ind < len(subrow):
                print subrow[ind]
            if ind < len(subrow) and subrow[ind]:
                return False
    return True

print column_empty(table, 4)

"""
print "INPUT"
for line in all_lines:
    print line

print "\nOUTPUT"
for row in table:
    print "+++++++"
    for line in row:
        print "| " + " | ".join(line) + " |"
"""
