#!/usr/local/opt/pyenv/shims/python
import re
from collections import defaultdict
import numpy as np

padding = 50
def solve():
	state = []
	rules = []
	with open("input.txt", "r") as f:
		initial = f.readline()
		initial = initial[15:]
		state = [True if x == "#" else False for x in initial]
		for i in range(padding):
			state.insert(0, False)
			state.append(False)
		f.readline()
		for line in f.readlines():
			line = line.strip()
			pattern = [True if x == '#' else False for x in line[:5]]
			result = True if line[-1] == '#' else False
			rules.append((pattern, result))
	# total = getTotal(state)
	# print("Generation 0: %d" % total)
	for g in range(20):
		next = [False] * len(state)
		for i in range(len(state) - 5):
			for rule in rules:
				if rule[0] == state[i: i+ len(rule[0])]:
					next[i+2] = rule[1]
		state = next
		# iterationCount = getTotal(state)
		# print("Generation %d: %d" % (g + 1, iterationCount))
		# total += iterationCount
	print(getTotal(state))
	print(''.join(['#' if x else '.' for x in state]))
	print("done")

def getTotal(state):
	total = 0
	for i in range(len(state)):
		if state[i]:
			total += i - padding
	return total
if __name__ == "__main__":
	solve()

