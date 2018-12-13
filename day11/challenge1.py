#!/usr/local/opt/pyenv/shims/python
import re
from collections import defaultdict
import numpy as np

def solve():
	serial = None
	with open("input.txt", "r") as f:
		serial = int(f.readline().strip())

	print(serial)
	# serial = 39
	grid = [ [0 for x in range(1, 301)] for y in range(1, 301)]
	for i in range(300 - 3):
		for j in range(300 - 3):
			rackId = (j + 1) + 10
			power = rackId * (i + 1)
			power += serial
			power *= rackId
			if power < 100:
				power = 0
			else:
				power = int(str(power)[-3:-2])
			power -= 5
			grid[i][j] = power
	totals = defaultdict(int)
	grid = np.array(grid)
	for size in range(1, 300):
		for i in range(300 - size):
			for j in range(300 - size):
				total = np.sum(grid[i: i + size, j: j + size])
				totals[(j+1, i + 1, size)] = total
		print("Finished size: %d" % size)

	best = None
	bestPower = None
	for k, v in totals.items():
		if bestPower is None or v > bestPower:
			best = k 
			bestPower = v
	# best = max(totals, key=lambda p: p[1])
	print(best)
	print(bestPower)
	print("done")

if __name__ == "__main__":
	solve()

