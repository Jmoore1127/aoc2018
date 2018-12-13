#!/usr/local/opt/pyenv/shims/python
import re 
from itertools import combinations
from collections import defaultdict

def solve():
	parser = re.compile("#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)")
	claims = []
	with open("input.txt", "r") as f:
		for line in f:
			line = line.strip()
			m = parser.match(line)
			if not m:
				print("FAILED TO MATCH ON: %s" % line)
				exit(1)
			claims.append(Claim(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))

	m = defaultdict(list)
	overlaps = {}
	for c in claims:
		overlaps[c.id] = set()
		for i in range(c.x, c.x + c.width):
			for j in range(c.y, c.y + c.height):
				if m[(i,j)]:
					for number in m[(i, j)]:
						overlaps[number].add(c.id)
						overlaps[c.id].add(number)
				m[(i,j)].append(c.id)
	print(len([k for k in m if len(m[k]) > 1]))
	print([k for k in overlaps if len(overlaps[k]) == 0][0])
	# maxX = 1000
	# maxY = 1000
	# for c in claims: 
	# 	if c.x + c.width > maxX:
	# 		maxX = c.x + c.width
	# 	if c.y + c.height > maxY:
	# 		maxY = c.y + c.height
	# print("%d, %d" % (maxX, maxY))
	
	# for c in claims:
	# 	for i in range(c.y, c.y + c.height):
	# 		for j in range(c.x, c.x + c.width):
	# 			fabric[i][j] += 1
	# overlap = 0
	# for i in range(0, 1000):
	# 	for j in range(0, 1000):
	# 		if fabric[i][j] > 1:
	# 			overlap += 1
	# for pair in combinations(claims, 2):
	# 	overlap += pair[0].overlap(pair[1])
		# if pair[0].intersects(pair[1]):
		# 	print("%d intersects %d" % (pair[0].id, pair[1].id))
	# print(overlap)
	print("done")

class Claim:
	def __init__(self, id, x, y, width, height):
		self.id = int(id)
		self.x = int(x)
		self.y = int(y)
		self.width = int(width)
		self.height = int(height)

	def __str__(self):
		return "Id: %d\tX: %d\tY: %d\tWidth: %d\tHeight: %d\n" % (self.id, self.x, self.y, self.width, self.height)

	def intersects(self, other):
		if self.x > (other.x + other.width) or (self.x + self.width) > other.x:
			return False
		if self.y < (other.y + other.height) or (self.y + self.height) < other.y:
			return False
		return True

	def overlap(self, other):
		# if not self.intersects(other):
		# 	return 0
		return max(0, min(self.x + self.width, other.x + other.width) - max(self.x, self.x)) * max(0, min(self.y + self.height, other.y + other.height) - max(self.y, other.y))
	



if __name__ == "__main__":
	solve()

