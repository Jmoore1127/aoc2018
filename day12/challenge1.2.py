#!/usr/local/opt/pyenv/shims/python
import re
from collections import defaultdict
import numpy as np

# padding = 50
generations = 20
def solve():
	state = []
	rules = defaultdict(lambda: '.')
	with open("input.txt", "r") as f:
		initial = f.readline().strip()
		initial = initial[15:]
		state = list(initial)
		# state = [True if x == "#" else False for x in initial]
		# for i in range(padding):
		# 	state.insert(0, False)
		# 	state.append(False)
		f.readline()
		for line in f.readlines():
			line = line.strip()
			pattern = line[:5] #[True if x == '#' else False for x in line[:5]]
			result = line[-1] #True if line[-1] == '#' else False
			rules[''.join(pattern)] = result
			# rules.append((pattern, result))
	zeroIndex = 0
	for g in range(generations):
		next = ['.' for _ in range(len(state) + 2)] # * (len(state) + 8) # 4 on each end
		state = list('..') + state + list('..')
		for i in range(len(state) - 4):
			replacement = rules[''.join(state[i:i+5])]
			next[i] = replacement
			# for rule in rules:
			# 	if rule[0] == state[i: i + 5]:
			# 		next[i+2] = rule[1]
		if list('..') != next[:2]:
			state = list('..') + next
			zeroIndex += 2
		else:
			state = next
		# state = list('..') + next + list('..')
		# zeroIndex += 2

		print("Generation %d: %s" % (g + 1, ''.join(state)))

	print(getTotal(state, zeroIndex))
	print(''.join(state))
	# print(''.join(['#' if x else '.' for x in state]))
	print("done")

def getTotal(state, zeroIndex):
	total = 0
	for i in range(len(state)):
		if state[i] == '#':
			total += i - zeroIndex
			# total += i - padding
	return total

if __name__ == "__main__":
	solve()

