#!/usr/local/opt/pyenv/shims/python
import re
from collections import defaultdict
import numpy as np

def solve():
	data = []
	with open("input.txt", "r") as f:
		for line in f:
			row = re.findall("-?\d+", line)
			data.append([int(x.strip()) for x in row])
	# sizes = []
	# for i in range(12000):
	# 	minX = min(x + i*vx for (x, _, vx, _) in data)
	# 	maxX = max(x + i*vx for (x, _, vx, _) in data)
	# 	minY = min(y + i*vy for (_, y, _, vy) in data)
	# 	maxY = min(y + i*vy for (_, y, _, vy) in data)
	# 	sizes.append(maxX - minX + maxY - minY)
	# step = sizes.index(min(sizes))
	step = 10813
	visualize(data, step)
	print("done")

def visualize(data, step):
	data = np.array(data)
	transformed = np.stack([data[:, 0] + data[:, 2] * step, data[:, 1] + data[:, 3] * step], axis=1)
	minX, minY = transformed.min(axis=0)
	transformed[:, 0] -= minX
	transformed[:, 1] -= minY
	# transformed = []
	# for (x, y, vx, vy) in data:
	# 	transformed.append([x + step * vx - minX, y + step * vy - minY])
	text = [[' ' for i in range(200)] for j in range(200)]
	for (x, y) in transformed:
		text[y][x] = '#'
	for row in text:
		print(''.join(row))

if __name__ == "__main__":
	solve()

