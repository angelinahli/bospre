import sys
import re

def read():
	try:
		result = raw_input().rstrip ('\n')
	except EOFError:
		result = None
	finally:
		return result

def readAll():
	lines = []
	while True:
		line = read()
		if line == None or line == ".":
			break
		lines.append(line)
	return "".join(lines)	

def getSize(lines):
	# all chars are instructions
	o = 0
	x, y = 0, 0
	upspace = 0
	rspace = 0
	lspace = 0
	dspace = 0
	for char in lines:
		if char == "R":
			o = (o + 1) % 4
		elif char == "L":
			o = (o - 1) % 4
		else:
			moveDict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
			dx, dy = moveDict[o]
			x += dx
			y += dy
			upspace = max(y, upspace)
			dspace = min(y, dspace)
			rspace = max(x, rspace)
			lspace = min(x, lspace)
	return dict(u=abs(upspace), d=abs(dspace), r=abs(rspace), l=abs(lspace))

def makeMap(lines):
	size = getSize(lines)
	numRows = size["u"] + size["d"]
	numCols = size["r"] + size["l"]
	turtMap = [ [ " " for col in range(numCols + 1) ] for row in range(numRows + 1) ]
	o = 0
	x, y = size["l"], size["u"]
	for char in lines:
		if char == "R":
			o = (o + 1) % 4
		elif char == "L":
			o = (o - 1) % 4
		else:
			if char != "M":
				turtMap[y][x] = char
			moveDict = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
			dx, dy = moveDict[o]
			x += dx
			y += dy
	
	return turtMap

while True:
	name = read()
	if name == None:
		break
	drawing = readAll()
	turtMap = makeMap(drawing)
	sys.stdout.write(name + "\n")
	sys.stdout.write("\n")
	for row in turtMap:
		sys.stdout.write("".join(row) + "\n")
	sys.stdout.write("\n")
