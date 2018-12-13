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

	(x1, _) = min(points, key=lambda p: p[0])
	(_, y1) = min(points, key=lambda p: p[1])
	(x2, _) = max(points, key=lambda p: p[0])
	(_, y2) = max(points, key=lambda p: p[1])
	s1 = score(x1, y1, x2, y2, 400, points)
	s2 = score(x1, y1, x2, y2, 600, points)

	best = [(s1[k] if s1[k]==s2[k] else 0, k) for k in s2.keys()]
	for area, p in sorted(best):
		print(area, p)
	
	print("done")

def score(x1, y1, x2, y2, size, points):
	score = defaultdict(int)
	for x in range(x1-size, x2+size):
		for y in range(y1-size, y2+size):
			score[closest(x,y,points)] += 1
	return score

def closest(x,y, points):
	distances = [(manhattan(p, (x,y)), p) for p in points]
	distances.sort()
	if distances[0][0] < distances[1][0]:
		return distances[0][1]
	else:
		return (-1, -1)
		 
def manhattan(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if __name__ == "__main__":
	solve()

