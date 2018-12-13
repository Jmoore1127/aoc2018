#!/usr/local/opt/pyenv/shims/python
import re

def solve():
	vals = None
	with open("input.txt", "r") as f:
		line = f.readline()
		vals = [int(x) for x in re.findall("\d+",line)]
	metaTotal, val, _ = process(vals)
	print(metaTotal)
	print(val)

def process(data):
	childCount, metaCount = data[:2]
	data = data[2:]
	vals = []
	metaSum = 0
	for i in range(childCount):
		metaTotal, val, data = process(data)
		metaSum += metaTotal
		vals.append(val)
	metaSum += sum(data[:metaCount])
	if childCount == 0:
		return (metaSum, sum(data[:metaCount]), data[metaCount:])
	else:
		return (
			metaSum,
			sum(vals[i - 1] for i in data[:metaCount] if i > 0 and i <= len(vals)),
			data[metaCount:]
		)
# def process(vals):
# 	allMeta = []
# 	children = getChildren(vals)
# 	allMeta = allMeta + getMetadata(vals)
# 	for child in children:
# 		allMeta = allMeta + process(child)
# 	return allMeta

# def getChildren(vals):
# 	total = vals[0]
# 	meta = vals[1]
# 	childSize = (len(vals) - 2 - meta) / total
# 	children = []
# 	for i in range(total):
# 		children.append(vals[i + 2:childSize])
# 	return children

# def getMetadata(vals):
# 	total = vals[1]
# 	meta = vals[len(vals) - total:]

if __name__ == "__main__":
	solve()

