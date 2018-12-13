#!/usr/local/opt/pyenv/shims/python
import re
from collections import defaultdict
import numpy as np

def solve():
	data = []
	with open("input.txt", "r") as f:
		for line in f:
			data.append([int(x) for x in re.findall("-?\d+", line)])
	print(data)
	print("done")

if __name__ == "__main__":
	solve()

