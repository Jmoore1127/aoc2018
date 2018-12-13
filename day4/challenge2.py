#!/usr/local/opt/pyenv/shims/python
from collections import defaultdict
import re

def solve():
	patt = re.compile('\[(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2})\]\s(.*)')
	entries = []
	with open("input.txt", "r") as f:
		for line in f:
			match = patt.match(line)
			if not match:
				print("FAILED TO MATCH: %s" % line)
				exit(1)
			entries.append(match.groups())
	currentGuard = -1
	currentIntervalStart = -1
	currentIntervalEnd = -1
	guards = defaultdict(lambda: [0] * 60)
	entries = sorted(entries)
	for entry in entries:
		if "Guard" in entry[5]:
			currentGuard = re.findall("\d+", entry[5])[0]
			continue
		elif "falls asleep" in entry[5]:
			currentIntervalStart = int(entry[4])
		elif "wakes up" in entry[5]:
			currentIntervalEnd = int(entry[4])
			for i in range(currentIntervalStart, currentIntervalEnd):
				guards[currentGuard][i] += 1
	(maxGuard, _) = max(guards.items(), key=lambda g: max(g[1]))
	minute = guards[maxGuard].index(max(guards[maxGuard]))
	print(maxGuard)
	print(minute)
	print(int(maxGuard) * minute)

if __name__ == "__main__":
	solve()

