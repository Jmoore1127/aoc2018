#!/usr/local/opt/pyenv/shims/python
import re 
from collections import defaultdict

def solve():
	points = []
	with open("input.txt", "r") as f:
		for line in f:
			point = re.findall("\d+", line)
			point = tuple(int(c) for c in point)
			points.append(point)


	(x, _) = max(points, key=lambda p: p[0])
	(_, y) = max(points, key=lambda p: p[1])
	shared = 0

	for i in range(x + 1):
		for j in range(y + 1):
			shared += int(sum(manhattan(p, (i, j)) for p in points) < 10000)
	print(shared)
	print("done")

		 
def manhattan(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if __name__ == "__main__":
	solve()

